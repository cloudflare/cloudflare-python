# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScanScreenshotParams"]


class ScanScreenshotParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    resolution: Literal["desktop", "mobile", "tablet"]
    """Target device type."""
