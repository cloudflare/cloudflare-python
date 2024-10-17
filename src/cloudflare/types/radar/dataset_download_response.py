# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["DatasetDownloadResponse", "Dataset"]


class Dataset(BaseModel):
    url: str


class DatasetDownloadResponse(BaseModel):
    dataset: Dataset
