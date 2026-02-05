# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["RegistrationListParams", "Device", "User"]


class RegistrationListParams(TypedDict, total=False):
    account_id: Required[str]

    id: SequenceNotStr[str]
    """Filter by registration ID."""

    cursor: str
    """
    Opaque token indicating the starting position when requesting the next set of
    records. A cursor value can be obtained from the result_info.cursor field in the
    response.
    """

    device: Device

    include: str
    """
    Comma-separated list of additional information that should be included in the
    registration response. Supported values are: "policy".
    """

    per_page: int
    """The maximum number of devices to return in a single response."""

    search: str
    """Filter by registration details."""

    seen_after: str
    """
    Filter by the last_seen timestamp - returns only registrations last seen after
    this timestamp.
    """

    seen_before: str
    """
    Filter by the last_seen timestamp - returns only registrations last seen before
    this timestamp.
    """

    sort_by: Literal["id", "user.name", "user.email", "last_seen_at", "created_at"]
    """The registration field to order results by."""

    sort_order: Literal["asc", "desc"]
    """Sort direction."""

    status: Literal["active", "all", "revoked"]
    """Filter by registration status. Defaults to 'active'."""

    user: User


class Device(TypedDict, total=False):
    id: str
    """Filter by WARP device ID."""


class User(TypedDict, total=False):
    id: SequenceNotStr[str]
    """Filter by user ID."""
