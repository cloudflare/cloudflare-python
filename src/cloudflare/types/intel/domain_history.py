# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from datetime import date

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DomainHistory", "Categorization"]

class Categorization(BaseModel):
    categories: Optional[List[object]] = None

    end: Optional[date] = None

    start: Optional[date] = None

class DomainHistory(BaseModel):
    categorizations: Optional[List[Categorization]] = None

    domain: Optional[str] = None