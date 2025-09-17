# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BlockPageSettings"]


class BlockPageSettings(BaseModel):
    background_color: Optional[str] = None
    """
    Specify the block page background color in `#rrggbb` format when the mode is
    customized_block_page.
    """

    enabled: Optional[bool] = None
    """Specify whether to enable the custom block page."""

    footer_text: Optional[str] = None
    """Specify the block page footer text when the mode is customized_block_page."""

    header_text: Optional[str] = None
    """Specify the block page header text when the mode is customized_block_page."""

    include_context: Optional[bool] = None
    """Specify whether to append context to target_uri as query parameters.

    This applies only when the mode is redirect_uri.
    """

    logo_path: Optional[str] = None
    """Specify the full URL to the logo file when the mode is customized_block_page."""

    mailto_address: Optional[str] = None
    """
    Specify the admin email for users to contact when the mode is
    customized_block_page.
    """

    mailto_subject: Optional[str] = None
    """
    Specify the subject line for emails created from the block page when the mode is
    customized_block_page.
    """

    mode: Optional[Literal["", "customized_block_page", "redirect_uri"]] = None
    """
    Specify whether to redirect users to a Cloudflare-hosted block page or a
    customer-provided URI.
    """

    name: Optional[str] = None
    """Specify the block page title when the mode is customized_block_page."""

    read_only: Optional[bool] = None
    """
    Indicate that this setting was shared via the Orgs API and read only for the
    current account.
    """

    source_account: Optional[str] = None
    """Indicate the account tag of the account that shared this setting."""

    suppress_footer: Optional[bool] = None
    """
    Specify whether to suppress detailed information at the bottom of the block page
    when the mode is customized_block_page.
    """

    target_uri: Optional[str] = None
    """Specify the URI to redirect users to when the mode is redirect_uri."""

    version: Optional[int] = None
    """Indicate the version number of the setting."""
