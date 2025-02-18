#!/usr/bin/env python3

import datetime
from typing import List

from pydantic import BaseModel
from rich import text

from .Point import Point

from .util import render_element, tlonts2dt


class Post(BaseModel):

    index: int
    revision: int
    author: Point
    sent: datetime.datetime
    content: List[dict] | dict
    n_replies: int
    last_reply_time: datetime.datetime | None

    def __hash__(self):
        return self.index

    def __lt__(self, other):
        return self.index < other.index

    def __gt__(self, other):
        return self.index > other.index

    def __leq__(self, other):
        return self.index <= other.index

    def __geq__(self, other):
        return self.index >= other.index

    def __eq__(self, other):
        return self.index == other.index

    @classmethod
    def from_dict(cls, v: dict):
        """
        We don't need the key as this information is stored in the seal.
        """
        meta = v["seal"]["meta"]
        index = int(v["seal"]["id"])
        revision = int(v["revision"])
        # Essay
        author = Point(patp=v["essay"]["author"])
        sent = tlonts2dt(v["essay"]["sent"])
        content = v["essay"]["content"]
        n_replies = int(meta["replyCount"])
        if n_replies > 0:
            last_reply_time = tlonts2dt(meta["lastReply"])
        else:
            last_reply_time = None
        return Post(
            index=index,
            revision=revision,
            author=author,
            sent=sent,
            content=content,
            n_replies=n_replies,
            last_reply_time=last_reply_time,
        )

    @property
    def tile(self):
        t = text.Text()
        t.append(str(self.sent))
        t.append(" ")
        t.append(self.author.cartouche)
        t.append(" ")
        for d in self.content:
            for k, v in d.items():
                for j in v:
                    t.append(text.Text.from_markup("".join(list(render_element(_) for _ in j))))
        return t


class Posts(BaseModel):
    """docstring for Posts"""

    contents: List[Post]

    def __init__(self, **kwargs):
        super(Posts, self).__init__(**kwargs)

    @classmethod
    def from_dict(cls, d: dict):
        contents = [Post.from_dict(v=v) for _, v in d.items() if v is not None]
        return Posts(contents=contents)


class Chat(BaseModel):
    """docstring for Chat"""

    posts: Posts
    total_records: int
    index_newer: int | None
    index_older: int | None

    @classmethod
    def from_dict(cls, d: dict):
        posts = Posts.from_dict(d["posts"])
        total_records = d["total"]
        index_newer = d["newer"]  # Index of record newer than newest in view
        index_older = d["older"]  # Index of record older than oldest in view
        return Chat(posts=posts, total_records=total_records, index_newer=index_newer, index_older=index_older)

    @classmethod
    def from_empty(cls):
        return Chat(posts=Posts.from_dict(dict()), total_records=0, index_newer=0, index_older=0)
