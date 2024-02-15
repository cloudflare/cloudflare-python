# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["DatasetListResponse", "Dataset"]


class Dataset(BaseModel):
    id: int

    description: str

    meta: object

    tags: List[str]

    title: str

    type: str


class DatasetListResponse(BaseModel):
    datasets: List[Dataset]
