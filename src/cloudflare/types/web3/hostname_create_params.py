# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["HostnameCreateParams"]


class HostnameCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Specify the identifier of the hostname."""

    name: Required[str]
    """Specify the hostname that points to the target gateway via CNAME."""

    target: Required[Literal["ethereum", "ipfs", "ipfs_universal_path"]]
    """Specify the target gateway of the hostname."""

    description: str
    """Specify an optional description of the hostname."""

    dnslink: str
    """Specify the DNSLink value used if the target is ipfs."""
