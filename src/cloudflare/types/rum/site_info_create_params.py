# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["SiteInfoCreateParams"]


class SiteInfoCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    auto_install: bool
    """
    If enabled, the JavaScript snippet is automatically injected for orange-clouded
    sites.
    """

    host: str
    """The hostname to use for gray-clouded sites."""

    zone_tag: str
    """The zone identifier."""
