# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SVCBRecordParam", "Data"]


class Data(TypedDict, total=False):
    priority: float
    """priority."""

    target: str
    """target."""

    value: str
    """value."""


class SVCBRecordParam(TypedDict, total=False):
    data: Data
    """Components of a SVCB record."""

    type: Literal["SVCB"]
    """Record type."""
