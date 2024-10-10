# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CAARecordParam", "Data"]


class Data(TypedDict, total=False):
    flags: float
    """Flags for the CAA record."""

    tag: str
    """Name of the property controlled by this record (e.g.: issue, issuewild, iodef)."""

    value: str
    """Value of the record. This field's semantics depend on the chosen tag."""


class CAARecordParam(TypedDict, total=False):
    data: Data
    """Components of a CAA record."""

    type: Literal["CAA"]
    """Record type."""
