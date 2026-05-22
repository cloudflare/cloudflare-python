# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RecipientListParams"]


class RecipientListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier."""

    include_resources: bool
    """Include resources in the response."""

    page: int
    """Page number.

    Defaults to `1` when `per_page` is supplied without `page`. May be omitted
    entirely along with `per_page` to receive a non-paginated response.
    """

    per_page: int
    """Number of objects to return per page.

    Defaults to `20` when `page` is supplied without `per_page`. May be omitted
    entirely along with `page` to receive a non-paginated response.
    """
