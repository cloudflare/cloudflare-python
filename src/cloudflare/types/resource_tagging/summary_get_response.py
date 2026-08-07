# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["SummaryGetResponse", "SummaryGetResponseItem"]


class SummaryGetResponseItem(BaseModel):
    key: str
    """A tag key."""

    values: List[str]
    """All distinct values for this tag key."""


SummaryGetResponse: TypeAlias = List[SummaryGetResponseItem]
