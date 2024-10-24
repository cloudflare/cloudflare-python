# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SMIMEARecordParam", "Data"]


class Data(TypedDict, total=False):
    certificate: str
    """Certificate."""

    matching_type: float
    """Matching Type."""

    selector: float
    """Selector."""

    usage: float
    """Usage."""


class SMIMEARecordParam(TypedDict, total=False):
    data: Data
    """Components of a SMIMEA record."""

    type: Literal["SMIMEA"]
    """Record type."""
