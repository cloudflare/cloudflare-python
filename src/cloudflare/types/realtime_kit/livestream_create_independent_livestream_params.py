# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LivestreamCreateIndependentLivestreamParams"]


class LivestreamCreateIndependentLivestreamParams(TypedDict, total=False):
    account_id: str
    """The account identifier tag."""

    name: Optional[str]
    """Name of the livestream"""
