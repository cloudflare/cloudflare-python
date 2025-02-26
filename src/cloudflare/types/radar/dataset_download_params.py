# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DatasetDownloadParams"]


class DatasetDownloadParams(TypedDict, total=False):
    dataset_id: Required[Annotated[int, PropertyInfo(alias="datasetId")]]

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""
