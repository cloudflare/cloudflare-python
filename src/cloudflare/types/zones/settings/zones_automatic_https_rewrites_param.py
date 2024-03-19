# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesAutomaticHTTPSRewritesParam"]


class ZonesAutomaticHTTPSRewritesParam(TypedDict, total=False):
    id: Required[Literal["automatic_https_rewrites"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""
