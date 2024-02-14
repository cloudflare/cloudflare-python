# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["MinifyUpdateParams", "Value"]


class MinifyUpdateParams(TypedDict, total=False):
    value: Required[Value]
    """Value of the zone setting."""


class Value(TypedDict, total=False):
    css: Literal["on", "off"]
    """Automatically minify all CSS files for your website."""

    html: Literal["on", "off"]
    """Automatically minify all HTML files for your website."""

    js: Literal["on", "off"]
    """Automatically minify all JavaScript files for your website."""
