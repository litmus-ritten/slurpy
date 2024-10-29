#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Representation of a running Urbit ship, used to manage an authenticated session"

from config import TIMEOUT
from pydantic import BaseModel, BeforeValidator
from pydantic_core import Url
from SlurpyExceptions import InsecureError
from typing_extensions import Annotated
from validators import valid_code


class Pier(BaseModel):
    """
    Representation of a running Urbit.
    """

    host: Url
    code: Annotated[str, BeforeValidator(valid_code)]
    insecure: bool = False

    def __init__(self, **kwargs):
        super(Pier, self).__init__(**kwargs)


def main():
    test = Pier(host="http://localhost:8080", code="sampel-palnet-sampel-palnet", insecure=True)
    if "https" not in str(test.host.path):
        if test.insecure:
            print("Operating in insecure mode. Be careful.")
        else:
            raise InsecureError("Connection is not secure (HTTP) but 'insecure' mode was not enabled.")


if __name__ == "__main__":
    main()
