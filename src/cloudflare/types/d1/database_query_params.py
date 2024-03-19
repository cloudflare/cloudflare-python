# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["DatabaseQueryParams"]


class DatabaseQueryParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Account identifier tag."""

    sql: Required[str]

    params: List[str]
