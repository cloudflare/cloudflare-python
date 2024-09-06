# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Snippet"]


class Snippet(BaseModel):
    created_on: Optional[str] = None
    """Creation time of the snippet"""

    modified_on: Optional[str] = None
    """Modification time of the snippet"""

    snippet_name: Optional[str] = None
    """Snippet identifying name"""
