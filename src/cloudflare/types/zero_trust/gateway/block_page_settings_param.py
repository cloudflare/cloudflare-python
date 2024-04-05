# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BlockPageSettingsParam"]


class BlockPageSettingsParam(TypedDict, total=False):
    background_color: str
    """Block page background color in #rrggbb format."""

    enabled: bool
    """Enable only cipher suites and TLS versions compliant with FIPS 140-2."""

    footer_text: str
    """Block page footer text."""

    header_text: str
    """Block page header text."""

    logo_path: str
    """Full URL to the logo file."""

    mailto_address: str
    """Admin email for users to contact."""

    mailto_subject: str
    """Subject line for emails created from block page."""

    name: str
    """Block page title."""

    suppress_footer: bool
    """Suppress detailed info at the bottom of the block page."""
