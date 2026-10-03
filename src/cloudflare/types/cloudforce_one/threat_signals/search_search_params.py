# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchSearchParams"]


class SearchSearchParams(TypedDict, total=False):
    account_id: Required[str]

    query: Required[str]

    feed_id: str

    max_results: Union[Literal[""], str]
