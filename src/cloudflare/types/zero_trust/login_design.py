# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LoginDesign"]


class LoginDesign(BaseModel):
    background_color: Optional[str] = None
    """The background color on your login page."""

    footer_text: Optional[str] = None
    """The text at the bottom of your login page."""

    header_text: Optional[str] = None
    """The text at the top of your login page."""

    logo_path: Optional[str] = None
    """The URL of the logo on your login page."""

    text_color: Optional[str] = None
    """The text color on your login page."""
