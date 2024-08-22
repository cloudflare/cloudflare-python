# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PermissionListResponse", "PermissionListResponseItem"]

class PermissionListResponseItem(BaseModel):
    id: Optional[int] = None
    """The unique identifier for the indicator feed"""

    description: Optional[str] = None
    """The description of the example test"""

    is_attributable: Optional[bool] = None
    """Whether the indicator feed can be attributed to a provider"""

    is_downloadable: Optional[bool] = None
    """Whether the indicator feed can be downloaded"""

    is_public: Optional[bool] = None
    """Whether the indicator feed is exposed to customers"""

    name: Optional[str] = None
    """The name of the indicator feed"""

PermissionListResponse: TypeAlias = List[PermissionListResponseItem]