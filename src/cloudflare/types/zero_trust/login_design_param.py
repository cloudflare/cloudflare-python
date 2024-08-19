# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LoginDesignParam"]


class LoginDesignParam(TypedDict, total=False):
    background_color: str
    """The background color on your login page."""

    footer_text: str
    """The text at the bottom of your login page."""

    header_text: str
    """The text at the top of your login page."""

    logo_path: str
    """The URL of the logo on your login page."""

    text_color: str
    """The text color on your login page."""
