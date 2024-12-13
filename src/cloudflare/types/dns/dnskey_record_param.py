# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DNSKEYRecordParam", "Data"]


class Data(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    flags: float
    """Flags."""

    protocol: float
    """Protocol."""

    public_key: str
    """Public Key."""


class DNSKEYRecordParam(TypedDict, total=False):
    data: Data
    """Components of a DNSKEY record."""

    type: Literal["DNSKEY"]
    """Record type."""
