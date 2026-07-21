# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["ByDatasetListResponse", "Items"]


class Items(BaseModel):
    type: str


class ByDatasetListResponse(BaseModel):
    items: Items

    type: str
