# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RuleUpdateResponse", "RuleUpdateResponseItem"]

class RuleUpdateResponseItem(BaseModel):
    description: Optional[str] = None

    enabled: Optional[bool] = None

    expression: Optional[str] = None

    snippet_name: Optional[str] = None
    """Snippet identifying name"""

RuleUpdateResponse: TypeAlias = List[RuleUpdateResponseItem]