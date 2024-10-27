#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Utility functions for slurpy"

import datetime

from typing import Any, Dict, Union

from constants import DA_EPOCH, DA_SECOND


def unix2da(time: int) -> str:
    """Convert unix time to urbit time.

    Args:
        time (int): Unix timestamp in seconds.

    Returns:
        str: Urbit time as a string.

    Raises:
        ValueError: If the input time is negative or too large.
    """
    time = int((time * DA_SECOND) / 1000)
    return f"/{time + DA_EPOCH}"


def urbts2datetime(urbts: int) -> datetime.datetime:
    """Convert urbit time to datetime.

    Args:
        urbts (int): Urbit timestamp in milliseconds.

    Returns:
        datetime.datetime: Datetime object representing the Urbit time.

    Raises:
        ValueError: If the input urbts is negative or too large.
    """
    t = datetime.datetime.fromtimestamp(urbts / 1000, tz=datetime.UTC)
    return t


def urbitdate(d: str) -> datetime.datetime:
    """Convert Urbit date string to datetime object.

    Args:
        d (str): Urbit date string in the format "/YYYY.MM.DD..HH.MM.SS".

    Returns:
        datetime.datetime: Datetime object representing the Urbit date.

    Raises:
        ValueError: If the input string is not in the correct format.
    """
    d = d[1:]
    date, time = d.split("..")
    date = list(map(int, date.split(".")))
    year, month, day = date
    time = list(map(int, time.split(".")))
    hour, minute, second = time
    return datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)


def tlonts2dt(t: str | int) -> datetime.datetime:
    """
    Convert Tlon timestamp into datetime object.

    Args:
        t (str | int): Tlon timestamp in milliseconds past Unix epoch.

    Returns:
        datetime.datetime: Converted datetime object.
    """
    return datetime.datetime.fromtimestamp(int(t) / 1000)


def format_time(dt: datetime.datetime) -> str:
    """
    Format datetime for terminal display.

    Args:
        dt (datetime.datetime): Datetime object to be formatted.

    Returns:
        str: Formatted datetime string in the format "YYYY-MM-DD HH:MM".
    """
    return f"{dt.year}-{dt.month}-{dt.day} {dt.hour:02d}:{dt.minute:02d}"


def render_element(d: Union[str, Dict[str, Any]]) -> str:
    """
    Recursively render a dict encoding Tlon rich text to a string which can be parsed by Rich.

    Args:
        d (Union[str, Dict[str, Any]]): The input element to render, either a string or a dictionary.

    Returns:
        str: The rendered string that can be parsed by Rich.

    Raises:
        ValueError: If an unsupported element type is encountered.

    Examples:
        >>> render_element("Hello")
        'Hello'
        >>> render_element({"italics": "Hello"})
        '[italic]Hello[/italic]'
        >>> render_element({"bold": {"italics": "Hello"}})
        '[bold][italic]Hello[/italic][/bold]'
    """
    if type(d) == str:
        return d
    if type(d) == dict:
        if list(d.keys())[0] == "italics":
            return (
                f"[italic]{d['italics']}[/italic]"
                if type(d["italics"]) == str
                else f"[italic]{render_element(d['italics'][0])}[/italic]"
            )
        if list(d.keys())[0] == "bold":
            return (
                f"[bold]{d['bold']}[/bold]"
                if type(d["bold"]) == str
                else f"[bold]{render_element(d['bold'][0])}[/bold]"
            )
        if list(d.keys())[0] == "blockquote":
            return (
                f"[#888888]{d['blockquote']}[/#888888]"
                if type(d["blockquote"]) == str
                else f"[#888888]{render_element(d['blockquote'][0])}[/#888888]"
            )
        if list(d.keys())[0] == "strike":
            return (
                f"[strike]{d['strike']}[/strike]"
                if type(d["strike"]) == str
                else f"[strike]{render_element(d['strike'][0])}[/strike]"
            )
        if list(d.keys())[0] == "break":
            return f"\n"
        if list(d.keys())[0] == "link":
            return f"[link={d['link']['href']}]{d['link']['content']}[/link]"
    raise ValueError(f"Unsupported element type: {type(d)}")


def rgb_to_hex(t: tuple[float, float, float]) -> str:
    """Converts RGB color values to hexadecimal color code.

    Args:
        t (tuple[float, float, float]): A tuple of three float values representing RGB colors.
            Each value should be between 0 and 1.

    Returns:
        str: A string representing the hexadecimal color code.

    Raises:
        ValueError: If the input tuple contains values outside the range [0, 1].
    """
    return f"#{int(t[0]*255):02x}{int(t[1]*255):02x}{int(t[2]*255):02x}"


def fragment_syllables(s: str) -> list[str]:
    """Fragments a string into a list of 3-character substrings.

    Args:
        s (str): A string to be fragmented.

    Returns:
        list[str]: A list of 3-character substrings.

    Raises:
        ValueError: If the input string is empty.
    """
    ss: str = s[1:].replace("-", "")
    return [ss[i : i + 3] for i in range(0, len(ss), 3)]
