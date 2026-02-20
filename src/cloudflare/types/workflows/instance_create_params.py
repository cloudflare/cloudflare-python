# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["InstanceCreateParams", "InstanceRetention"]


class InstanceCreateParams(TypedDict, total=False):
    account_id: Required[str]

    instance_id: str

    instance_retention: InstanceRetention

    params: object


class InstanceRetention(TypedDict, total=False):
    error_retention: Union[int, str]
    """Specifies the duration in milliseconds or as a string like '5 minutes'."""

    success_retention: Union[int, str]
    """Specifies the duration in milliseconds or as a string like '5 minutes'."""
