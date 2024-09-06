# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from .override_url import OverrideURL

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["OverrideCreateParams"]


class OverrideCreateParams(TypedDict, total=False):
    urls: Required[List[OverrideURL]]
    """The URLs to include in the current WAF override.

    You can use wildcards. Each entered URL will be escaped before use, which means
    you can only use simple wildcard patterns.
    """
