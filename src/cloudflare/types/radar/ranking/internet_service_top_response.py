# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InternetServiceTopResponse", "Meta", "MetaTop0", "Top0"]


class MetaTop0(BaseModel):
    date: str

    service_category: str = FieldInfo(alias="serviceCategory")


class Meta(BaseModel):
    top_0: MetaTop0


class Top0(BaseModel):
    rank: int

    service: str


class InternetServiceTopResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
