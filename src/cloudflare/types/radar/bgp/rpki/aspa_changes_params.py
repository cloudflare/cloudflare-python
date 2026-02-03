# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ASPAChangesParams"]


class ASPAChangesParams(TypedDict, total=False):
    asn: int
    """Filter changes involving this ASN (as customer or provider)."""

    date_end: Annotated[Union[str, datetime], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive)."""

    date_start: Annotated[Union[str, datetime], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range (inclusive)."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    include_asn_info: Annotated[bool, PropertyInfo(alias="includeAsnInfo")]
    """Include ASN metadata (name, country) in response."""
