# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["HostnameWeb3HostnameCreateWeb3HostnameParams"]


class HostnameWeb3HostnameCreateWeb3HostnameParams(TypedDict, total=False):
    target: Required[Literal["ethereum", "ipfs", "ipfs_universal_path"]]
    """Target gateway of the hostname."""

    description: str
    """An optional description of the hostname."""

    dnslink: str
    """DNSLink value used if the target is ipfs."""
