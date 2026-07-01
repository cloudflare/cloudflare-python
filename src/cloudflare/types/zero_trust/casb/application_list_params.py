# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    account_id: Required[str]

    environment: str
    """Filter by supported environment (standard, fedramp)."""
