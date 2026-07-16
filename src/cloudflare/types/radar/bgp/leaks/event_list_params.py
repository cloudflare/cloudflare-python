# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    date_end: Annotated[Union[str, datetime], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateStart`.
    """

    date_range: Annotated[str, PropertyInfo(alias="dateRange")]
    """Filters results by a relative date range ending at the current time.

    Use `<n>d` for days (up to `364d`) or `<n>w` for weeks (up to `52w`), e.g. `7d`.
    Append `control` to request the equivalent previous period for comparison: the
    comparison window is shifted back by the current window's length rounded up to a
    whole number of weeks, so it keeps the same weekday alignment and does not
    overlap the current window (e.g. `3dcontrol` covers days -10 to -7, `7dcontrol`
    covers days -14 to -7, `28dcontrol` covers days -56 to -28, and `10dcontrol`
    covers days -24 to -14). Mutually exclusive with `dateStart`/`dateEnd`.
    """

    date_start: Annotated[Union[str, datetime], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateEnd`.
    """

    event_id: Annotated[int, PropertyInfo(alias="eventId")]
    """The unique identifier of a event."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    involved_asn: Annotated[int, PropertyInfo(alias="involvedAsn")]
    """ASN that is causing or affected by a route leak event."""

    involved_country: Annotated[str, PropertyInfo(alias="involvedCountry")]
    """Country code of a involved ASN in a route leak event."""

    leak_asn: Annotated[int, PropertyInfo(alias="leakAsn")]
    """The leaking AS of a route leak event."""

    page: int
    """Current page number, starting from 1."""

    per_page: int
    """Number of entries per page."""

    sort_by: Annotated[Literal["ID", "LEAKS", "PEERS", "PREFIXES", "ORIGINS", "TIME"], PropertyInfo(alias="sortBy")]
    """Sorts results by the specified field."""

    sort_order: Annotated[Literal["ASC", "DESC"], PropertyInfo(alias="sortOrder")]
    """Sort order."""
