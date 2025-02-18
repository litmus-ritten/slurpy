#!/usr/bin/env python3


__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Enumeration of Tlon Channel types"

from enum import Enum

from .SlurpyExceptions import UnknownChannelTypeError


class Chantype(Enum):
    CHAT = 0
    GALLERY = 1
    DIARY = 2
    QUORUM = 3

    @classmethod
    def from_str(cls, s: str) -> "Chantype":
        try:
            return CHANTYPE_NAMES[s]["enum"]
        except KeyError:
            raise UnknownChannelTypeError(f"{s} not in {list(CHANTYPE_NAMES.keys())}")

    @property
    def internal_name(self):
        return CHANTYPE_ATTRIBUTES[self]["internal_name"]

    @property
    def external_name(self):
        return CHANTYPE_ATTRIBUTES[self]["external_name"]

    @property
    def external_name_plural(self):
        return CHANTYPE_ATTRIBUTES[self]["external_name_plural"]

    @property
    def glyph(self):
        return CHANTYPE_ATTRIBUTES[self]["glyph"]


CHANTYPE_NAMES = {
    "chat": {"enum": Chantype.CHAT},
    "heap": {"enum": Chantype.GALLERY},
    "diary": {"enum": Chantype.DIARY},
    "quorum": {"enum": Chantype.QUORUM},
}

CHANTYPE_ATTRIBUTES = {
    Chantype.CHAT: {
        "internal_name": "chat",
        "external_name": "chat",
        "external_name_plural": "chats",
        "glyph": "📣",
    },
    Chantype.GALLERY: {
        "internal_name": "heap",
        "external_name": "gallery",
        "external_name_plural": "galleries",
        "glyph": "🍱",
    },
    Chantype.DIARY: {
        "internal_name": "diary",
        "external_name": "notebook",
        "external_name_plural": "notebook",
        "glyph": "📗",
    },
    Chantype.QUORUM: {
        "internal_name": "quorum",
        "external_name": "quorum (deprecated)",
        "external_name_plural": "quora (deprecated)",
        "glyph": "💀",
    },
}
