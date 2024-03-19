# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .zones_orange_to_orange_param import ZonesOrangeToOrangeParam

__all__ = ["OrangeToOrangeEditParams"]


class OrangeToOrangeEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[ZonesOrangeToOrangeParam]
    """
    Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
    on Cloudflare.
    """
