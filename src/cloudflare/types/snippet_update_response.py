# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["SnippetUpdateResponse"]


class SnippetUpdateResponse(BaseModel):
    created_on: Optional[str] = None
    """Creation time of the snippet"""

    modified_on: Optional[str] = None
    """Modification time of the snippet"""

    snippet_name: Optional[str] = None
    """Snippet identifying name"""
