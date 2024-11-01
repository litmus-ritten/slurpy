#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Urbit Azimuth point representation"

import re
from enum import Enum
from typing import Annotated, Any

import numpy as np
import rich
from cmap import Colormap

from constants import CLANS, EXPECTED_PATP_LEN, EXPECTED_PATP_SHAPE, PATP_SYL, SEIN_RELATIONS
from more_itertools import chunked
from pydantic import BaseModel, computed_field
from pydantic.functional_validators import AfterValidator
from Rank import Rank
from rich.text import Text
from SlurpyExceptions import InvalidPatpError
from urbitob import clan, hex_to_patp, hex_to_patq, patp, patp_to_hex, patp_to_num, patq_to_num, sein
from util import fragment_syllables, rgb_to_hex

CARTOUCHE_LUT = Colormap("gnuplot:rainbow")(np.arange(256))


class Form(Enum):
    """
    Enumeration of valid syllabic encodings of a Point. PAPT is 'scrambled' to obscure star/planet relations, PATQ is not.
    """

    PATP = 0
    PATQ = 1


def ValidPatp(patp: str):
    """Validate a @p string.

    This function validates a @p string by removing hyphens and whitespace,
    splitting it into syllables, and confirming that it has the correct number
    of syllables and follows the correct pattern of alternating syllables. This
    function is slightly stricter than the urbit-ob check, as it also confirms
    that the @p string has the appropriate hyphenation pattern.

    Args:
        patp (str): The @p string to validate.

    Returns:
        str: The original @p string if valid.

    Raises:
        InvalidPatpError: If the @p string is invalid.
    """

    def _ValidPatpShape(patp: str) -> bool:
        """Validate that an @p string has the correct shape.

        Args:
            patp (str): The @p string to validate.

        Returns:
            bool: True if the @p matches a regex in the dictionary
            EXPECTED_PATP_SHAPE, otherwise False.
        """
        for pattern in EXPECTED_PATP_SHAPE.values():
            if re.match(pattern, patp):
                return True
        return False

    p = patp.strip().lower()

    try:
        assert _ValidPatpShape(p)
    except AssertionError:
        raise InvalidPatpError(f"Invalid @p: {patp} does not have the correct shape.")

    if p[0] == "~":  # Remove leading ~ if present.
        p = p[1:]
    p = p.strip().replace("-", "")
    try:
        assert len(p) in EXPECTED_PATP_LEN
    except AssertionError:
        raise InvalidPatpError(
            f"Invalid @p: {patp} does not have the correct length. Expected {EXPECTED_PATP_LEN} but got {len(p)}."
        )
    syll = [p[i : i + 3] for i in range(0, len(p), 3)]
    try:
        for i, v in enumerate(syll[::-1]):
            if i % 2 == 0:
                assert v in PATP_SYL["suffix"]
            else:
                assert v in PATP_SYL["prefix"]
    except AssertionError:
        raise InvalidPatpError(f"Invalid @p: {patp}. Unexpected syllable at byte {i}: {v}.")  # pyright: ignore
    return patp


