# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AuditLogListParams", "Action", "Actor", "Zone"]


class AuditLogListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    id: str
    """Finds a specific log by its ID."""

    action: Action

    actor: Actor

    before: Annotated[Union[Union[str, date], Union[str, datetime]], PropertyInfo(format="iso8601")]
    """Limits the returned results to logs older than the specified date.

    A `full-date` that conforms to RFC3339.
    """

    direction: Literal["desc", "asc"]
    """Changes the direction of the chronological sorting."""

    export: bool
    """Indicates that this request is an export of logs in CSV format."""

    hide_user_logs: bool
    """Indicates whether or not to hide user level audit logs."""

    page: float
    """Defines which page of results to return."""

    per_page: float
    """Sets the number of results to return per page."""

    since: Annotated[Union[Union[str, date], Union[str, datetime]], PropertyInfo(format="iso8601")]
    """Limits the returned results to logs newer than the specified date.

    A `full-date` that conforms to RFC3339.
    """

    zone: Zone


class Action(TypedDict, total=False):
    type: str
    """Filters by the action type."""


class Actor(TypedDict, total=False):
    email: str
    """Filters by the email address of the actor that made the change."""

    ip: str
    """
    Filters by the IP address of the request that made the change by specific IP
    address or valid CIDR Range.
    """


class Zone(TypedDict, total=False):
    name: str
    """Filters by the name of the zone associated to the change."""
