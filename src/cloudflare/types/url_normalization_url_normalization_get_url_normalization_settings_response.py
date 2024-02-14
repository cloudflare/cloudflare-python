# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse"]


class URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse(BaseModel):
    scope: Optional[str] = None
    """The scope of the URL normalization."""

    type: Optional[str] = None
    """The type of URL normalization performed by Cloudflare."""
