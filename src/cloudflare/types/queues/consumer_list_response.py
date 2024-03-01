# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

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
