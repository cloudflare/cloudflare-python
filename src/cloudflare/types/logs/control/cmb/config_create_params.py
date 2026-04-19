# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConfigCreateParams"]


class ConfigCreateParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    allow_out_of_region_access: bool
    """Allow out of region access"""

    regions: str
    """Name of the region."""
