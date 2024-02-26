# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConfigCreateParams"]


class ConfigCreateParams(TypedDict, total=False):
    regions: str
    """Comma-separated list of regions."""
