# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["RegionalHostnameCreateParams"]

class RegionalHostnameCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    hostname: Required[str]
    """DNS hostname to be regionalized, must be a subdomain of the zone.

    Wildcards are supported for one level, e.g `*.example.com`
    """

    region_key: Required[str]
    """Identifying key for the region"""