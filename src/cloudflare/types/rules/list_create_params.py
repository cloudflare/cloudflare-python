# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ListCreateParams"]


class ListCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    kind: Required[Literal["ip", "redirect", "hostname", "asn"]]
    """The type of the list.

    Each type supports specific list items (IP addresses, ASNs, hostnames or
    redirects).
    """

    name: Required[str]
    """An informative name for the list. Use this name in filter and rule expressions."""

    description: str
    """An informative summary of the list."""
