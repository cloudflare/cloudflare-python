# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["CatalogListResponse", "Items"]


class Items(BaseModel):
    type: str


class CatalogListResponse(BaseModel):
    items: Items

    type: str
