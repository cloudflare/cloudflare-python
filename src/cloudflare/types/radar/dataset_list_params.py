# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Annotated

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
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
