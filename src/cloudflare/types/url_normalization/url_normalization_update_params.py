# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["URLNormalizationUpdateParams"]


class URLNormalizationUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    scope: str
    """The scope of the URL normalization."""

    type: str
    """The type of URL normalization performed by Cloudflare."""
