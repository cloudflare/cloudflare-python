# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FallbackOriginUpdateParams"]


class FallbackOriginUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    origin: Required[str]
    """Your origin hostname that requests to your custom hostnames will be sent to."""
