#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Tlon Cabal (logical grouping of users in a Group)"

from typing import Any

from pydantic import BaseModel
from pydantic_core import Url


class Cabal(BaseModel):
    """Tlon group cabal (logical grouping of users)

    Attributes:
        name (str): The internal name of the cabal.
        image (Optional[Url]): The image URL of the cabal, if any (this doesn't appear to be used at the moment).
        title (str): The external title of the cabal.
        cover (Optional[Url]): The cover image URL of the cabal, if any (this doesn't appear to be used at the moment).
        description (str): The description of the cabal.
    """

    name: str
    image: Url | None
    title: str
    cover: Url | None
    description: str

    def __init__(self, **kwargs: Any) -> None:
        """Initialize a Cabal instance.

        Args:
            **kwargs: Keyword arguments to initialize the Cabal attributes.
        """
        super().__init__(**kwargs)

    @classmethod
    def from_dict(cls, k: str, d: dict[str, Any]) -> "Cabal":
        """Create a Cabal instance from a dictionary.

        Args:
            k (str): The key representing the cabal name.
            d (Dict[str, Any]): The dictionary containing cabal data.

        Returns:
            Cabal: A new Cabal instance created from the provided data.
        """
        name = k
        meta = d[k]["meta"]
        title = meta["title"]
        description = meta["description"]
        image = Url(meta["image"]) if meta["image"] != "" else None
        cover = Url(meta["cover"]) if meta["cover"] != "" else None

        return Cabal(name=name, image=image, title=title, cover=cover, description=description)
