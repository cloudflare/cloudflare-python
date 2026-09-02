# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ProtocolListResponse"]


class ProtocolListResponse(BaseModel):
    description: str
    """The full name of the application protocol."""

    name: str
    """The short name of the application protocol."""

    ports: List[int]
    """The available listening ports for the given protocol."""

    transport: str
    """The transport layer protocol used by the application protocol"""
