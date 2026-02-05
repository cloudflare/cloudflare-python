# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CustomPage"]


class CustomPage(BaseModel):
    custom_html: str
    """Custom page HTML."""

    name: str
    """Custom page name."""

    type: Literal["identity_denied", "forbidden"]
    """Custom page type."""

    uid: Optional[str] = None
    """UUID."""
