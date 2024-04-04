# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...shared import UnnamedSchemaRef92

__all__ = ["ZoneSettingMinifyParam", "Value"]


class Value(TypedDict, total=False):
    css: UnnamedSchemaRef92
    """Automatically minify all CSS files for your website."""

    html: Literal["on", "off"]
    """Automatically minify all HTML files for your website."""

    js: Literal["on", "off"]
    """Automatically minify all JavaScript files for your website."""


class ZoneSettingMinifyParam(TypedDict, total=False):
    id: Required[Literal["minify"]]
    """Zone setting identifier."""

    value: Required[Value]
    """Current value of the zone setting."""
