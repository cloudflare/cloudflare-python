# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["URLNormalizationUpdateResponse"]

class URLNormalizationUpdateResponse(BaseModel):
    scope: Optional[str] = None
    """The scope of the URL normalization."""

    type: Optional[str] = None
    """The type of URL normalization performed by Cloudflare."""