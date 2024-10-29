#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Pydantic validators for slurpy"

import re

from constants import PATP_SYL

from pydantic_core import Url
from pydantic_extra_types.color import Color

from SlurpyExceptions import MalformedCodeError

from util import fragment_syllables


def valid_code(v: str) -> str:
    """
    Pydantic BeforeValidator for an Urbit login code.

    This validator checks if the input string consists of valid prefix-suffix pairs.
    TODO: It should be refactored into a hierarchical validator for Urbit syllables.

    Args:
        v (str): The input string to validate.

    Returns:
        str: The validated and lowercase input string.

    Raises:
        MalformedCodeError: If the input string is malformed or contains invalid syllables.
    """
    v = v.lower()
    if re.search(r"[a-z]{6}-[a-z]{6}-[a-z]{6}-[a-z]{6}", v) is not None:
        syllables = fragment_syllables(f"~{v}")
        try:
            assert False not in [e in list(PATP_SYL["prefix"].keys()) for e in syllables[::2]]
            assert False not in [e in list(PATP_SYL["suffix"].keys()) for e in syllables[1::2]]
        except AssertionError:
            raise MalformedCodeError(message="Supplied login code has at least one invalid syllable")
        return v
    else:
        raise MalformedCodeError(message="Supplied login code is malformed")


def valid_cover(v: str) -> Color | Url | None:
    """
    Pydantic BeforeValidator for a cover, which can be a Color, Url, or empty.

    Args:
        v (str): The input value to validate.

    Returns:
        Color | Url | None: A Color object if the input is a valid color,
            a Url object if the input is a valid URL, or None if the input is empty.

    Raises:
        ValidationError: If the input is neither a valid color nor a valid URL.
    """
    if v == "":
        return None
    try:
        c = Color(value=v)
        return c
    except Exception as _:
        pass
    try:
        u = Url(v)
        return u
    except Exception as _:
        raise _
