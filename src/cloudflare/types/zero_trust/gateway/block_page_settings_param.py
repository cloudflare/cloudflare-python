# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["BlockPageSettingsParam"]


class BlockPageSettingsParam(TypedDict, total=False):
    background_color: str
    """
    Specify the block page background color in `#rrggbb` format when the mode is
    customized_block_page.
    """

    enabled: Optional[bool]
    """Specify whether to enable the custom block page."""

    footer_text: str
    """Specify the block page footer text when the mode is customized_block_page."""

    header_text: str
    """Specify the block page header text when the mode is customized_block_page."""

    include_context: bool
    """Specify whether to append context to target_uri as query parameters.

    This applies only when the mode is redirect_uri.
    """

    logo_path: str
    """Specify the full URL to the logo file when the mode is customized_block_page."""

    mailto_address: str
    """
    Specify the admin email for users to contact when the mode is
    customized_block_page.
    """

    mailto_subject: str
    """
    Specify the subject line for emails created from the block page when the mode is
    customized_block_page.
    """

    mode: Literal["", "customized_block_page", "redirect_uri"]
    """
    Specify whether to redirect users to a Cloudflare-hosted block page or a
    customer-provided URI.
    """

    name: str
    """Specify the block page title when the mode is customized_block_page."""

    suppress_footer: bool
    """
    Specify whether to suppress detailed information at the bottom of the block page
    when the mode is customized_block_page.
    """

    target_uri: str
    """Specify the URI to redirect users to when the mode is redirect_uri."""
