# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContentGetParams"]


class ContentGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    version_id: int
    """Specific version ID to retrieve. When omitted, the latest version is returned."""
