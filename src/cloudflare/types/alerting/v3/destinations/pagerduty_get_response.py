# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["PagerdutyGetResponse", "PagerdutyGetResponseItem"]


class PagerdutyGetResponseItem(BaseModel):
    id: Optional[str] = None
    """UUID"""

    name: Optional[str] = None
    """The name of the pagerduty service."""


PagerdutyGetResponse = List[PagerdutyGetResponseItem]
