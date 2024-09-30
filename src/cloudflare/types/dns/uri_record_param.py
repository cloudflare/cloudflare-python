# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["URIRecordParam", "Data"]


class Data(TypedDict, total=False):
    target: str
    """The record content."""

    weight: float
    """The record weight."""


class URIRecordParam(TypedDict, total=False):
    data: Data
    """Components of a URI record."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    type: Literal["URI"]
    """Record type."""
