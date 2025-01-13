# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["TargetListParams"]


class TargetListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Date and time at which the target was created after (inclusive)"""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Date and time at which the target was created before (inclusive)"""

    direction: Literal["asc", "desc"]
    """The sorting direction."""

    hostname: Optional[str]
    """Hostname of a target"""

    hostname_contains: Optional[str]
    """Partial match to the hostname of a target"""

    ip_v4: Optional[str]
    """IPv4 address of the target"""

    ip_v6: Optional[str]
    """IPv6 address of the target"""

    ips: List[str]
    """Filters for targets that have any of the following IP addresses.

    Specify `ips` multiple times in query parameter to build list of candidates.
    """

    modified_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Date and time at which the target was modified after (inclusive)"""

    modified_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Date and time at which the target was modified before (inclusive)"""

    order: Literal["hostname", "created_at"]
    """The field to sort by."""

    page: int
    """Current page in the response"""

    per_page: int
    """Max amount of entries returned per page"""

    virtual_network_id: Optional[str]
    """Private virtual network identifier of the target"""
