# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["DatabaseRawParams", "D1SingleQuery", "MultipleQueries", "MultipleQueriesBatch"]


class D1SingleQuery(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    sql: Required[str]
    """Your SQL query.

    Supports multiple statements, joined by semicolons, which will be executed as a
    batch.
    """

    params: SequenceNotStr[str]


class MultipleQueries(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    batch: Iterable[MultipleQueriesBatch]


class MultipleQueriesBatch(TypedDict, total=False):
    """A single query with or without parameters"""

    sql: Required[str]
    """Your SQL query.

    Supports multiple statements, joined by semicolons, which will be executed as a
    batch.
    """

    params: SequenceNotStr[str]


DatabaseRawParams: TypeAlias = Union[D1SingleQuery, MultipleQueries]
