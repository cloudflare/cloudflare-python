# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DatasetListResponse", "DatasetListResponseItem"]


class DatasetListResponseItem(BaseModel):
    indicator_write_mode: Literal["read_only", "create_only", "full"] = FieldInfo(alias="indicatorWriteMode")
    """
    Effective indicator mutation capability after account/dataset authorization and
    dataset storage capability are applied. API Gateway method permissions are
    separate and must also allow the requested operation.
    """

    is_analytics: bool = FieldInfo(alias="isAnalytics")

    is_public: bool = FieldInfo(alias="isPublic")

    name: str

    uuid: str

    deleted_at: Optional[str] = FieldInfo(alias="deletedAt", default=None)


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]
