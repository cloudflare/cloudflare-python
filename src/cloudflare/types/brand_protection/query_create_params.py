# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["QueryCreateParams", "StringMatch"]


class QueryCreateParams(TypedDict, total=False):
    account_id: Required[str]

    id: str

    query_scan: Annotated[bool, PropertyInfo(alias="scan")]

    query_tag: Annotated[str, PropertyInfo(alias="tag")]

    max_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    min_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    body_scan: Annotated[bool, PropertyInfo(alias="scan")]

    string_matches: Iterable[StringMatch]

    body_tag: Annotated[str, PropertyInfo(alias="tag")]


class StringMatch(TypedDict, total=False):
    pattern: Required[str]

    max_edit_distance: float
