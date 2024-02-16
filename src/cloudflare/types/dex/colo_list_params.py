# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required, Literal

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ColoListParams"]


class ColoListParams(TypedDict, total=False):
    time_end: Required[Annotated[str, PropertyInfo(alias="timeEnd")]]
    """End time for connection period in RFC3339 (ISO 8601) format."""

    time_start: Required[Annotated[str, PropertyInfo(alias="timeStart")]]
    """Start time for connection period in RFC3339 (ISO 8601) format."""

    sort_by: Annotated[Literal["fleet-status-usage", "application-tests-usage"], PropertyInfo(alias="sortBy")]
    """Type of usage that colos should be sorted by.

    If unspecified, returns all Cloudflare colos sorted alphabetically.
    """
