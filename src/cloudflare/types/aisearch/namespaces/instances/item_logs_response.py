# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ItemLogsResponse", "ItemLogsResponseItem"]


class ItemLogsResponseItem(BaseModel):
    action: str

    chunk_count: Optional[int] = FieldInfo(alias="chunkCount", default=None)

    error_type: Optional[str] = FieldInfo(alias="errorType", default=None)

    file_key: str = FieldInfo(alias="fileKey")

    message: Optional[str] = None

    processing_time_ms: Optional[int] = FieldInfo(alias="processingTimeMs", default=None)

    timestamp: datetime


ItemLogsResponse: TypeAlias = List[ItemLogsResponseItem]
