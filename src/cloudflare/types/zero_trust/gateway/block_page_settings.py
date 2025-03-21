# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BlockPageSettings"]


class BlockPageSettings(BaseModel):
    background_color: Optional[str] = None
    """
    If mode is customized_block_page: block page background color in #rrggbb format.
    """

    enabled: Optional[bool] = None
    """Enable only cipher suites and TLS versions compliant with FIPS 140-2."""

    footer_text: Optional[str] = None
    """If mode is customized_block_page: block page footer text."""

    header_text: Optional[str] = None
    """If mode is customized_block_page: block page header text."""

    include_context: Optional[bool] = None
    """
    If mode is redirect_uri: when enabled, context will be appended to target_uri as
    query parameters.
    """

    logo_path: Optional[str] = None
    """If mode is customized_block_page: full URL to the logo file."""

    mailto_address: Optional[str] = None
    """If mode is customized_block_page: admin email for users to contact."""

    mailto_subject: Optional[str] = None
    """
    If mode is customized_block_page: subject line for emails created from block
    page.
    """

    mode: Optional[Literal["customized_block_page", "redirect_uri"]] = None
    """
    Controls whether the user is redirected to a Cloudflare-hosted block page or to
    a customer-provided URI.
    """

    name: Optional[str] = None
    """If mode is customized_block_page: block page title."""

    suppress_footer: Optional[bool] = None
    """
    If mode is customized_block_page: suppress detailed info at the bottom of the
    block page.
    """

    target_uri: Optional[str] = None
    """If mode is redirect_uri: URI to which the user should be redirected."""
