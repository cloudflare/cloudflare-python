# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["LanguageUpdateParams"]

class LanguageUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    identifier: Required[str]
    """A Cloudflare-generated unique identifier for a media item."""

    file: Required[str]
    """The WebVTT file containing the caption or subtitle content."""