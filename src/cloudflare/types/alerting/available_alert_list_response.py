# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AvailableAlertListResponse", "AvailableAlertListResponseItem"]

class AvailableAlertListResponseItem(BaseModel):
    description: Optional[str] = None
    """Describes the alert type."""

    display_name: Optional[str] = None
    """Alert type name."""

    filter_options: Optional[List[object]] = None
    """Format of additional configuration options (filters) for the alert type.

    Data type of filters during policy creation: Array of strings.
    """

    type: Optional[str] = None
    """Use this value when creating and updating a notification policy."""

AvailableAlertListResponse: TypeAlias = Dict[str, List[AvailableAlertListResponseItem]]