# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DatasetListParams"]


class DatasetListParams(TypedDict, total=False):
    dataset_type: Annotated[Literal["RANKING_BUCKET", "REPORT"], PropertyInfo(alias="datasetType")]
    """Dataset type."""

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    limit: int
    """Limit the number of objects in the response."""

    offset: int
    """Number of objects to skip before grabbing results."""
