# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AseGetResponse", "Meta", "Top0"]


class Meta(BaseModel):
    date_range: List[object] = FieldInfo(alias="dateRange")


class Top0(BaseModel):
    asn: int

    as_name: str = FieldInfo(alias="ASName")

    value: str
    """
    Percentage of updates by this AS out of the total updates by all autonomous
    systems.
    """


class AseGetResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
