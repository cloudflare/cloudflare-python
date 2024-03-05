# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["DomainHistoryGetResponse", "DomainHistoryGetResponseItem", "DomainHistoryGetResponseItemCategorization"]


class DomainHistoryGetResponseItemCategorization(BaseModel):
    categories: Optional[object] = None

    end: Optional[date] = None

    start: Optional[date] = None


class DomainHistoryGetResponseItem(BaseModel):
    categorizations: Optional[List[DomainHistoryGetResponseItemCategorization]] = None

    domain: Optional[str] = None


DomainHistoryGetResponse = List[DomainHistoryGetResponseItem]
