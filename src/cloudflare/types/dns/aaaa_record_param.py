# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AAAARecordParam"]


class AAAARecordParam(TypedDict, total=False):
    content: str
    """A valid IPv6 address."""

    type: Literal["AAAA"]
    """Record type."""
