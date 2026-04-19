# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ASPASnapshotParams"]


class ASPASnapshotParams(TypedDict, total=False):
    customer_asn: Annotated[int, PropertyInfo(alias="customerAsn")]
    """Filter by customer ASN (the ASN publishing the ASPA object)."""

    date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters results by the specified datetime (ISO 8601)."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    include_asn_info: Annotated[bool, PropertyInfo(alias="includeAsnInfo")]
    """Include ASN metadata (name, country) in response."""

    provider_asn: Annotated[int, PropertyInfo(alias="providerAsn")]
    """Filter by provider ASN (an authorized upstream provider in ASPA objects)."""
