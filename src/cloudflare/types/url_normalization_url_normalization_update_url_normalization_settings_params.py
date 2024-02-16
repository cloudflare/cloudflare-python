# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["URLNormalizationURLNormalizationUpdateURLNormalizationSettingsParams"]


class URLNormalizationURLNormalizationUpdateURLNormalizationSettingsParams(TypedDict, total=False):
    scope: str
    """The scope of the URL normalization."""

    type: str
    """The type of URL normalization performed by Cloudflare."""
