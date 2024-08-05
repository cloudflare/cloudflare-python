# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["RuleUpdateResponse", "RuleUpdateResponseItem"]


class RuleUpdateResponseItem(BaseModel):
    description: Optional[str] = None

    enabled: Optional[bool] = None

    expression: Optional[str] = None

    snippet_name: Optional[str] = None
    """Snippet identifying name"""


RuleUpdateResponse: TypeAlias = List[RuleUpdateResponseItem]
