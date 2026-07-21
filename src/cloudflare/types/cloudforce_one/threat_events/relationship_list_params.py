# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["RelationshipListParams"]


class RelationshipListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    dataset_id: Required[Annotated[str, PropertyInfo(alias="datasetId")]]
    """The dataset ID to search within."""

    direction: Literal["ancestors", "descendants", "both"]
    """The direction to traverse the graph. Defaults to 'both' to search all."""

    include_parent: Annotated[bool, PropertyInfo(alias="includeParent")]
    """Whether to include the starting event in the results. Defaults to true."""

    indicator_type_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="indicatorTypeIds")]
    """An optional array of indicator type IDs to filter the results by."""

    max_depth: Annotated[float, PropertyInfo(alias="maxDepth")]
    """The maximum depth to traverse. Defaults to 5."""

    page: float

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]

    relationship_types: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="relationshipTypes")]
    """An optional array of relationship types to filter by."""
