# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["PayloadDeleteResponse", "PayloadDeleteResponseItem"]


class PayloadDeleteResponseItem(BaseModel):
    id: Optional[str] = None
    """The unique ID for this custom scan expression"""

    payload: Optional[str] = None
    """Ruleset expression to use in matching content objects"""


PayloadDeleteResponse: TypeAlias = List[PayloadDeleteResponseItem]
