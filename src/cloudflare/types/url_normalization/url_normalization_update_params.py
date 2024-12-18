# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["URLNormalizationUpdateParams"]


class URLNormalizationUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """The unique ID of the zone."""

    scope: Required[Literal["incoming", "both"]]
    """The scope of the URL normalization."""

    type: Required[Literal["cloudflare", "rfc3986"]]
    """The type of URL normalization performed by Cloudflare."""
