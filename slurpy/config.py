#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Configuration constants for slurpy"

from pathlib import Path

import platformdirs

TIMEOUT = 30.0
POLL_RATE = 5.0
DEBUG = True
SCRYJSONHEAD = {"Content-Type": "application/json"}
SSEHEAD = {"Content-Type": "text/event-stream"}
LOGINURL = "~/login"
LARGE_PAGE_SIZE = "1.000.000.000.000"  # Assume that there are less than a trillion messages in a channel.
PAGE_SIZE = "50"  # For chunked scries, read this many posts at a time.
CACHE_DIR = platformdirs.user_cache_dir(appname="urbit-slurpy", ensure_exists=True)
CACHE_PATH = Path(CACHE_DIR, "slurpy_cache.json")
