# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConsumerUpdateResponse", "Settings"]


class Settings(BaseModel):
    batch_size: Optional[float] = None

    max_retries: Optional[float] = None

    max_wait_time_ms: Optional[float] = None


class ConsumerUpdateResponse(BaseModel):
    created_on: Optional[object] = None

    dead_letter_queue: Optional[str] = None

    environment: Optional[object] = None

    queue_name: Optional[object] = None

    script_name: Optional[object] = None

    settings: Optional[Settings] = None
