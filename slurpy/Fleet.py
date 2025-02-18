#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Tlon Channel Fleet (Subscriber list)"

from typing import List

from pydantic import BaseModel

from .Subscriber import Subscriber


class Fleet(BaseModel):
    """A Tlon Fleet, i.e. a enumeration of subscribed users to a Channel.

    Attributes:
        contents (List[Subscriber]): List of subscribers in the fleet.
    """

    contents: List[Subscriber]

    @classmethod
    def from_dict(cls, d: dict) -> "Fleet":
        """Create a Fleet instance from a dictionary.

        Args:
            d (dict): Dictionary containing subscriber information.

        Returns:
            Fleet: A new Fleet instance.
        """
        return Fleet(contents=[Subscriber.from_dict(k=k, d=d) for k in d.keys()])
