#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Tlon Post (any authored rich text elememt)"

import datetime

from Point import Point
from pydantic import BaseModel

from pydantic_core import Url
from util import tlonts2dt


class Post(BaseModel):
    """
    Representation of a any Tlon rich text post, i.e. a Chat message, Heap post, or Diary post.

    Attributes:
        index (int): The unique identifier of the post.
        author (Point): The author of the post.
        sent (datetime.datetime): The timestamp when the post was sent.
        title (str): The title of the post.
        image (Url | None): The URL of the associated image, if any.
        content (list): The content of the post.
    """

    index: int
    author: Point
    sent: datetime.datetime
    title: str
    image: Url | None
    content: list

    def __init__(self, **kwargs) -> None:
        """
        Initialize a Post instance.

        Args:
            **kwargs: Keyword arguments to initialize the Post attributes.
        """
        super(Post, self).__init__(**kwargs)

    @classmethod
    def from_dict(cls, d: dict) -> "Post":
        """
        Create a Post instance from a dictionary.

        Args:
            d (dict): A dictionary containing post data.

        Returns:
            Post: A new Post instance created from the dictionary data.
        """
        index = int(d["seal"]["id"])
        essay = d["essay"]
        author = Point(patp=essay["author"])
        sent = tlonts2dt(essay["sent"])
        title = essay["kind-data"]["diary"]["title"]
        image = Url(essay["kind-data"]["diary"]["image"]) if essay["kind-data"]["diary"]["image"] != "" else None
        content = essay["content"]
        return Post(index=index, author=author, sent=sent, title=title, image=image, content=content)

    def __hash__(self) -> int:
        """
        Compute the hash value for the Post instance.

        Returns:
            int: The hash value based on the Post's index.
        """
        return self.index

    def __lt__(self, other: "Post") -> bool:
        """
        Compare if this Post is less than another Post.

        Args:
            other (Post): Another Post instance to compare with.

        Returns:
            bool: True if this Post's index is less than the other Post's index, False otherwise.
        """
        return self.index < other.index

    def __gt__(self, other: "Post") -> bool:
        """
        Compare if this Post is greater than another Post.

        Args:
            other (Post): Another Post instance to compare with.

        Returns:
            bool: True if this Post's index is greater than the other Post's index, False otherwise.
        """
        return self.index > other.index

    def __le__(self, other: "Post") -> bool:
        """
        Compare if this Post is less than or equal to another Post.

        Args:
            other (Post): Another Post instance to compare with.

        Returns:
            bool: True if this Post's index is less than or equal to the other Post's index, False otherwise.
        """
        return self.index <= other.index

    def __ge__(self, other: "Post") -> bool:
        """
        Compare if this Post is greater than or equal to another Post.

        Args:
            other (Post): Another Post instance to compare with.

        Returns:
            bool: True if this Post's index is greater than or equal to the other Post's index, False otherwise.
        """
        return self.index >= other.index
