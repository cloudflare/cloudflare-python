# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["QueueQueueCreateQueueResponse"]


class QueueQueueCreateQueueResponse(BaseModel):
    created_on: Optional[object] = None

    modified_on: Optional[object] = None

    queue_id: Optional[object] = None

    queue_name: Optional[str] = None
