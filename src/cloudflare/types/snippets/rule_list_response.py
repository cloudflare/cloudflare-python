# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["RuleListResponse", "RuleListResponseItem"]


class RuleListResponseItem(BaseModel):
    description: Optional[str] = None

    enabled: Optional[bool] = None

    expression: Optional[str] = None

    snippet_name: Optional[str] = None
    """Snippet identifying name"""


RuleListResponse = List[RuleListResponseItem]
