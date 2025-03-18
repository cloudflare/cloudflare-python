# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["InstanceBulkParams", "Body"]


class InstanceBulkParams(TypedDict, total=False):
    account_id: Required[str]

    body: Iterable[Body]


class Body(TypedDict, total=False):
    instance_id: str

    params: object
