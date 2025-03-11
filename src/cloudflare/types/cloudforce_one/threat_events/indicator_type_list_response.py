# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["IndicatorTypeListResponse", "Items"]


class Items(BaseModel):
    type: str


class IndicatorTypeListResponse(BaseModel):
    items: Items

    type: str
