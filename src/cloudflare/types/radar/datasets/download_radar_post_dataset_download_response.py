# File generated from our OpenAPI spec by Stainless.

from ...._models import BaseModel

__all__ = ["DownloadRadarPostDatasetDownloadResponse", "Dataset"]


class Dataset(BaseModel):
    url: str


class DownloadRadarPostDatasetDownloadResponse(BaseModel):
    dataset: Dataset
