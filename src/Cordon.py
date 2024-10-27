#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Tlon Cordon (structure representing banned or allowed ships or ranks in a Group)"

from typing import Set

from Point import Point
from pydantic import BaseModel
from Rank import Rank
from rich.panel import Panel

from rich.text import Text


class Cordon(BaseModel):
    """Tlon group cordon (bans, invites and permissions).

    Attributes:
        banned_ships: Named @ps which are banned.
        banned_ranks: Ranks which are be banned.
        invited_ships: Named @ps which have been invited to a private or secret group (but have not joined?).
        asking_ships: @ps which have asked to enter a private (or secret?) group but have not yet been permitted.
    """

    banned_ships: Set[Point]
    banned_ranks: Set[Rank]
    asking_ships: Set[Point]
    invited_ships: Set[Point]
    open: bool

    def __init__(self, **kwarg):
        super(Cordon, self).__init__(**kwarg)

    @classmethod
    def from_dict(cls, d: dict) -> "Cordon":
        """Create a Cordon instance from a dictionary.

        Args:
            d (dict): A dictionary containing cordon data.

        Returns:
            Cordon: A new Cordon instance.

        Raises:
            ValueError: If the input dictionary is invalid.
        """
        banned_ships = set()
        banned_ranks = set()
        asking_ships = set()
        invited_ships = set()
        open = False

        if "open" in d.keys():
            banned_ships = set(Point(patp=e) for e in d["open"]["ships"])
            banned_ranks = set(Rank.from_str(e) for e in d["open"]["ranks"])
            open = True
        if "shut" in d.keys():
            invited_ships = set(Point(patp=e) for e in d["shut"]["pending"])
            asking_ships = set(Point(patp=e) for e in d["shut"]["ask"])
            open = False
        return Cordon(
            banned_ranks=banned_ranks,
            banned_ships=banned_ships,
            asking_ships=asking_ships,
            invited_ships=invited_ships,
            open=open,
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the Cordon object.

        Returns:
            str: A formatted string containing the Cordon object's attributes.
        """
        return (
            f"Cordon(\n"
            f"  banned_ships: {self.banned_ships},\n"
            f"  banned_ranks: {self.banned_ranks},\n"
            f"  asking_ships: {self.asking_ships},\n"
            f"  invited_ships: {self.invited_ships}\n"
            f"  open: {self.open}\n"
            f")"
        )

    @property
    def pp(self) -> Panel:
        """
        Returns a pretty-printed Panel representation of the Cordon object.

        Returns:
            Panel: A rich Panel summarising the Cordon object's attributes.
        """
        t = Text()
        if self.open:
            t.append(f"Open cordon\n", style="bold green")
            if self.banned_ranks is set() and self.banned_ships is set():
                t.append("\nNo bans\n", style="bold green")
            if self.banned_ships is not set():
                t.append("\nBanned ships:\n", style="bold red")
                for _ in sorted(self.banned_ships):
                    t.append(_.cartouche)
                    t.append("\n")
            if self.banned_ranks is not set():
                t.append("\nBanned ranks:", style="bold red")
                for _ in self.banned_ranks:
                    t.append(f" ")
                    t.append(_.external_name_plural)
                t.append("\n")
        else:
            t.append(f"Closed cordon", style="bold red")
        return Panel(t, expand=False)
