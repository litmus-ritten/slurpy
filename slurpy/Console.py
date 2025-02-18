#!/usr/bin/env python3


__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Provider for rich console"

import logging

from rich import console
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler(markup=True)])
log = logging.getLogger("rich")
console = console.Console()
