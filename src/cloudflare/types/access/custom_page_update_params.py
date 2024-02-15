# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["CustomPageUpdateParams"]


class CustomPageUpdateParams(TypedDict, total=False):
    identifier: Required[str]
    """Identifier"""

    custom_html: Required[str]
    """Custom page HTML."""

    name: Required[str]
    """Custom page name."""

    type: Required[Literal["identity_denied", "forbidden"]]
    """Custom page type."""

    app_count: int
    """Number of apps the custom page is assigned to."""
