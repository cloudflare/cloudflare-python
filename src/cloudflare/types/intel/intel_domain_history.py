# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["IntelDomainHistory", "Categorization"]


class Categorization(BaseModel):
    categories: Optional[List[object]] = None

    end: Optional[date] = None

    start: Optional[date] = None


class IntelDomainHistory(BaseModel):
    categorizations: Optional[List[Categorization]] = None

    domain: Optional[str] = None
