# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceCreateParams", "InstanceRetention"]


class InstanceCreateParams(TypedDict, total=False):
    account_id: Required[str]

    instance_id: str
    """
    The system reserves IDs that consist of the `cf_` prefix and exactly 64
    lowercase hexadecimal characters.
    """

    instance_retention: InstanceRetention

    location_hint: Literal["wnam", "weur", "enam", "eeur", "apac", "apac-ne", "apac-se", "oc", "sam", "afr", "me"]

    params: str
    """JSON-encoded event payload passed into the new instance."""


class InstanceRetention(TypedDict, total=False):
    error_retention: Union[int, str]
    """Specifies the duration in milliseconds or as a string like '5 minutes'."""

    success_retention: Union[int, str]
    """Specifies the duration in milliseconds or as a string like '5 minutes'."""
