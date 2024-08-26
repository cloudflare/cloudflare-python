# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TieredCachingEditResponse"]

class TieredCachingEditResponse(BaseModel):
    id: str
    """The identifier of the caching setting"""

    editable: bool
    """Whether the setting is editable"""

    modified_on: datetime
    """The time when the setting was last modified"""

    value: Literal["on", "off"]
    """The status of the feature being on / off"""