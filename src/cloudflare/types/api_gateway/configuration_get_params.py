# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConfigurationGetParams"]


class ConfigurationGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    normalize: bool
    """Ensures that the configuration is written or retrieved in normalized fashion"""
