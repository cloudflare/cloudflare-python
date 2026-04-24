# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ColoListParams"]


class ColoListParams(TypedDict, total=False):
    account_id: Required[str]

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start time for connection period in ISO (RFC3339 - ISO 8601) format"""

    to: Required[str]
    """End time for connection period in ISO (RFC3339 - ISO 8601) format"""

    sort_by: Annotated[Literal["fleet-status-usage", "application-tests-usage"], PropertyInfo(alias="sortBy")]
    """Type of usage that colos should be sorted by.

    If unspecified, returns all Cloudflare colos sorted alphabetically.
    """
