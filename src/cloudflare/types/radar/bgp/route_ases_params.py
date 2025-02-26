# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RouteAsesParams"]


class RouteAsesParams(TypedDict, total=False):
    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    location: str
    """Location alpha-2 code."""

    sort_by: Annotated[
        Literal["cone", "pfxs", "ipv4", "ipv6", "rpki_valid", "rpki_invalid", "rpki_unknown"],
        PropertyInfo(alias="sortBy"),
    ]
    """Sorts results by the specified field."""

    sort_order: Annotated[Literal["ASC", "DESC"], PropertyInfo(alias="sortOrder")]
    """Sort order."""
