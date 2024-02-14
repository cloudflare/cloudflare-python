# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["ConsumerUpdateResponse", "Settings"]


class Settings(BaseModel):
    batch_size: Optional[float] = None

    max_retries: Optional[float] = None

    max_wait_time_ms: Optional[float] = None


class ConsumerUpdateResponse(BaseModel):
    created_on: Optional[object] = None

    dead_letter_queue: Optional[object] = None

    environment: Optional[object] = None

    queue_name: Optional[object] = None

    script_name: Optional[object] = None

    settings: Optional[Settings] = None
