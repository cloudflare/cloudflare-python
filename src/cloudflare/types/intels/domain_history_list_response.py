# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import date

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["DomainHistoryListResponse", "DomainHistoryListResponseItem", "DomainHistoryListResponseItemCategorization"]


class DomainHistoryListResponseItemCategorization(BaseModel):
    categories: Optional[object] = None

    end: Optional[date] = None

    start: Optional[date] = None


class DomainHistoryListResponseItem(BaseModel):
    categorizations: Optional[List[DomainHistoryListResponseItemCategorization]] = None

    domain: Optional[str] = None


DomainHistoryListResponse = List[DomainHistoryListResponseItem]
