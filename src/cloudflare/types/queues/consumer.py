# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Consumer", "Settings"]


class Settings(BaseModel):
    batch_size: Optional[float] = None
    """The maximum number of messages to include in a batch."""

    max_retries: Optional[float] = None
    """The maximum number of retries"""

    max_wait_time_ms: Optional[float] = None


class Consumer(BaseModel):
    created_on: Optional[str] = None

    environment: Optional[str] = None

    queue_name: Optional[str] = None

    service: Optional[str] = None

    settings: Optional[Settings] = None
