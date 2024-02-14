# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, Annotated

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["BucketCreateParams"]


class BucketCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the bucket"""

    location_hint: Annotated[Literal["apac", "eeur", "enam", "weur", "wnam"], PropertyInfo(alias="locationHint")]
    """Location of the bucket"""
