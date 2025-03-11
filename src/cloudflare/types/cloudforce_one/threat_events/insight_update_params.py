# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["InsightUpdateParams"]


class InsightUpdateParams(TypedDict, total=False):
    account_id: Required[Annotated[float, PropertyInfo(alias="accountId")]]
    """Account ID"""

    event_id: Required[Annotated[str, PropertyInfo(alias="eventId")]]
    """Event UUID"""

    content: Required[str]
