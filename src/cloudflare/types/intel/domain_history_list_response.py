# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["DomainHistoryListResponse", "DomainHistoryListResponseItem", "DomainHistoryListResponseItemCategorization"]


class DomainHistoryListResponseItemCategorization(BaseModel):
    categories: Optional[object] = None

    end: Optional[date] = None

    start: Optional[date] = None


class DomainHistoryListResponseItem(BaseModel):
    categorizations: Optional[List[DomainHistoryListResponseItemCategorization]] = None

    domain: Optional[str] = None


DomainHistoryListResponse = List[DomainHistoryListResponseItem]
