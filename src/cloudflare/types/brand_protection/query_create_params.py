# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["QueryCreateParams"]


class QueryCreateParams(TypedDict, total=False):
    account_id: Required[str]

    id: str

    query_scan: Annotated[bool, PropertyInfo(alias="scan")]

    query_tag: Annotated[str, PropertyInfo(alias="tag")]

    max_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    min_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    body_scan: Annotated[bool, PropertyInfo(alias="scan")]

    string_matches: object

    body_tag: Annotated[str, PropertyInfo(alias="tag")]
