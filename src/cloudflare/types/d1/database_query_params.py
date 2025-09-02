# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["DatabaseQueryParams"]


class DatabaseQueryParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    sql: Required[str]
    """Your SQL query.

    Supports multiple statements, joined by semicolons, which will be executed as a
    batch.
    """

    params: SequenceNotStr[str]
