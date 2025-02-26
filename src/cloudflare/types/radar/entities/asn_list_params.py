# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ASNListParams"]


class ASNListParams(TypedDict, total=False):
    asn: str
    """Comma-separated list of Autonomous System Numbers (ASNs)."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    location: str
    """Location alpha-2 code."""

    offset: int
    """Skips the specified number of objects before fetching the results."""

    order_by: Annotated[Literal["ASN", "POPULATION"], PropertyInfo(alias="orderBy")]
    """Metric to order the ASNs by."""
