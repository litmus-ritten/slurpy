#!/usr/bin/env python3

__author__ = ["litmus-ritten"]
__license__ = "MIT"
__description__ = "Custom exceptions for slurpy"


class InvalidRankError(Exception):
    """
    Exception raised when the Rank of a Point is invalid.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str):
        super(InvalidRankError, self).__init__()
        self._message = message

    @property
    def message(self) -> str:
        """str: The error message."""
        return self._message

    def __str__(self) -> str:
        return f"{self.message}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message='{self.message}')"


class InvalidPatpError(Exception):
    """
    Exception raised when the Patp of a Point is invalid.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str):
        super(InvalidPatpError, self).__init__()
        self._message = message

    @property
    def message(self) -> str:
        """str: The error message."""
        return self._message

    def __str__(self) -> str:
        return f"{self.message}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message='{self.message}')"


class UnknownChannelType(Exception):
    """
    Exception raised when the type of a Channel is invalid.

    Attributes:
        message (str): The error message.
    """

    def __init__(self, message: str):
        super(UnknownChannelType, self).__init__()
        self._message = message

    @property
    def message(self) -> str:
        """str: The error message."""
        return self._message

    def __str__(self) -> str:
        return f"{self.message}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message='{self.message}')"
