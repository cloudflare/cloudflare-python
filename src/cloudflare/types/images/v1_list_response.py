# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .image import Image
from ..shared import UnnamedSchemaRef172
from ..._models import BaseModel

__all__ = ["V1ListResponse", "Result"]


class Result(BaseModel):
    images: Optional[List[Image]] = None


class V1ListResponse(BaseModel):
    errors: List[UnnamedSchemaRef172]

    messages: List[UnnamedSchemaRef172]

    result: Result

    success: Literal[True]
    """Whether the API call was successful"""
