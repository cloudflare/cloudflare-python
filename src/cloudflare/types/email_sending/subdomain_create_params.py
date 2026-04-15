# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubdomainCreateParams"]


class SubdomainCreateParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    name: Required[str]
    """The subdomain name. Must be within the zone."""
