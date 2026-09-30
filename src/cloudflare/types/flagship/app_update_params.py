# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AppUpdateParams"]


class AppUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID that owns the Flagship app."""

    name: str
    """Name of the Flagship app (1–64 letters, numbers, hyphens, or underscores)."""
