# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["IssueTypeResponse", "IssueTypeResponseItem"]


class IssueTypeResponseItem(BaseModel):
    count: Optional[int] = None

    value: Optional[str] = None


IssueTypeResponse: TypeAlias = List[IssueTypeResponseItem]
