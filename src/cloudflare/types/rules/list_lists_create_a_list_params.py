# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ListListsCreateAListParams"]


class ListListsCreateAListParams(TypedDict, total=False):
    kind: Required[Literal["ip", "redirect", "hostname", "asn"]]
    """The type of the list.

    Each type supports specific list items (IP addresses, ASNs, hostnames or
    redirects).
    """

    name: Required[str]
    """An informative name for the list. Use this name in filter and rule expressions."""

    description: str
    """An informative summary of the list."""
