# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DiscoveryGetResponse"]


class DiscoveryGetResponse(BaseModel):
    schemas: List[object]

    timestamp: datetime
