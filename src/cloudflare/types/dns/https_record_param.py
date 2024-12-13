# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["HTTPSRecordParam", "Data"]


class Data(TypedDict, total=False):
    priority: float
    """priority."""

    target: str
    """target."""

    value: str
    """value."""


class HTTPSRecordParam(TypedDict, total=False):
    data: Data
    """Components of a HTTPS record."""

    type: Literal["HTTPS"]
    """Record type."""
