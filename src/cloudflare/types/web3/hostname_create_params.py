# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["HostnameCreateParams"]


class HostnameCreateParams(TypedDict, total=False):
    target: Required[Literal["ethereum", "ipfs", "ipfs_universal_path"]]
    """Target gateway of the hostname."""

    description: str
    """An optional description of the hostname."""

    dnslink: str
    """DNSLink value used if the target is ipfs."""
