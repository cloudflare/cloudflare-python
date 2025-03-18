# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["AttackerListResponse", "Items"]


class Items(BaseModel):
    type: str


class AttackerListResponse(BaseModel):
    items: Items

    type: str
