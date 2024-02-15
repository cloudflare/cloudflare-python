# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomPageCreateParams"]


class CustomPageCreateParams(TypedDict, total=False):
    custom_html: Required[str]
    """Custom page HTML."""

    name: Required[str]
    """Custom page name."""

    type: Required[Literal["identity_denied", "forbidden"]]
    """Custom page type."""

    app_count: int
    """Number of apps the custom page is assigned to."""
