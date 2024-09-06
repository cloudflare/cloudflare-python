# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["InvestigateRawResponse"]


class InvestigateRawResponse(BaseModel):
    raw: str
    """UTF-8 encoded eml file"""
