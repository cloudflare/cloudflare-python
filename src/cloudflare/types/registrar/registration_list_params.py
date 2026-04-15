# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RegistrationListParams"]


class RegistrationListParams(TypedDict, total=False):
    account_id: str
    """Identifier"""

    cursor: str
    """
    Opaque token from a previous response's `result_info.cursor`. Pass this value to
    fetch the next page of results. Omit (or pass an empty string) for the first
    page.
    """

    direction: Literal["asc", "desc"]
    """Sort direction for results. Defaults to ascending order."""

    per_page: int
    """Number of items to return per page."""

    sort_by: Literal["registry_created_at", "registry_expires_at", "name"]
    """Column to sort results by.

    Defaults to registration date (`registry_created_at`) when omitted.
    """
