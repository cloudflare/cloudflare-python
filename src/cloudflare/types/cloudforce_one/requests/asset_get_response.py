# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["AssetGetResponse", "AssetGetResponseItem"]


class AssetGetResponseItem(BaseModel):
    id: int
    """Asset ID"""

    name: str
    """Asset name"""

    created: Optional[datetime] = None
    """Asset creation time"""

    description: Optional[str] = None
    """Asset description"""

    file_type: Optional[str] = None
    """Asset file type"""


AssetGetResponse: TypeAlias = List[AssetGetResponseItem]
