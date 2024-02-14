# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["RegionLoadBalancerRegionsListRegionsParams"]


class RegionLoadBalancerRegionsListRegionsParams(TypedDict, total=False):
    country_code_a2: str
    """Two-letter alpha-2 country code followed in ISO 3166-1."""

    subdivision_code: str
    """Two-letter subdivision code followed in ISO 3166-2."""

    subdivision_code_a2: str
    """Two-letter subdivision code followed in ISO 3166-2."""
