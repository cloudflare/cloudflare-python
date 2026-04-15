# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DNSGetParams"]


class DNSGetParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    subdomain: str
    """Domain of your zone."""
