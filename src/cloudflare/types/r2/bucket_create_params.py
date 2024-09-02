# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, Annotated

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["BucketCreateParams"]


class BucketCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    name: Required[str]
    """Name of the bucket"""

    location_hint: Annotated[Literal["apac", "eeur", "enam", "weur", "wnam"], PropertyInfo(alias="locationHint")]
    """Location of the bucket"""

    storage_class: Annotated[Literal["Standard", "InfrequentAccess"], PropertyInfo(alias="storageClass")]
    """Storage class for newly uploaded objects, unless specified otherwise."""
