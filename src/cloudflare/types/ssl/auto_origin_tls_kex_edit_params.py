# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AutoOriginTLSKexEditParams"]


class AutoOriginTLSKexEditParams(TypedDict, total=False):
    zone_id: Required[str]

    enabled: Required[bool]
    """Controls enablement of Auto-Origin TLS KEX selection for the zone."""
