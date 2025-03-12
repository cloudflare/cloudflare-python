# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DatasetListResponse", "DatasetListResponseItem"]


class DatasetListResponseItem(BaseModel):
    is_public: bool = FieldInfo(alias="isPublic")

    name: str

    uuid: str


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]
