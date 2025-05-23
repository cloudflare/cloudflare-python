# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["WARPChangeEventGetParams"]


class WARPChangeEventGetParams(TypedDict, total=False):
    account_id: Required[str]

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start time for the query in ISO (RFC3339 - ISO 8601) format"""

    page: Required[float]
    """Page number of paginated results"""

    per_page: Required[float]
    """Number of items per page"""

    to: Required[str]
    """End time for the query in ISO (RFC3339 - ISO 8601) format"""

    account_name: str
    """Filter events by account name."""

    config_name: str
    """Filter events by WARP configuration name changed from or to.

    Applicable to type='config' events only.
    """

    sort_order: Literal["ASC", "DESC"]
    """Sort response by event timestamp."""

    toggle: Literal["on", "off"]
    """Filter events by type toggle value. Applicable to type='toggle' events only."""

    type: Literal["config", "toggle"]
    """Filter events by type 'config' or 'toggle'"""
