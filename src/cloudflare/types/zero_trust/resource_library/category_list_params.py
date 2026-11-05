# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CategoryListParams"]


class CategoryListParams(TypedDict, total=False):
    account_id: Required[str]

    cursor: str
    """Opaque value from `result_info.cursor` of the previous response.

    Returns the categories that follow it. `limit` may change between requests. An
    empty value is the same as no cursor. A modified cursor, or one returned by a
    different list, returns `400`.
    """

    limit: int
    """Number of results to return. Defaults to 25; values are clamped to 1–250."""

    offset: int
    """Number of results to skip.

    Defaults to 0; negative values are clamped to 0. Ignored when `cursor` is
    provided.
    """
