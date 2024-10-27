#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Tlon Channel"

import datetime
from enum import Enum
from typing import Any, Dict, List

from pydantic import BaseModel, BeforeValidator
from pydantic_core import Url
from pydantic_extra_types.color import Color

from SlurpyExceptions import UnknownChannelType
from typing_extensions import Annotated

from util import urbts2datetime
from validators import valid_cover


class Chantype(Enum):
    CHAT = 0
    GALLERY = 1
    DIARY = 2

    @classmethod
    def from_str(cls, s: str) -> "Chantype":
        try:
            return CHANTYPE_STRINGS[s]["enum"]
        except KeyError:
            raise UnknownChannelType(f"{s} not in {list(CHANTYPE_STRINGS.keys())}")


CHANTYPE_STRINGS = {
    "chat": {"enum": Chantype.CHAT, "external_name": "chat", "external_name_plural": "chats", "glyph": "📣"},
    "heap": {"enum": Chantype.GALLERY, "external_name": "gallery", "external_name_plural": "galleries", "glyph": "🖼️"},
    "diary": {"enum": Chantype.DIARY, "external_name": "diary", "external_name_plural": "diaries", "glyph": "📗"},
}


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
    chantype: Enum
    join: bool = False
    added: datetime.datetime
    readers: List[str]
    zone: str
    image: Annotated[Color | Url | None, BeforeValidator(valid_cover)]
    title: str
    cover: Annotated[Color | Url | None, BeforeValidator(valid_cover)]
    description: str

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize a Channel instance.

        Args:
            **kwargs: Keyword arguments to initialize the Channel attributes.
        """
        super(Channel, self).__init__(**kwargs)

    @classmethod
    def from_dict(cls, k: str, d: Dict[str, dict]) -> "Channel":
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
        chantype = Chantype.from_str(k.split("/")[0])
        join = ds["join"]  # Probably whether a channel is joined by default
        added = urbts2datetime(urbts=ds["added"])
        readers = [str(e) for e in ds["readers"]]  # ACL for users that can read a channel
        zone = ds["zone"]  # Section in the sidebar the channel is listed in
        image = ds["meta"]["image"]  # Unused at present
        title = ds["meta"]["title"]
        cover = ds["meta"]["cover"]
        description = ds["meta"]["description"]
        return Channel(
            name=name,
            chantype=chantype,
            join=join,
            added=added,
            readers=readers,
            zone=zone,
            image=image,
            title=title,
            cover=cover,
            description=description,
        )
