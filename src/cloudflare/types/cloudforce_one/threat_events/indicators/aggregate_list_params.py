# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
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

    created_after: Annotated[Union[Union[str, datetime], str], PropertyInfo(alias="createdAfter", format="iso8601")]
    """
    Filter indicators created after this date/datetime (ISO 8601, e.g., '2024-01-01'
    or '2024-01-01T00:00:00Z')
    """

    created_before: Annotated[Union[Union[str, datetime], str], PropertyInfo(alias="createdBefore", format="iso8601")]
    """
    Filter indicators created before this date/datetime (ISO 8601, e.g.,
    '2024-12-31' or '2024-12-31T23:59:59Z')
    """

    dataset_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="datasetIds")]
    """
    Dataset UUIDs to filter by, or one standalone scope value: 'all'/'\\**' for all
    accessible datasets, 'analytics' for isAnalytics=true datasets, or 'operational'
    for isAnalytics=false datasets. If not provided, aggregates across all
    accessible datasets.
    """

    event_date_after: Annotated[str, PropertyInfo(alias="eventDateAfter")]
    """
    For measure=relationships: only count indicator→event links whose relationship
    was created/observed on or after this date (ISO 8601). Bounds the activity view
    to recently-observed links. Note: this filters by the relationship's createdAt
    (link-observation time), not the underlying event's business date.
    """

    event_date_before: Annotated[str, PropertyInfo(alias="eventDateBefore")]
    """
    For measure=relationships: only count indicator→event links whose relationship
    was created/observed on or before this date (ISO 8601). Bounds the activity view
    by the relationship's createdAt (link-observation time), not the underlying
    event's business date.
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
