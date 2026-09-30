# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NamespaceListParams"]


class NamespaceListParams(TypedDict, total=False):
    account_id: Required[str]
    """ID of the Cloudflare account that owns the Workers KV namespaces."""

    direction: Literal["asc", "desc"]
    """Sort namespaces in ascending (`asc`) or descending (`desc`) order."""

    order: Literal["id", "title"]
    """Namespace field to sort by (`id` or `title`)."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""
