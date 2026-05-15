# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AISecurityUpdateParams"]


class AISecurityUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines the zone."""

    enabled: bool
    """Whether AI Security for Apps is enabled on the zone."""
