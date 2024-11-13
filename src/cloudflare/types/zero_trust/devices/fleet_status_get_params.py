# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FleetStatusGetParams"]


class FleetStatusGetParams(TypedDict, total=False):
    account_tag: Required[Annotated[str, PropertyInfo(alias="accountTag")]]

    since_minutes: Required[float]
    """Number of minutes before current time"""

    colo: str
    """List of data centers to filter results"""

    time_now: str
    """Number of minutes before current time"""
