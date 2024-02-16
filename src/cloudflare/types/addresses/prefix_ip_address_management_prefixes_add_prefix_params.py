# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PrefixIPAddressManagementPrefixesAddPrefixParams"]


class PrefixIPAddressManagementPrefixesAddPrefixParams(TypedDict, total=False):
    asn: Required[Optional[int]]
    """Autonomous System Number (ASN) the prefix will be advertised under."""

    cidr: Required[str]
    """IP Prefix in Classless Inter-Domain Routing format."""

    loa_document_id: Required[Optional[str]]
    """Identifier for the uploaded LOA document."""
