# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesMinifyParam", "Value"]


class Value(TypedDict, total=False):
    css: Literal["on", "off"]
    """Automatically minify all CSS files for your website."""

    html: Literal["on", "off"]
    """Automatically minify all HTML files for your website."""

    js: Literal["on", "off"]
    """Automatically minify all JavaScript files for your website."""


class ZonesMinifyParam(TypedDict, total=False):
    id: Required[Literal["minify"]]
    """Zone setting identifier."""

    value: Required[Value]
    """Current value of the zone setting."""
