# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["CustomPageGetResponse"]


class CustomPageGetResponse(BaseModel):
    custom_html: str
    """Custom page HTML."""

    name: str
    """Custom page name."""

    type: Literal["identity_denied", "forbidden"]
    """Custom page type."""

    app_count: Optional[int] = None
    """Number of apps the custom page is assigned to."""

    created_at: Optional[datetime] = None

    uid: Optional[str] = None
    """UUID"""

    updated_at: Optional[datetime] = None
