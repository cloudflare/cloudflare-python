# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConfigListParams"]


class ConfigListParams(TypedDict, total=False):
    account_id: Required[str]
    """Define configurations using a unique string identifier."""

    page: int
    """Page number of paginated results."""

    per_page: int
    """Maximum number of results per page."""
