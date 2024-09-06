# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IssueClassResponse", "IssueClassResponseItem"]


class IssueClassResponseItem(BaseModel):
    count: Optional[int] = None

    value: Optional[str] = None


IssueClassResponse: TypeAlias = List[IssueClassResponseItem]
