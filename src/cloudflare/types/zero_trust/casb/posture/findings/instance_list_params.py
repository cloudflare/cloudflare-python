# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ......_types import SequenceNotStr
from ......_utils import PropertyInfo

__all__ = ["InstanceListParams"]


class InstanceListParams(TypedDict, total=False):
    account_id: Required[str]

    archived: bool
    """Archived"""

    asset_ids: SequenceNotStr[str]
    """Filter finding instances by an array of asset IDs.

    Supports multiple comma-separated values.
    """

    cursor: str
    """A cursor for pagination.

    Obtained from the `result_info.cursor` field of a previous response.
    """

    direction: Literal["asc", "desc"]
    """Direction to order results."""

    finding_instance_ids: SequenceNotStr[str]
    """Filter finding instances by an array of finding instance IDs.

    Supports multiple comma-separated values.
    """

    max_affliction_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view findings that occurred on or before the affliction date.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    min_affliction_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to view findings that occurred on or after the affliction date.

    Can be a date-time in ISO 8601 format or an epoch timestamp.
    """

    order: Literal["affliction_date", "asset.name", "remediation.status"]
    """
    Which field to use when ordering the Finding's instances. When ordering by
    'remediation.status', only the most recent non-stale remediation job is
    considered. Stale jobs (created before the instance's affliction_date) are
    treated as having no status for ordering purposes.
    """

    page: int
    """A page number within the paginated result set."""

    per_page: int
    """Number of results to return per page."""

    remediation_statuses: List[Literal["none", "pending", "processing", "validating", "completed", "failed"]]
    """Filter finding instances by most recent remediation job status.

    Supports multiple comma-separated values. Use 'none' to filter instances with no
    remediation jobs or instances where the most recent job is stale. Note: Stale
    jobs (created before the instance's affliction_date) are ignored for filtering
    purposes, but are still included in the 'remediations' array with stale=true.
    """

    search: str
    """A search term."""
