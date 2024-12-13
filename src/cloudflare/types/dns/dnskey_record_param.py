# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .ttl_param import TTLParam
from .record_tags import RecordTags

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
    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: Data
    """Components of a DNSKEY record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["DNSKEY"]
    """Record type."""
