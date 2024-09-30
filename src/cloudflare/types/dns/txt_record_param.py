# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TXTRecordParam"]


class TXTRecordParam(TypedDict, total=False):
    content: str
    """Text content for the record."""

    type: Literal["TXT"]
    """Record type."""
