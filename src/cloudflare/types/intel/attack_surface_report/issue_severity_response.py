# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["IssueSeverityResponse", "IssueSeverityResponseItem"]


class IssueSeverityResponseItem(BaseModel):
    count: Optional[int] = None

    value: Optional[str] = None


IssueSeverityResponse = List[IssueSeverityResponseItem]
