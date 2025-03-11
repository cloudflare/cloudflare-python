# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["UserAgentDirectiveParams"]


class UserAgentDirectiveParams(TypedDict, total=False):
    date: Annotated[List[Union[str, datetime.date]], PropertyInfo(format="iso8601")]
    """Array of dates to filter the results."""

    directive: Literal["ALLOW", "DISALLOW"]
    """Filters results by robots.txt directive."""

    domain_category: Annotated[List[str], PropertyInfo(alias="domainCategory")]
    """Filters results by domain category."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    name: List[str]
    """Array of names used to label the series in the response."""

    user_agent_category: Annotated[Literal["AI"], PropertyInfo(alias="userAgentCategory")]
    """Filters results by user agent category."""
