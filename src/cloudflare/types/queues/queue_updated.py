# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["QueueUpdated"]

class QueueUpdated(BaseModel):
    created_on: Optional[str] = None

    modified_on: Optional[str] = None

    queue_id: Optional[str] = None

    queue_name: Optional[str] = None