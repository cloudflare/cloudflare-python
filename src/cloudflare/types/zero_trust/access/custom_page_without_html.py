# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CustomPageWithoutHTML"]


class CustomPageWithoutHTML(BaseModel):
    name: str
    """Custom page name."""

    type: Literal["identity_denied", "forbidden"]
    """Custom page type."""

    uid: Optional[str] = None
    """UUID."""
