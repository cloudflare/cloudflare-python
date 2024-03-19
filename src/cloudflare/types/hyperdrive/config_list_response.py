# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ConfigListResponse", "ConfigListResponseItem"]


class ConfigListResponseItem(BaseModel):
    id: Optional[str] = None
    """Identifier"""


ConfigListResponse = List[ConfigListResponseItem]
