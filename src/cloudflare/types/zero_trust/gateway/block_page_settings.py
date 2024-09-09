# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["BlockPageSettings"]


class BlockPageSettings(BaseModel):
    background_color: Optional[str] = None
    """Block page background color in #rrggbb format."""

    enabled: Optional[bool] = None
    """Enable only cipher suites and TLS versions compliant with FIPS 140-2."""

    footer_text: Optional[str] = None
    """Block page footer text."""

    header_text: Optional[str] = None
    """Block page header text."""

    logo_path: Optional[str] = None
    """Full URL to the logo file."""

    mailto_address: Optional[str] = None
    """Admin email for users to contact."""

    mailto_subject: Optional[str] = None
    """Subject line for emails created from block page."""

    name: Optional[str] = None
    """Block page title."""

    suppress_footer: Optional[bool] = None
    """Suppress detailed info at the bottom of the block page."""
