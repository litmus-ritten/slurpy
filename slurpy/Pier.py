#!/usr/bin/env python3


__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Representation of a running Urbit ship, used to manage an authenticated session"

import datetime
import gc
import re
from asyncio import sleep
from os import environ
from typing import Dict, Optional, Union

import aiohttp

import requests
from pydantic import BaseModel, BeforeValidator, computed_field, ConfigDict, Field, SecretStr
from pydantic_core import Url

from rich import print
from typing_extensions import Annotated

from .Client import Client

from .config import CACHE_PATH, LOGINURL, SCRYJSONHEAD, TIMEOUT
from .Console import log
from .constants import LOGIN_POINT_SHAPE, SLURPY_ISSUES_ADDR
from .Group import Group
from .Point import Point

from .SlurpyExceptions import InsecureError, LoginError
from .validators import valid_code


class Pier(BaseModel):
    """
    Representation of a running Urbit.
    """

    _client: aiohttp.ClientSession
    cookie: Optional[SecretStr | None] = Field(default=None, exclude=True)
    groups: Optional[Dict[str, Group]] = {}
    groups_last_updated: Optional[datetime.datetime] = datetime.datetime.fromisoformat("1970-01-01")
    host: Url
    code: Optional[Annotated[str, BeforeValidator(valid_code)] | None] = Field(default=None, exclude=True)
    insecure: bool = False
    timeout: aiohttp.ClientTimeout = Field(aiohttp.ClientTimeout(TIMEOUT), exclude=True)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    async def connect(self):
        self._block_insecure()
        try:
            async with self._client.post(
                url=self.login_url.unicode_string(),
                data={"password": self.code},
                timeout=self.timeout,
            ) as res:
                if res.status != requests.codes.no_content:  # Expected for successful authentication
                    raise LoginError(f"Could not log in to {self.host}: {res.status}")
        except Exception as _:
            raise (_)
        self.cookie = SecretStr(res.headers["set-cookie"])
        self._client = await Client.get_session(cookies=self.cookie_dict)
        self._hostpoint = await self.get_hostpoint()
        # await self.update_groups()

    def _block_insecure(self) -> None:
        """
        Block insecure connections if 'insecure' flag is not set.

        This method checks if the connection is using HTTPS. If not, it either
        raises an exception or prints a warning based on the 'insecure' flag.

        Raises:
            InsecureError: If the connection is not secure (HTTP) and 'insecure'
                mode is not enabled.

        Returns:
            None
        """
        if "https" not in str(self.host.path):
            if self.insecure:
                log.warning("Operating in insecure mode by request. Be careful.")
            else:
                raise InsecureError("Connection is not secure (HTTP) but 'insecure' mode was not enabled.")

    @computed_field
    @property
    def login_url(self) -> Url:
        """
        Get the URL for the login page of an Urbit Pier.

        Returns:
            Url: The login URL for the Urbit Pier.
        """
        return Url(f"{self.host}{LOGINURL}")

    async def get_hostpoint(self) -> Point:
        """
        Get the Azimuth Point associated with a running Pier.

        The Point is extracted from the login page.

        Returns:
            Point: The Azimuth Point associated with the Pier.

        Raises:
            requests.RequestException: If there's an error fetching the login page.
            IndexError: If the Point cannot be extracted from the login page.
        """
        try:
            log.info("Checking host")
            async with self._client.get(
                url=self.login_url.unicode_string(),
                timeout=self.timeout,
            ) as peek:
                text = await peek.text()
                m = re.findall(LOGIN_POINT_SHAPE, text)
                log.info("OK")
        except requests.RequestException as _:
            raise LoginError(f"Could not access {self.login_url}: {_}")
        except IndexError:
            raise LoginError(f"Could not find @p on login page. Please file a GitHub issue at {SLURPY_ISSUES_ADDR}.")
        return Point(patp=m[0])

    @property
    def logged_in(self) -> bool:
        """Returns whether the client is logged in.

        Returns:
            bool: True if client has a valid cookie, False otherwise.
        """
        return self.cookie != None

    @property
    def cookie_dict(self) -> Union[dict, None]:
        """Returns the cookie as a dictionary.

        Returns:
            Union[dict, None]: Dictionary containing cookie key-value pair,
                or None if no cookie is set.
        """
        if self.cookie is None:
            return None
        else:
            cookie_k, cookie_v = self.cookie.get_secret_value().split(";")[0].split("=")
            return {cookie_k: cookie_v}

    async def update_groups(self) -> Dict[str, Group]:
        """Updates all groups by calling update_groups_pattern with no pattern.

        Returns:
            Dict[str, Group]: Dictionary mapping group names to Group objects.
        """
        return await self.update_groups_pattern(pattern=None)

    async def update_groups_pattern(self, pattern: Union[str, None]) -> Dict[str, Group]:
        """Updates the groups dictionary by fetching from the scry endpoint and filtering by pattern.

        Args:
            pattern: A regex pattern string to filter group names, or None to include all groups.

        Returns:
            Dict[str, Group]: A dictionary mapping group names to Group objects that match the pattern.

        Raises:
            aiohttp.ClientError: If there is an error fetching the groups data.
            re.error: If the provided pattern is an invalid regex pattern.
        """
        import re

        from .Group import Group

        scrypath = f"{self.host}~/scry/groups/groups/v1.json"
        log.info(f"Scrying groups")
        async with self._client.get(url=scrypath, headers=SCRYJSONHEAD) as scry:
            res = await scry.json()

        if pattern:
            groups = {
                k: await Group.from_key(k=k, d=res, pier_host=self.host)
                for k, _ in res.items()
                if bool(re.search(pattern=pattern, string=k))
            }
        else:
            groups = {k: await Group.from_key(k=k, d=res, pier_host=self.host) for k, _ in res.items()}
        log.info(f"Got {len(groups)} groups")

        self.groups = groups
        self.groups_last_updated = datetime.datetime.now()

    @property
    def groups_recency(self) -> datetime.timedelta:
        """Calculates the time elapsed since groups were last updated.

        Returns:
            datetime.timedelta: The duration since the last groups update.
        """
        return datetime.datetime.now() - self.groups_last_updated

    def attach_client(self, client, code: str) -> None:
        """Attaches a client and authentication code to the Pier instance.

        Args:
            client: The client instance to attach.
            code (str): The authentication code to use.
        """
        self._client = client
        self.code = code

    @classmethod
    def reacquire(cls, json_data: str, args) -> "Pier":
        """Reacquires a Pier instance from JSON data.

        Args:
            json_data (str): JSON string containing serialized Pier data.
            args: Arguments object containing optional host override.

        Returns:
            Pier: A new Pier instance populated with the provided data.

        Note:
            If args.host is provided and differs from the cached host,
            the specified host will be used instead of the cached one.
        """
        p = Pier.model_validate_json(json_data=json_data)
        if args.host is not None and Url(args.host) != p.host:
            log.warning(f"Specified host {Url(args.host)} is distinct from cached host {p.host}. Using specified host.")
            p.host = args.host
        return p


