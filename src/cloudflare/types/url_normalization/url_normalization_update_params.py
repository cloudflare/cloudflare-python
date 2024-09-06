# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["URLNormalizationUpdateParams"]


class URLNormalizationUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    scope: str
    """The scope of the URL normalization."""

    type: str
    """The type of URL normalization performed by Cloudflare."""
