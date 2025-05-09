# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DeviceListParams", "LastSeenUser"]


class DeviceListParams(TypedDict, total=False):
    account_id: Required[str]

    id: List[str]
    """Filter by a one or more device IDs."""

    active_registrations: Literal["include", "only", "exclude"]
    """Include or exclude devices with active registrations.

    The default is "only" - return only devices with active registrations.
    """

    cursor: str
    """
    Opaque token indicating the starting position when requesting the next set of
    records. A cursor value can be obtained from the result_info.cursor field in the
    response.
    """

    include: str

    last_seen_user: LastSeenUser

    per_page: int
    """The maximum number of devices to return in a single response."""

    search: str
    """Search by device details."""

    seen_after: str
    """
    Filters by the last_seen timestamp - returns only devices last seen after this
    timestamp.
    """

    seen_before: str
    """
    Filter by the last_seen timestamp - returns only devices last seen before this
    timestamp.
    """

    sort_by: Literal[
        "name", "id", "client_version", "last_seen_user.email", "last_seen_at", "active_registrations", "created_at"
    ]
    """The device field to order results by."""

    sort_order: Literal["asc", "desc"]
    """Sort direction."""


class LastSeenUser(TypedDict, total=False):
    email: str
    """Filter by the last seen user's email."""
