# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from ..._utils import PropertyInfo

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["TracerouteTestPercentilesParams"]


class TracerouteTestPercentilesParams(TypedDict, total=False):
    account_id: Required[str]

    time_end: Required[Annotated[str, PropertyInfo(alias="timeEnd")]]
    """End time for aggregate metrics in ISO format"""

    time_start: Required[Annotated[str, PropertyInfo(alias="timeStart")]]
    """Start time for aggregate metrics in ISO format"""

    colo: str
    """Optionally filter result stats to a Cloudflare colo.

    Cannot be used in combination with deviceId param.
    """

    device_id: Annotated[List[str], PropertyInfo(alias="deviceId")]
    """Optionally filter result stats to a specific device(s).

    Cannot be used in combination with colo param.
    """
