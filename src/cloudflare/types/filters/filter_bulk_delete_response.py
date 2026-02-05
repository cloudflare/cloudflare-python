# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["FilterBulkDeleteResponse", "FilterBulkDeleteResponseItem"]


class FilterBulkDeleteResponseItem(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the filter."""


FilterBulkDeleteResponse: TypeAlias = List[FilterBulkDeleteResponseItem]
