# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BlockPageSettingsParam"]


class BlockPageSettingsParam(TypedDict, total=False):
    background_color: str
    """
    If mode is customized_block_page: block page background color in #rrggbb format.
    """

    enabled: bool
    """Enable only cipher suites and TLS versions compliant with FIPS 140-2."""

    footer_text: str
    """If mode is customized_block_page: block page footer text."""

    header_text: str
    """If mode is customized_block_page: block page header text."""

    include_context: bool
    """
    If mode is redirect_uri: when enabled, context will be appended to target_uri as
    query parameters.
    """

    logo_path: str
    """If mode is customized_block_page: full URL to the logo file."""

    mailto_address: str
    """If mode is customized_block_page: admin email for users to contact."""

    mailto_subject: str
    """
    If mode is customized_block_page: subject line for emails created from block
    page.
    """

    mode: Literal["customized_block_page", "redirect_uri"]
    """
    Controls whether the user is redirected to a Cloudflare-hosted block page or to
    a customer-provided URI.
    """

    name: str
    """If mode is customized_block_page: block page title."""

    suppress_footer: bool
    """
    If mode is customized_block_page: suppress detailed info at the bottom of the
    block page.
    """

    target_uri: str
    """If mode is redirect_uri: URI to which the user should be redirected."""
