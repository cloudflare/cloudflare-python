# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SRVRecordParam", "Data"]


class Data(TypedDict, total=False):
    port: float
    """The port of the service."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    target: str
    """A valid hostname."""

    weight: float
    """The record weight."""


class SRVRecordParam(TypedDict, total=False):
    data: Data
    """Components of a SRV record."""

    type: Literal["SRV"]
    """Record type."""
