# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CNAMERecordParam"]


class CNAMERecordParam(TypedDict, total=False):
    content: str
    """A valid hostname. Must not match the record's name."""

    type: Literal["CNAME"]
    """Record type."""
