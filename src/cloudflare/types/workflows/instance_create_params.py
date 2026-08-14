# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceCreateParams", "InstanceRetention"]


class InstanceCreateParams(TypedDict, total=False):
    account_id: Required[str]

    instance_id: str
    """
    An id of exactly `cf_` followed by 64 lowercase hex characters is reserved for
    system-generated instances.
    """

    instance_retention: InstanceRetention

    location_hint: Literal["wnam", "weur", "enam", "eeur", "apac", "oc", "sam", "afr", "me"]

    params: str
    """JSON-encoded event payload passed into the new instance."""


class InstanceRetention(TypedDict, total=False):
    error_retention: Union[int, str]
    """Specifies the duration in milliseconds or as a string like '5 minutes'."""

    success_retention: Union[int, str]
    """Specifies the duration in milliseconds or as a string like '5 minutes'."""
