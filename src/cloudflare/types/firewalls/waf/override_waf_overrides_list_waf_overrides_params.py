# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["OverrideWAFOverridesListWAFOverridesParams"]


class OverrideWAFOverridesListWAFOverridesParams(TypedDict, total=False):
    page: float
    """The page number of paginated results."""

    per_page: float
    """The number of WAF overrides per page."""
