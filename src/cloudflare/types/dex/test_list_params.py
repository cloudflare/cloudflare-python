# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TestListParams"]


class TestListParams(TypedDict, total=False):
    colo: str
    """Optionally filter result stats to a Cloudflare colo.

    Cannot be used in combination with deviceId param.
    """

    device_id: Annotated[List[str], PropertyInfo(alias="deviceId")]
    """Optionally filter result stats to a specific device(s).

    Cannot be used in combination with colo param.
    """

    page: float
    """Page number of paginated results"""

    per_page: float
    """Number of items per page"""

    test_name: Annotated[str, PropertyInfo(alias="testName")]
    """Optionally filter results by test name"""
