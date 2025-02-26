# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DatasetListParams"]


class DatasetListParams(TypedDict, total=False):
    dataset_type: Annotated[Literal["RANKING_BUCKET", "REPORT"], PropertyInfo(alias="datasetType")]
    """Filters results by dataset type."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    offset: int
    """Skips the specified number of objects before fetching the results."""
