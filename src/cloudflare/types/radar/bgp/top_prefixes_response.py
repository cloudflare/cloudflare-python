# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["TopPrefixesResponse", "Meta", "Top0"]


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")


class Top0(BaseModel):
    prefix: str

    value: str


class TopPrefixesResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
