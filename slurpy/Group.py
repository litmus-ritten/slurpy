#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Tlon Group (a Tlon community)"


from typing import Annotated, Union

from pydantic import BaseModel, BeforeValidator, ConfigDict
from pydantic_core import Url
from pydantic_extra_types.color import Color
from rich.text import Text

from .Cabal import Cabal
from .Channel import Channel
from .Cordon import Cordon
from .Fleet import Fleet
from .Point import Point
from .validators import valid_cover


class Group(BaseModel):
    """Tlon Group, i.e. a community consisting of one or more Channels and one or more Subscribers.

    Attributes:
        path (str): Address of group, forming stem of scry path.
        host (Point): Ship hosting the Group.
        secret (bool): Whether the group is publicly enumerable.
        image (Color | Url | None): Group sidebar avatar.
        title (str): Group name.
        cover (Color | Url | None): Sidebar hero image.
        description (str): Group description which pops up in search/join dialogs.
        cabals (list[Cabal]): List of logical subscriber groups.
        channels (list[Channel]): List of chats, diaries, heaps, etc.
        cordon (Cordon): Banned ships and ranks (for a public group) or invited/asking ships (for a private group).
        fleet (Fleet): Subscribers.
    """

    path: str
    host: Point
    pier_host: Point
    secret: bool = False
    image: Annotated[Union[Color, Url, None], BeforeValidator(valid_cover)]
    cover: Annotated[Union[Color, Url, None], BeforeValidator(valid_cover)]
    title: str
    description: str
    cabals: list[Cabal]
    channels: dict[str, Channel]
    cordon: Cordon
    fleet: Fleet

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    async def from_key(cls, k: str, d: dict, pier_host: Point) -> "Group":
        """Parse a group from a key/value pair.

        Args:
            k (str): The key.
            d (dict): The dictionary containing group data.

        Returns:
            Group: A new Group instance.
        """
        path = k
        d = d[k]
        secret = bool(d["secret"])
        host = Point(patp=path.split("/")[0])
        image = d["meta"]["image"]
        title = d["meta"]["title"]
        cover = d["meta"]["cover"]
        description = d["meta"]["description"]
        cabals = [Cabal.from_dict(k=k, d=d["cabals"]) for k in d["cabals"].keys()]
        cordon = Cordon.from_dict(d["cordon"])
        fleet = Fleet.from_dict(d=d["fleet"])
        print(f"Pier host: {pier_host}")
        channels = {
            k.split("/")[-1]: await Channel.from_dict(k=k, d=d["channels"], pier_host=pier_host)
            for k in d["channels"].keys()
        }
        return Group(
            path=path,
            host=host,
            pier_host=host,
            secret=secret,
            image=image,
            title=title,
            cover=cover,
            description=description,
            cabals=cabals,
            channels=channels,
            cordon=cordon,
            fleet=fleet,
        )

    @property
    def tile(self) -> Text:
        t = Text()
        t.append(self.host.cartouche)
        t.append("/")
        t.append(
            Text.from_markup(
                f"[green]{self.title}:[/green] {self.description.replace("\n", "•")} ({len(self.fleet.contents)} subscribers)"
            )
        )

        return t

    @property
    def normalised_title(self) -> str:
        t = self.title
        t = t.replace("~", "")
        t = t.replace("/", ".")
        return t

    async def update(self, hush: bool = False, echo_messages=False) -> None:
        for chan in self.channels.items():
            await chan[1].update_channel(hush, echo_messages)
