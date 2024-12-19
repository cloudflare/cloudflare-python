# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .image import Image
from ..._models import BaseModel

__all__ = ["V1ListResponse"]


class V1ListResponse(BaseModel):
    images: Optional[List[Image]] = None
