#!/usr/bin/env python3

from types import NoneType
from typing import Optional

import aiohttp
from aiohttp import CookieJar


class Client:
    """A singleton HTTP client session manager.

    This class manages a single aiohttp ClientSession instance and its associated cookie jar.

    Attributes:
        _instance (Optional[aiohttp.ClientSession]): The singleton client session instance.
        _cookiejar (CookieJar): Cookie storage for the session.
    """

    _instance: Optional[aiohttp.ClientSession] = None
    _cookiejar: CookieJar

    @classmethod
    async def get_session(cls, cookies: dict = {}) -> aiohttp.ClientSession:
        """Creates or returns an existing aiohttp ClientSession instance.

        Args:
            cookies (dict, optional): Dictionary of cookies to initialize or update the session with.
                Defaults to empty dict.

        Returns:
            aiohttp.ClientSession: The singleton client session instance.
        """
        if isinstance(cls._instance, NoneType) or cls._instance.closed:
            cls._cookiejar = CookieJar()
            cls._cookiejar.update_cookies(cookies=cookies)
            cls._instance = aiohttp.ClientSession(cookie_jar=cls._cookiejar)
        return cls._instance

    @classmethod
    async def close(cls):
        """Closes the current client session if it exists and is open.

        This method should be called when the session is no longer needed to properly
        clean up resources.
        """
        if not isinstance(cls._instance, NoneType) and not cls._instance.closed:
            await cls._instance.close()
            cls._instance = None
            del cls._cookiejar
