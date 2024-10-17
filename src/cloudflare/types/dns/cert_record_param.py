# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CERTRecordParam", "Data"]


class Data(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    certificate: str
    """Certificate."""

    key_tag: float
    """Key Tag."""

    type: float
    """Type."""


class CERTRecordParam(TypedDict, total=False):
    data: Data
    """Components of a CERT record."""

    type: Literal["CERT"]
    """Record type."""
