# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ResourceSharingGetParams"]


class ResourceSharingGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier."""

    include_recipient_counts: bool
    """Include recipient counts in the response."""

    include_resources: bool
    """Include resources in the response."""
