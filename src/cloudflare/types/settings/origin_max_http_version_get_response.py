# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["OriginMaxHTTPVersionGetResponse"]


class OriginMaxHTTPVersionGetResponse(BaseModel):
    id: Literal["origin_max_http_version"]
    """Value of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Literal["2", "1"]
    """Value of the Origin Max HTTP Version Setting."""
