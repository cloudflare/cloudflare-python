# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["SiteInfoCreateParams"]


class SiteInfoCreateParams(TypedDict, total=False):
    auto_install: bool
    """
    If enabled, the JavaScript snippet is automatically injected for orange-clouded
    sites.
    """

    host: str
    """The hostname to use for gray-clouded sites."""

    zone_tag: str
    """The zone identifier."""
