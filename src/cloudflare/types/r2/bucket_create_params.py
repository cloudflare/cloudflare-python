# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BucketCreateParams"]


class BucketCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    name: Required[str]
    """Name of the bucket"""

    location_hint: Annotated[Literal["apac", "eeur", "enam", "weur", "wnam"], PropertyInfo(alias="locationHint")]
    """Location of the bucket"""
