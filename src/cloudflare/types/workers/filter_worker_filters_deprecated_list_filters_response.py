# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["FilterWorkerFiltersDeprecatedListFiltersResponse", "FilterWorkerFiltersDeprecatedListFiltersResponseItem"]


class FilterWorkerFiltersDeprecatedListFiltersResponseItem(BaseModel):
    id: str
    """Identifier"""

    enabled: bool

    pattern: str


FilterWorkerFiltersDeprecatedListFiltersResponse = List[FilterWorkerFiltersDeprecatedListFiltersResponseItem]
