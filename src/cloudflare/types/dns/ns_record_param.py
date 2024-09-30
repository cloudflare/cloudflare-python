# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NSRecordParam"]


class NSRecordParam(TypedDict, total=False):
    content: str
    """A valid name server host name."""

    type: Literal["NS"]
    """Record type."""
