# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DNSParam"]


class DNSParam(TypedDict, total=False):
    name: str
    """The name of the DNS record associated with the application."""

    type: Literal["CNAME", "ADDRESS"]
    """The type of DNS record associated with the application."""
