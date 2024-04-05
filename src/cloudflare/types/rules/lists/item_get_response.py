# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from ..hostname import Hostname
from ..redirect import Redirect

__all__ = ["ItemGetResponse"]

ItemGetResponse = Union[str, Redirect, Hostname, int, None]