class Point(BaseModel):
    """Represents a point in the Urbit network.

    Attributes:
        patp (str): The @p address of the point.
    """

    patp: Annotated[str, AfterValidator(ValidPatp)]

    @classmethod
    def from_hex(cls, h: str) -> Any:
        """Attempts to parse a hexadecimal string to a Point.

        Args:
            h (str): The hexadecimal string to parse.

        Returns:
            Any: A Point object.

        Raises:
            InvalidPatpError: If the hexadecimal string does not correspond to a valid @p.
        """
        try:
            return Point(patp=hex_to_patp(h))
        except Exception:
            raise InvalidPatpError(f"Hexadecimal string '{h}' does not correspond to a valid @p.")

    @classmethod
    def from_num(cls, i: int | str) -> Any:
        """Attempts to parse an integer or thousands-delimited integer string to a Point.

        Args:
            i (int | str): The integer or thousands-delimited integer string to parse.

        Returns:
            Any: A Point object.

        Raises:
            ValueError: If the input cannot be interpreted as an integer.
            InvalidPatpError: If the integer does not correspond to a valid @p.
        """
        try:
            if isinstance(i, str):
                i = int(i.replace(".", ""))
        except Exception:
            raise ValueError(f"Could not interpret {i} as an integer.")
        try:
            return Point(patp=hex_to_patp(hex(int(i))))
        except Exception:
            raise InvalidPatpError(f"Integer '{i}' does not correspond to a valid @p.")

    @classmethod
    def from_patq(cls, h: str) -> Any:
        """Attempts to parse a patq (@q) string to a Point.

        Args:
            h (str): The patq string to parse.

        Returns:
            Any: A Point object.

        Raises:
            InvalidPatpError: If the patq string does not correspond to a valid @p.
        """
        try:
            return Point(patp=patp(patq_to_num(h)))
        except Exception:
            raise InvalidPatpError(f"@q string '{h}' does not correspond to a valid @p.")

    def syllables(self, form: Form) -> list[str]:
        """Retrieves syllables for the given form (patp or patq).

        Args:
            form (Form): The form to retrieve syllables for.

        Returns:
            list[str]: A list of syllables.

        Raises:
            KeyError: If the provided form is not supported.
        """
        forms = {Form.PATP: self.patp, Form.PATQ: self.patq}
        try:
            return fragment_syllables(forms[form])
        except KeyError as _:
            raise _

    @property
    def patp_syllables(self) -> list[str]:
        """Returns the syllables for the @p format.

        Returns:
            list[str]: A list of syllables in @p format.
        """
        return self.syllables(Form.PATP)

    @property
    def patq_syllables(self) -> list[str]:
        """Returns the syllables for the @q format.

        Returns:
            list[str]: A list of syllables in @q format.
        """
        return self.syllables(Form.PATQ)

    def syllable_indices(self, form: Form) -> list[int]:
        """Calculates the syllable indices for the given form.

        Args:
            form (Form): The form to calculate syllable indices for.

        Returns:
            list[int]: A list of syllable indices.
        """
        forms = {Form.PATP: self.patp_syllables, Form.PATQ: self.patq_syllables}
        return [
            (PATP_SYL["prefix"][v] if i % 2 != 0 else PATP_SYL["suffix"][v]) for i, v in enumerate(forms[form][::-1])
        ]

    @property
    def patp_indices(self) -> list[int]:
        """Returns the syllable indices for the @p format.

        Returns:
            list[int]: A list of syllable indices for @p format.
        """
        return self.syllable_indices(Form.PATP)

    @property
    def patq_indices(self) -> list[int]:
        """Returns the syllable indices for the @q format.

        Returns:
            list[int]: A list of syllable indices for @q format.
        """
        return self.syllable_indices(Form.PATQ)

    @computed_field
    @property
    def patq(self) -> str:
        """Represents the Point in @q format, which is a syllabic un-obfusated form.

        Returns:
            str: The Point in @q format.

        Note:
            Provided by urbit-ob.
        """
        return hex_to_patq(self.index_hex)

    @computed_field
    @property
    def index(self) -> int:
        """Represents the Point in integer format.

        Returns:
            int: The Point in integer format.

        Note:
            Provided by urbit-ob.
        """
        return patp_to_num(self.patp)

    @computed_field
    @property
    def index_delimited(self) -> str:
        """Represents the Point in integer format with thousands dot delimiters.

        Returns:
            str: The Point in integer format with thousands dot delimiters.
        """
        a = list(chunked(str(self.index)[::-1], n=3))
        a = ".".join(["".join(e) for e in a])[::-1]

        return a

    @computed_field
    @property
    def index_hex(self) -> str:
        """Represents the Point in hexadecimal format.

        Returns:
            str: The Point in hexadecimal format.

        Note:
            Provided by urbit-ob.
        """
        return f"0x{patp_to_hex(self.patp)}"

    @computed_field
    @property
    def rank(self) -> Rank:
        """Returns the Rank of the point.

        Returns:
            Rank: The Rank of the point.
        """
        return CLANS[clan(self.patp)]

    @property
    def root(self) -> Any:
        """Returns the root (highest ranked ancestor) of a Point.

        Returns:
            Any: The root Point object.

        Note:
            The root of a galaxy is itself.
        """
        if self.rank != Rank.CZAR:
            return self.ancestors[-1]
        else:
            return self

    @property
    def greatgrandparent(self) -> Any | None:
        """Returns the great grandparent of the point.

        Returns:
            Any | None: The great grandparent of the point, or None if the point doesn't have a great grandparent.

        Note:
            Only moons have great grandparents.
        """
        if self.rank.value != Rank.EARL.value:
            return None
        else:
            return self.parent.parent.parent  # pyright: ignore

    @property
    def grandparent(self) -> Any | None:
        """Returns the grandparent of the point.

        Returns:
            Any | None: The grandparent of the point, or None if the point doesn't have a grandparent.

        Note:
            Comets do not have grandparents.
        """
        if (self.rank.value <= Rank.KING.value) | (self.rank == Rank.PAWN):
            return None
        else:
            return self.parent.parent  # pyright: ignore

    @property
    def parent(self) -> Any | None:
        """Returns the parent of the point.

        Returns:
            Any | None: The parent of the point, or None if the point doesn't have a parent (galaxies don't have parents).
        """
        if self.rank.value <= Rank.CZAR.value:
            return None
        else:
            return Point(patp=sein(self.patp))

    @property
    def ancestors_patp_list(self) -> list[str]:
        """Returns the ancestor list of a Point in ascending order of @ps.

        Returns:
            List[str]: The ancestor list of the Point in ascending order of @ps.
        """
        return [p.patp for p in self.ancestors]

    @computed_field
    @property
    def ancestors_patp_dict(self) -> dict:
        """Returns the ancestor list of a Point as a dictionary.

        Returns:
            dict: The ancestor list of the Point as a dictionary where the keys are non-null relations.
        """
        d = {
            k: v.patp
            for k, v in {
                "galaxy": self.galaxy,
                "star": self.star,
                "planet": self.planet,
            }.items()
            if v is not None
        }
        return d

    @property
    def galaxy(self) -> Any | None:
        """Report parent galaxy if it exists.

        Returns:
            Any | None: The parent galaxy object if it exists, None otherwise.
        """
        r = SEIN_RELATIONS[self.rank]["galaxy"]
        if r is not None:
            return self.ancestors[r]
        return None

    @property
    def star(self) -> Any | None:
        """Report parent star if it exists. The try/except is a hacky way of catching galaxy moons.

        Returns:
            Any | None: The parent star object if it exists, None otherwise.
        """
        r = SEIN_RELATIONS[self.rank]["star"]
        try:
            if r is not None:
                return self.ancestors[r]
        except IndexError:
            return None

    @property
    def planet(self) -> Any | None:
        """Report parent planet if it exists. The try/except is a hacky way of catching star moons.

        Returns:
            Any | None: The parent planet object if it exists, None otherwise.
        """
        r = SEIN_RELATIONS[self.rank]["planet"]
        try:
            if r is not None:
                return self.ancestors[r]
        except IndexError:
            return None

    @property
    def ancestors(self) -> list[Any]:
        """Evaluate the chain of ancestors of a Point through recursive tree ascent.

        Returns:
            List[Any]: A list of the ancestors of a Point in ascending order.
        """

        def _recurse_parent(p: Point) -> list[Point]:
            if p.parent is not None:
                return [p, *_recurse_parent(p.parent)]
            else:
                return [p]

        return _recurse_parent(self)[1:]

    def related(self, other):
        """Check if a Point is related to another.

        No point is related to itself. If two non-comets (PAWNs) are related they
        will share an ancestor galaxy. All comets (PAWNs) are related to one another.
        We don't consider comets (PAWNs) to be related to any non-comets except for ~zod.

        Args:
            other (Point): The Point to check against.

        Returns:
            bool: True if this Point is related to other, False otherwise.
        """
        if self == other:
            return False
        elif self.rank == other.rank == Rank.PAWN:
            return True
        elif ((self.rank == Rank.PAWN) & (other.rank != Rank.PAWN)) | (
            (self.rank != Rank.PAWN) & (other.rank == Rank.PAWN)
        ):
            if (self == Point(patp="~zod")) | (other == Point(patp="~zod")):
                return True
            else:
                return False
        elif self.root == other.root:
            return True
        else:
            return False

    def parent_of(self, other):
        """Check if a Point is the parent (direct ancestor of other).

        Args:
            other (Point): The Point to check against.

        Returns:
            bool: True if this Point is the parent of other, False otherwise.
        """
        return self == other.parent

    def child_of(self, other):
        """Check if a Point is the child (direct descendent of other).

        Args:
            other (Point): The Point to check against.

        Returns:
            bool: True if this Point is the child of other, False otherwise.
        """
        return self.parent == other

    def cousin_of(self, other) -> bool:
        """Check if two Points are cousins.

        Two Points are considered cousins if they have the same parent.
        A Point is not considered cousins with itself.

        Args:
            other (Point): The Point to compare with.

        Returns:
            bool: True if the Points are cousins, False otherwise.
        """
        if self == other:
            return False
        try:
            assert hasattr(self.parent, "parent") & hasattr(other.parent, "parent")
            return self.parent.parent == other.parent.parent  # pyright: ignore
        except AssertionError:
            return False

    def sibling_of(self, other) -> bool:
        """Check if two Points are siblings.

        Two Points are considered siblings if they have the same parent.
        A Point is not considered siblings with itself.

        Args:
            other (Point): The Point to compare with.

        Returns:
            bool: True if the Points are siblings, False otherwise.
        """
        if self == other:
            return False
        return self.parent == other.parent

    def __str__(self) -> str:
        """Returns a string representation of the Point.

        Returns:
            str: A string containing the rank glyph and patp of the Point.
        """
        return f"{self.rank.glyph} {self.patp}"

    def __hash__(self):
        """Computes the hash value for the Point.

        Returns:
            int: The hash value of the string representation of the Point.
        """
        return hash(str(self))

    def __lt__(self, other):
        """Compares this Point with another for less than.

        Args:
            other: Another Point object to compare with.

        Returns:
            bool: True if this Point's index is less than the other's, False otherwise.
        """
        return self.index < other.index

    def __le__(self, other):
        """Compares this Point with another for less than or equal to.

        Args:
            other: Another Point object to compare with.

        Returns:
            bool: True if this Point's index is less than or equal to the other's, False otherwise.
        """
        return self.index <= other.index

    def __gt__(self, other):
        """Compares this Point with another for greater than.

        Args:
            other: Another Point object to compare with.

        Returns:
            bool: True if this Point's index is greater than the other's, False otherwise.
        """
        return self.index > other.index

    def __ge__(self, other):
        """Compares this Point with another for greater than or equal to.

        Args:
            other: Another Point object to compare with.

        Returns:
            bool: True if this Point's index is greater than or equal to the other's, False otherwise.
        """
        return self.index >= other.index

    @property
    def cartouche(self, pq="q") -> Text:
        """
        Cartouche representation of a Point, as a capsule with up to two colours.
        Coefficients for determining correct light/dark text are from Max Chuhryaev (w3core on GitHub) but I'm not sure quite where they were mentioned.

        Args:
            pq (str, optional): Determines whether to use 'patp' or 'patq' indexing. Defaults to "q".

        Returns:
            Text: A Rich Text object representing the cartouche.

        TODO:
            Refactor this method, as it's currently complex and difficult to maintain.
        """
        t = Text()
        left = ""
        right = ""
        t.append(left, style="white")
        t.append(f"{str(self.rank.glyph)} ", style="black on white")
        if pq == "p":
            syls = list(zip(self.patp_syllables, self.patp_indices[::-1]))
        else:
            syls = list(zip(self.patp_syllables, self.patq_indices[::-1]))
        syls = [list(e) for e in syls]
        if len(syls) >= 4:
            syls = [syls[i] for i in [0, 1, -2, -1]]
            syls[0][1] = syls[1][1]
            syls[2][1] = syls[3][1]
        for i, v in enumerate(syls):
            r, g, b = CARTOUCHE_LUT[v[1]][:-1]
            if r * 0.299 + g * 0.587 + b * 0.144 < 0.5:
                c = "#FFFFFF"
            else:
                c = "#282828"
            t.append(f"{v[0]}", style=f"{c} on {rgb_to_hex(CARTOUCHE_LUT[v[1]])}")
            if i % 2 == 1 and i != len(syls) - 1:
                if self.rank == Rank.DUKE:
                    t.append(" ", style="bold black on bright_white")
                if self.rank == Rank.EARL:
                    t.append(":", style="bold black on bright_white")
                if self.rank == Rank.PAWN:
                    t.append("|", style="bold black on bright_white")
        t.append(right, style=f"{rgb_to_hex(CARTOUCHE_LUT[syls[-1][1]])}")
        return t
