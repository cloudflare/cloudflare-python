# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["SnippetRuleUpdateResponse", "SnippetRuleUpdateResponseItem"]


class SnippetRuleUpdateResponseItem(BaseModel):
    description: Optional[str] = None

    enabled: Optional[bool] = None

    expression: Optional[str] = None

    snippet_name: Optional[str] = None
    """Snippet identifying name"""


SnippetRuleUpdateResponse = List[SnippetRuleUpdateResponseItem]
