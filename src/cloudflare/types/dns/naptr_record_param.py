# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NAPTRRecordParam", "Data"]


class Data(TypedDict, total=False):
    flags: str
    """Flags."""

    order: float
    """Order."""

    preference: float
    """Preference."""

    regex: str
    """Regex."""

    replacement: str
    """Replacement."""

    service: str
    """Service."""


class NAPTRRecordParam(TypedDict, total=False):
    data: Data
    """Components of a NAPTR record."""

    type: Literal["NAPTR"]
    """Record type."""
