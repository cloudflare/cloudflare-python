# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    account_id: Required[str]

    image: str
    """Filter applications by image."""

    name: str
    """Filter applications by name."""

    page_token: str
    """Opaque token from a previous response to retrieve the next page."""

    per_page: int
    """Maximum number of applications to return per page.

    Defaults to all, or 100 when `page_token` is set.
    """
