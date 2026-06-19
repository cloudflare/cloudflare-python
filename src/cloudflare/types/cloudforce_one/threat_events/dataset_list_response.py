# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DatasetListResponse", "DatasetListResponseItem"]


class DatasetListResponseItem(BaseModel):
    is_public: bool = FieldInfo(alias="isPublic")

    name: str

    uuid: str

    deleted_at: Optional[str] = FieldInfo(alias="deletedAt", default=None)


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]
