# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AggregateListParams"]


class AggregateListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    aggregate_by: Required[Annotated[str, PropertyInfo(alias="aggregateBy")]]
    """
    Column(s) to aggregate by - single column or comma-separated list (e.g.,
    'attacker', 'targetIndustry', 'attacker,targetIndustry')
    """

    dataset_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="datasetId")]
    """Dataset ID(s) to filter by.

    Can be a single dataset ID, comma-separated list, or array. If not provided,
    uses default dataset
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """End date for filtering (ISO 8601 format, e.g., '2024-12-31')"""

    group_by_date: Annotated[bool, PropertyInfo(alias="groupByDate")]
    """Whether to group results by date (daily aggregation)"""

    limit: float
    """Maximum number of results to return"""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Start date for filtering (ISO 8601 format, e.g., '2024-01-01')"""
