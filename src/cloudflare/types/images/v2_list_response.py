# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .image import Image
from ..._models import BaseModel

__all__ = ["V2ListResponse"]


class V2ListResponse(BaseModel):
    continuation_token: Optional[str] = None
    """Continuation token to fetch next page.

    Passed as a query param when requesting List V2 api endpoint.
    """

    images: Optional[List[Image]] = None
