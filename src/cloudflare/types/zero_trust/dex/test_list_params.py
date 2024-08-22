# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import List

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["TestListParams"]

class TestListParams(TypedDict, total=False):
    account_id: Required[str]

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