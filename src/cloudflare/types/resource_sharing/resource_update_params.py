# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ResourceUpdateParams"]


class ResourceUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier."""

    share_id: Required[str]
    """Share identifier tag."""

    meta: Required[object]
    """Resource Metadata."""
