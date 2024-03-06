# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrangeToOrangeEditParams", "Value"]


class OrangeToOrangeEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Value]
    """
    Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
    on Cloudflare.
    """


class Value(TypedDict, total=False):
    id: Required[Literal["orange_to_orange"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""
