# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PrefixListParams"]


class PrefixListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    direction: str
    """The direction of ordering (ASC or DESC). Defaults to 'ASC'."""

    order: str
    """The field to order by. Defaults to 'prefix'."""

    page: int
    """The page number for pagination. Defaults to 1."""

    per_page: int
    """The number of items per page. Must be between 10 and 1000. Defaults to 25."""
