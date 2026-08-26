# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SuppressionImportParams", "Item"]


class SuppressionImportParams(TypedDict, total=False):
    account_id: Required[str]

    items: Required[Iterable[Item]]


class Item(TypedDict, total=False):
    email: Required[str]

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    note: str
