# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from datetime import datetime

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["BlockSenderGetResponse"]

class BlockSenderGetResponse(BaseModel):
    id: int

    created_at: datetime

    is_regex: bool

    last_modified: datetime

    pattern: str

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]

    comments: Optional[str] = None