#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Tlon Channel Subscriber"

from datetime import datetime
from typing import Any, List

from Point import Point

from pydantic import BaseModel
from util import urbts2datetime


class Subscriber(BaseModel):
    """
    A Tlon Channel Subscriber.

    Attributes:
        point (Point): The user's Point.
        join_datetime (datetime): The datetime when the user joined, in Urbit timestamp format.
        sects (List[Any]): An enumeration of sects.
    """

    point: Point
    join_datetime: datetime
    sects: List[Any]

    def __init__(
        self,
        **kwargs,
    ) -> None:
        """
        Initialize a Subscriber instance.

        Args:
            **kwargs: Keyword arguments to initialize the Subscriber.
        """
        super().__init__(**kwargs)

    @classmethod
    def from_dict(cls, k: str, d: dict) -> "Subscriber":
        """
        Parse a key, value pair representing a Subscriber from a Fleet record.

        Args:
            k (str): The key representing the subscriber's patp.
            d (dict): The dictionary containing subscriber data.

        Returns:
            Subscriber: A new Subscriber instance.
        """
        return Subscriber(point=Point(patp=k), join_datetime=urbts2datetime(d[k]["joined"]), sects=d[k]["sects"])
