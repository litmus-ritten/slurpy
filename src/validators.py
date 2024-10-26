#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Pydantic validators for slurpy"

from pydantic_core import Url
from pydantic_extra_types.color import Color


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