async def main():
    import argparse

    parser = argparse.ArgumentParser("Demonstration: pull user list for named Group")
    parser.add_argument("-u", "--urbit_host", type=str, help="Hostname:port of running ship")
    args = parser.parse_args()

    log.info(f"Cache dir: {CACHE_PATH}")
    ourclient = await Client.get_session()
    async with ourclient as client:
        from pathlib import Path

        if Path.exists(CACHE_PATH):
            log.info("Loading cached data, please wait...")
            with open(CACHE_PATH, "r") as f:
                our_pier = Pier.model_validate_json(json_data=f.read())
                log.info("Attaching HTTP client to loaded pier")
                our_pier.attach_client(client=client, code=str(environ.get("URBIT_KEY")))
                log.info("Reconnecting to pier")
                await our_pier.connect()
                host = await our_pier.get_hostpoint()
                log.info(f"Reacquired connection to {host}")
                for k, v in enumerate(our_pier.groups.items()):
                    g = v[1]
                    await g.update()
                    # print("")
                    # print(g.tile)
                    # for c in g.channels.items():
                    #    print(c[1].tile)
                while True:
                    for k, v in enumerate(our_pier.groups.items()):
                        g = v[1]
                        await g.update(hush=True, echo_messages=True)
                    await sleep(5.0)

        else:
            log.info("No cached data found: pulling Groups data")
            our_pier = Pier(host=args.urbit_host, insecure=True)
            our_pier.attach_client(client=client, code=str(environ.get("URBIT_KEY")))
            await our_pier.connect()
            host = await our_pier.get_hostpoint()
            print(host)
            await our_pier.update_groups()
            for g in our_pier.groups.values():
                print(g.tile)

        import os

        with open(CACHE_PATH, "w") as f:
            f.write(our_pier.model_dump_json(exclude_unset=True, exclude_defaults=True))

        jsons = [Path(e) for e in os.listdir("./") if "json" in e]

        # for e in jsons:
        #    t = open(e, "r").read()
        #    our_pier.groups[e] = Group.model_validate_json(str(t))
        # for g in our_pier.groups.values():
        #    for c in g.channels.values():
        #        print(c)
        #        await c.update_channel()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
