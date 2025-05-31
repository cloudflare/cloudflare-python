# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["HealthGetResponse", "Items"]


class Items(BaseModel):
    type: str


class HealthGetResponse(BaseModel):
    items: Items

    type: str
