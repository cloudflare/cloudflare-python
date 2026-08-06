# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceBulkParams", "Body", "BodyInstanceRetention"]


class InstanceBulkParams(TypedDict, total=False):
    account_id: Required[str]

    body: Iterable[Body]


class BodyInstanceRetention(TypedDict, total=False):
    error_retention: Union[int, str]
    """Specifies the duration in milliseconds or as a string like '5 minutes'."""

    success_retention: Union[int, str]
    """Specifies the duration in milliseconds or as a string like '5 minutes'."""


class Body(TypedDict, total=False):
    instance_id: str

    instance_retention: BodyInstanceRetention

    location_hint: Literal["wnam", "weur", "enam", "eeur", "apac", "oc", "sam", "afr", "me"]

    params: str
    """JSON-encoded event payload passed into the new instance."""
