# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FleetStatusOverTimeParams"]


class FleetStatusOverTimeParams(TypedDict, total=False):
    account_id: Required[str]
    """Unique identifier linked to an account."""

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start of the time range to query.

    Timestamp can be provided in ISO 8601 datetime format or milliseconds since
    epoch.
    """

    to: Required[str]
    """End of the time range to query.

    Timestamp can be provided in ISO 8601 datetime format or milliseconds since
    epoch.
    """

    colo: str
    """Cloudflare colo airport code."""

    device_id: str
    """Device-specific ID, given as UUID."""
