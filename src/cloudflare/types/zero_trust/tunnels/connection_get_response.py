# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .client import Client

__all__ = ["ConnectionGetResponse"]

ConnectionGetResponse: TypeAlias = List[Client]
