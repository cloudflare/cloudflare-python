# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MonitorGroupCreateParams", "Member"]


class MonitorGroupCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    id: Required[str]
    """
    The ID of the Monitor Group to use for checking the health of origins within
    this pool.
    """

    description: Required[str]
    """A short description of the monitor group"""

    members: Required[Iterable[Member]]
    """List of monitors in this group"""


class Member(TypedDict, total=False):
    enabled: Required[bool]
    """Whether this monitor is enabled in the group"""

    monitor_id: Required[str]
    """
    The ID of the Monitor to use for checking the health of origins within this
    pool.
    """

    monitoring_only: Required[bool]
    """Whether this monitor is used for monitoring only (does not affect pool health)"""

    must_be_healthy: Required[bool]
    """Whether this monitor must be healthy for the pool to be considered healthy"""
