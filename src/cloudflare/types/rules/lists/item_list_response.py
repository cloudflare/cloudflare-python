# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from ..hostname import Hostname
from ..redirect import Redirect

__all__ = ["ItemListResponse"]

ItemListResponse: TypeAlias = Union[str, Redirect, Hostname, int]
