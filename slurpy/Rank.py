#!/usr/bin/env python3

"""Enumeration of valid ranks of an Urbit point."""

from enum import Enum
from typing import Any
from .SlurpyExceptions import InvalidRankError

RANK_STRINGS = {
    0: {
        "noble_name": "czar",
        "noble_name_alt": "czar",
        "nautical_name": "carrier",
        "external_name": "galaxy",
        "external_name_plural": "galaxies",
        "glyph": "🌀",
        "byte_width": 1,
    },
    1: {
        "noble_name": "king",
        "noble_name_alt": "king",
        "nautical_name": "cruiser",
        "external_name": "star",
        "external_name_plural": "stars",
        "glyph": "🌟",
        "byte_width": 2,
    },
    2: {
        "noble_name": "duke",
        "noble_name_alt": "duke",
        "nautical_name": "destroyer",
        "external_name": "planet",
        "external_name_plural": "planets",
        "glyph": "🌏",
        "byte_width": 4,
    },
    3: {
        "noble_name": "earl",
        "noble_name_alt": "earl",
        "nautical_name": "yacht",
        "external_name": "moon",
        "external_name_plural": "moons",
        "glyph": "🌙",
        "byte_width": 8,
    },
    4: {
        "noble_name": "pawn",
        "noble_name_alt": "wolf",
        "nautical_name": "submarine",
        "external_name": "comet",
        "external_name_plural": "comets",
        "glyph": "☄️ ",
        "byte_width": 16,
    },
}


class Rank(Enum):
    """Enumeration of valid Azimuth ranks."""

    CZAR = 0
    KING = 1
    DUKE = 2
    EARL = 3
    PAWN = 4

    def __str__(self) -> str:
        """Human-readable summary of Rank.

        Returns:
            str: A string representation of the Rank.
        """
        return f"({self.name}, {self.value}): {RANK_STRINGS[self.value]}"

    @property
    def internal_name(self) -> str:
        """Developer-facing name of the rank, following the four-letter noble theme.

        Returns:
            str: The internal name of the rank.
        """
        return self.noble_name

    @property
    def noble_name_alt(self) -> str:
        """Alternative noble name of the Rank, based on some lore shared by ~lidreg-dillut.

        Returns:
            str: The alternative noble name of the rank.
        """
        return RANK_STRINGS[self.value]["noble_name_alt"]

    @property
    def noble_name(self) -> str:
        """Noble name of the Rank.

        Returns:
            str: The noble name of the rank.
        """
        return RANK_STRINGS[self.value]["noble_name"]

    @property
    def nautical_name(self) -> str:
        """(Ancient) nautical name of the rank.

        Sourced from https://alexkrupp.typepad.com/sensemaking/2013/12/a-brief-introduction-to-urbit.html,
        of largely historical interest.

        Returns:
            str: The nautical name of the rank.
        """
        return RANK_STRINGS[self.value]["nautical_name"]

    @property
    def external_name(self) -> str:
        """User-facing name of the rank, following Azimuth's astronomical theme.

        Returns:
            str: The external name of the rank.
        """
        return RANK_STRINGS[self.value]["external_name"]

    @property
    def external_name_plural(self) -> str:
        """User-facing name of the rank, following Azimuth's astronomical theme, pluralised.

        Returns:
            str: The external name of the rank, pluralised.
        """
        return RANK_STRINGS[self.value]["external_name_plural"]

    @property
    def glyph(self) -> str:
        """A cute(?) emoji representation of the rank.

        Returns:
            str: Single emoji depicting the rank.
        """
        return RANK_STRINGS[self.value]["glyph"]

    @property
    def byte_width(self) -> int:
        """How many bytes (and by extension how many syllables) are used to represent the rank.

        Returns:
            int: The byte width of the rank.
        """
        return RANK_STRINGS[self.value]["byte_width"]

    @classmethod
    def from_str(cls, s: str) -> Any | Exception:
        """Parse a string to generate a Rank, or else raise an exception.

        Args:
            s (str): String naming the rank according to any of the known conventions.

        Returns:
            Any | Exception: A Rank object or an exception if the string is not a known rank name.

        Raises:
            InvalidRankError: If the input string is not a known rank name.
        """
        for _ in RANK_STRINGS.values():
            n = (
                _["noble_name"],
                _["noble_name_alt"],
                _["nautical_name"],
                _["external_name"],
            )
            if s.strip().lower() in n:
                return Rank[_["noble_name"].upper()]
        raise InvalidRankError(f"'{s}' is not a known rank name")
