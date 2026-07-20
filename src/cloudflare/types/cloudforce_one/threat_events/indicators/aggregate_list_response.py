# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AggregateListResponse", "Aggregation"]


class Aggregation(BaseModel):
    count: float
    """Number of indicators for this aggregation"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, Optional[str]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[str]: ...
    else:
        __pydantic_extra__: Dict[str, Optional[str]]


class AggregateListResponse(BaseModel):
    aggregate_by: str = FieldInfo(alias="aggregateBy")
    """Column(s) that were aggregated by"""

    aggregations: List[Aggregation]
    """Array of aggregation results with dynamic fields based on aggregateBy columns"""

    failed_datasets: float = FieldInfo(alias="failedDatasets")
    """Number of datasets whose aggregation failed and were excluded from the result"""

    total: float
    """
    Total count in the aggregation: indicator rows when measure=indicators, or
    linked-event rows when measure=relationships
    """
