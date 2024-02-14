# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["IndicatorFeedPermissionsViewResponse", "IndicatorFeedPermissionsViewResponseItem"]


class IndicatorFeedPermissionsViewResponseItem(BaseModel):
    id: Optional[int] = None
    """The unique identifier for the indicator feed"""

    description: Optional[str] = None
    """The description of the example test"""

    name: Optional[str] = None
    """The name of the indicator feed"""


IndicatorFeedPermissionsViewResponse = List[IndicatorFeedPermissionsViewResponseItem]
