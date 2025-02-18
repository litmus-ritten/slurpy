#!/usr/bin/env python3

from __future__ import annotations

from rich import print

from slurpy import Console

from .Client import Client

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Tlon Channel"

import datetime
from typing import Any, Dict, List, Optional, Union

from aiohttp import ClientSession, ContentTypeError

from pydantic import BaseModel, BeforeValidator, computed_field, Field
from pydantic_core import Url
from pydantic_extra_types.color import Color
from rich import text

from typing_extensions import Annotated

from .Chantype import Chantype
from .Chat import Chat

from .config import LARGE_PAGE_SIZE, PAGE_SIZE, SCRYJSONHEAD
from .Console import console, log

from .Point import Point

from .util import condense_postid, da2datetime, delimit_postid, format_time, urbts2datetime
from .validators import valid_cover


class Channel(BaseModel):
    """
    A Tlon group channel

    Attributes:
        name (str): The name of the channel.
        chantype (str): The type of the channel.
        join (bool): Whether the channel is joinable.
        added (datetime.datetime): The date and time when the channel was added.
        readers (List[str]): List of cabal names which can read the channel.
        zone (str): The zone of the channel.
        image (Optional[Url]): The image URL of the channel, if any.
        title (str): The title of the channel.
        cover (Color|Url): The cover color or url of the channel.
        description (str): The description of the channel.
    """

    name: str = ""
    owner: Point
    pier_host: Url
    chantype: Chantype
    join: bool = False
    added: datetime.datetime
    readers: List[str]
    zone: str
    image: Annotated[Union[Color, Url, None], BeforeValidator(valid_cover)]
    cover: Annotated[Union[Color, Url, None], BeforeValidator(valid_cover)]
    title: str
    description: str
    content: Union[Chat, None] = Chat.from_empty()
    channel_last_updated: datetime.datetime = datetime.datetime.fromisoformat("1970-01-01")
    channel_latest_message_id: str = "0"
    channel_latest_message_date: datetime.datetime = datetime.datetime.fromisoformat("1970-01-01")

    def append_content(self, c: Chat) -> None:
        self.content.posts.contents += c.posts.contents

    @property
    def tile(self) -> text.Text:
        """
        A tile representing the Channel for pretty-printing in a CLI/TUI context.

        """
        t = text.Text()
        t.append(self.owner.cartouche)
        t.append(text.Text.from_markup(f" {self.chantype.glyph} [bold yellow]{self.title}[/bold yellow] "))
        t.append(text.Text.from_markup(f"@ {format_time(self.added.astimezone())}"))
        return t

    @classmethod
    async def from_dict(cls, k: str, d: Dict[str, dict], pier_host: Point) -> "Channel":
        """
        Create a Channel instance from a dictionary.

        Args:
            k (str): The key representing the channel.
            d (Dict[str, Any]): The dictionary containing channel data.

        Returns:
            Channel: A new Channel instance.
        """
        ds = d[k]
        name = k.split("/")[-1]
        owner = Point(patp=k.split("/")[-2])
        chantype = Chantype.from_str(k.split("/")[0])
        join = ds["join"]  # Probably whether a channel is joined by default
        added = urbts2datetime(urbts=ds["added"])
        readers = [str(e) for e in ds["readers"]]  # ACL for users that can read a channel
        zone = ds["zone"]  # Section in the sidebar the channel is listed in
        image = ds["meta"]["image"]  # Unused at present
        title = ds["meta"]["title"]
        cover = ds["meta"]["cover"]
        description = ds["meta"]["description"]
        a = Channel(
            name=name,
            owner=owner,
            chantype=chantype,
            join=join,
            added=added,
            readers=readers,
            zone=zone,
            image=image,
            title=title,
            cover=cover,
            description=description,
            pier_host=pier_host,
        )
        await a.pull_channel()
        if a.channel_latest_message_id != "0":
            log.info(f"Proceeding from id: {a.channel_latest_message_id}")
            await a.update_channel()
        return a

    async def pull_channel(self):
        scrypath_init = (
            f"{self.pier_host}~/scry/channels/v1/chat/{self.owner.patp}/{self.name}/posts/newer/1/1/outline.json"
        )
        client = await Client.get_session()
        try:
            async with client.get(
                url=scrypath_init,
                headers=SCRYJSONHEAD,
            ) as scry:
                res = await scry.json()
            if res["posts"] != {}:
                self.content = Chat.from_dict(res)
                id = list(res["posts"].keys())[0]
                ud = condense_postid(id)
                self.channel_last_updated = datetime.datetime.now()
                self.channel_latest_message_id = id
                self.channel_latest_message_date = da2datetime(int(ud))
                log.info(f"Init: {self.owner}/{self.title}, first message: {self.channel_latest_message_date}")
            else:
                log.warning(f"Init: {self.owner}/{self.title} but looks empty")
        except ContentTypeError as _:
            log.warning(f"Failed to init channel {self.title}. You may not be presently subscribed.")
            pass

    async def update_channel(self, hush=False, echo_messages=False):
        if not hush:
            log.info(f"Updating: {self.owner}/{self.title}")
        with console.status("") as status:
            while True:
                scrypath = f"{self.pier_host}~/scry/channels/v1/chat/{self.owner.patp}/{self.name}/posts/newer/{self.channel_latest_message_id}/{PAGE_SIZE}/outline.json"
                try:
                    client = await Client.get_session()
                    async with client.get(
                        url=scrypath,
                        headers=SCRYJSONHEAD,
                    ) as scry:
                        res = await scry.json()
                    if res["posts"] != {}:
                        new_content = Chat.from_dict(res)
                        self.append_content(new_content)
                        if echo_messages:
                            for elem in new_content.posts.contents:
                                print(elem.tile)
                        id = list(res["posts"].keys())[0]
                        ud = condense_postid(id)
                        self.channel_last_updated = datetime.datetime.now()
                        self.channel_latest_message_id = id
                        self.channel_latest_message_date = da2datetime(int(ud))
                        status.update(
                            status=f"{self.owner}/{self.title}, latest message: {self.channel_latest_message_date}",
                            spinner="dots",
                        )
                    else:
                        if not hush:
                            log.info(f"Got {len(self.content.posts.contents)} messages")
                        break
                except ContentTypeError:
                    if not hush:
                        log.warning(f"Failed to update channel {self.title}. You may not be presently subscribed.")
                    break
                except TypeError as _:
                    log.warning(
                        f"Channel update for {self.title} errored out: {_}. Reply payload is: {str(res)} Skipping."
                    )
                    break

    def scry_path(self) -> str:
        return f"{self.chantype.external_name}/{self.owner.patp}/{self.name}"
