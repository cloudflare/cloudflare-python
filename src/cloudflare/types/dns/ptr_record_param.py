# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PTRRecordParam"]


class PTRRecordParam(TypedDict, total=False):
    content: str
    """Domain name pointing to the address."""

    type: Literal["PTR"]
    """Record type."""
