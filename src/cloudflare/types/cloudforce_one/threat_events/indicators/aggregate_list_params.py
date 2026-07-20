# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["AggregateListParams"]


class AggregateListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    aggregate_by: Required[Annotated[str, PropertyInfo(alias="aggregateBy")]]
    """
    Column(s) to aggregate by - single column or comma-separated list (e.g.,
    'indicatorType', 'value', 'indicatorType,value')
    """

    created_after: Annotated[str, PropertyInfo(alias="createdAfter")]
    """Filter indicators created after this date (ISO 8601 format, e.g., '2024-01-01')"""

    created_before: Annotated[str, PropertyInfo(alias="createdBefore")]
    """
    Filter indicators created before this date (ISO 8601 format, e.g., '2024-12-31')
    """

    dataset_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="datasetIds")]
    """Dataset ID(s) to filter by.

    Can be a single dataset ID or comma-separated list. If not provided, aggregates
    across all accessible datasets
    """

    event_date_after: Annotated[str, PropertyInfo(alias="eventDateAfter")]
    """
    For measure=relationships: only count event links whose eventDate is on/after
    this date (ISO 8601). Use to bound 'top indicator' to recent activity.
    """

    event_date_before: Annotated[str, PropertyInfo(alias="eventDateBefore")]
    """
    For measure=relationships: only count event links whose eventDate is on/before
    this date (ISO 8601).
    """

    limit: float
    """Maximum number of aggregation results to return (1-100)"""

    measure: Literal["indicators", "relationships"]
    """
    What to count per group: 'indicators' (catalog rows, default) or 'relationships'
    (linked events per indicator). Use 'relationships' for 'top indicator by event
    activity'.
    """

    tag_uuid: Annotated[str, PropertyInfo(alias="tagUuid")]
    """Scope to indicators associated with this tag/actor UUID.

    Combine with measure=relationships for 'top indicator for an actor'.
    """
