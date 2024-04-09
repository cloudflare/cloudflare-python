# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomMetadataParam"]


class CustomMetadataParam(TypedDict, total=False):
    key: str
    """Unique metadata for this hostname."""
