# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ARecordParam"]


class ARecordParam(TypedDict, total=False):
    content: str
    """A valid IPv4 address."""

    type: Literal["A"]
    """Record type."""
