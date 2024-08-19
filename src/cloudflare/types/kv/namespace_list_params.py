# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NamespaceListParams"]


class NamespaceListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    direction: Literal["asc", "desc"]
    """Direction to order namespaces."""

    order: Literal["id", "title"]
    """Field to order results by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""
