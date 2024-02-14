# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["ConsumerListResponse", "ConsumerListResponseItem", "ConsumerListResponseItemSettings"]


class ConsumerListResponseItemSettings(BaseModel):
    batch_size: Optional[float] = None

    max_retries: Optional[float] = None

    max_wait_time_ms: Optional[float] = None


class ConsumerListResponseItem(BaseModel):
    created_on: Optional[object] = None

    environment: Optional[object] = None

    queue_name: Optional[object] = None

    service: Optional[object] = None

    settings: Optional[ConsumerListResponseItemSettings] = None


ConsumerListResponse = List[ConsumerListResponseItem]
