# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["DatabaseRawParams"]


class DatabaseRawParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    sql: Required[str]
    """Your SQL query.

    Supports multiple statements, joined by semicolons, which will be executed as a
    batch.
    """

    params: List[str]
