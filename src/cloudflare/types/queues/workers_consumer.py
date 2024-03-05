# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["WorkersConsumer", "Settings"]


class Settings(BaseModel):
    batch_size: Optional[float] = None

    max_retries: Optional[float] = None

    max_wait_time_ms: Optional[float] = None


class WorkersConsumer(BaseModel):
    created_on: Optional[object] = None

    environment: Optional[object] = None

    queue_name: Optional[object] = None

    service: Optional[object] = None

    settings: Optional[Settings] = None
