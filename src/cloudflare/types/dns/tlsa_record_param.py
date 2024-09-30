# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TLSARecordParam", "Data"]


class Data(TypedDict, total=False):
    certificate: str
    """certificate."""

    matching_type: float
    """Matching Type."""

    selector: float
    """Selector."""

    usage: float
    """Usage."""


class TLSARecordParam(TypedDict, total=False):
    data: Data
    """Components of a TLSA record."""

    type: Literal["TLSA"]
    """Record type."""
