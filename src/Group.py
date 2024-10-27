#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Tlon Group (a Tlon community)"


from typing import Annotated

from Cabal import Cabal
from Channel import Channel
from Cordon import Cordon
from Fleet import Fleet

from pydantic import BaseModel, BeforeValidator
from pydantic_core import Url
from pydantic_extra_types.color import Color
from validators import valid_cover


class Group(BaseModel):
    """Tlon Group, i.e. a community consisting of one or more Channels and one or more Subscribers.

    Attributes:
        path (str): Address of group, forming stem of scry path.
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
    secret: bool = False
    image: Annotated[Color | Url | None, BeforeValidator(valid_cover)]
    title: str
    cover: Annotated[Color | Url | None, BeforeValidator(valid_cover)]
    description: str
    cabals: list[Cabal]
    channels: list[Channel]
    cordon: Cordon
    fleet: Fleet

    def __init__(self, **kwarg):
        super().__init__(**kwarg)

    @classmethod
    def from_key(cls, k: str, d: dict) -> "Group":
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
        image = d["meta"]["image"]
        title = d["meta"]["title"]
        cover = d["meta"]["cover"]
        description = d["meta"]["description"]
        cabals = [Cabal.from_dict(k=k, d=d["cabals"]) for k in d["cabals"].keys()]
        cordon = Cordon.from_dict(d["cordon"])
        fleet = Fleet.from_dict(d=d["fleet"])
        channels = [Channel.from_dict(k=k, d=d["channels"]) for k in d["channels"].keys()]
        return Group(
            path=path,
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
