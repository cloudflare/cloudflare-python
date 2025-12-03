# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PrefixCreateParams"]


class PrefixCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of a Cloudflare account."""

    asn: Required[int]
    """Autonomous System Number (ASN) the prefix will be advertised under."""

    cidr: Required[str]
    """IP Prefix in Classless Inter-Domain Routing format."""

    delegate_loa_creation: bool
    """
    Whether Cloudflare is allowed to generate the LOA document on behalf of the
    prefix owner.
    """

    description: str
    """Description of the prefix."""

    loa_document_id: Optional[str]
    """Identifier for the uploaded LOA document."""
