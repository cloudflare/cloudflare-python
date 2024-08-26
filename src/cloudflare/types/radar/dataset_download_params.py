# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required, Literal

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["DatasetDownloadParams"]

class DatasetDownloadParams(TypedDict, total=False):
    dataset_id: Required[Annotated[int, PropertyInfo(alias="datasetId")]]

    format: Literal["JSON", "CSV"]
    """Format results are returned in."""