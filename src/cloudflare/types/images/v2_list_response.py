# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from .image import Image

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["V2ListResponse"]


class V2ListResponse(BaseModel):
    continuation_token: Optional[str] = None
    """Continuation token to fetch next page.

    Passed as a query param when requesting List V2 api endpoint.
    """

    images: Optional[List[Image]] = None
