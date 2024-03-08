# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AccessCustomPage"]


class AccessCustomPage(BaseModel):
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
