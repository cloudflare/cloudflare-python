# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SkipConfiguration"]

class SkipConfiguration(BaseModel):
    files: bool
    """If the content type is a file, skip context analysis and return all matches."""