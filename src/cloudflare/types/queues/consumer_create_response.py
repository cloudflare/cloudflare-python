# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConsumerCreateResponse", "Settings"]


class Settings(BaseModel):
    batch_size: Optional[float] = None
    """The maximum number of messages to include in a batch"""

    max_retries: Optional[float] = None
    """The maximum number of retries"""

    max_wait_time_ms: Optional[float] = None


class ConsumerCreateResponse(BaseModel):
    created_on: Optional[str] = None

    dead_letter_queue: Optional[str] = None
    """The name of the dead letter queue"""

    environment: Optional[str] = None

    queue_name: Optional[str] = None

    script_name: Optional[str] = None

    settings: Optional[Settings] = None
