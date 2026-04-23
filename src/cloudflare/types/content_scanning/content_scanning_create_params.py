# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContentScanningCreateParams"]


class ContentScanningCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    value: Required[Literal["enabled", "disabled"]]
    """The status value for Content Scanning."""
