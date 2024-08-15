# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FleetStatusOverTimeParams"]


class FleetStatusOverTimeParams(TypedDict, total=False):
    account_id: Required[str]

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Time range beginning in ISO format"""

    to: Required[str]
    """Time range end in ISO format"""

    colo: str
    """Cloudflare colo"""

    device_id: str
    """Device-specific ID, given as UUID v4"""
