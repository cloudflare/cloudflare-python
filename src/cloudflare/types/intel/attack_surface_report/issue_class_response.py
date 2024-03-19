# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["IssueClassResponse", "IssueClassResponseItem"]


class IssueClassResponseItem(BaseModel):
    count: Optional[int] = None

    value: Optional[str] = None


IssueClassResponse = List[IssueClassResponseItem]
