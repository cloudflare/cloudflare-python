# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DSRecordParam", "Data"]


class Data(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    digest: str
    """Digest."""

    digest_type: float
    """Digest Type."""

    key_tag: float
    """Key Tag."""


class DSRecordParam(TypedDict, total=False):
    data: Data
    """Components of a DS record."""

    type: Literal["DS"]
    """Record type."""
