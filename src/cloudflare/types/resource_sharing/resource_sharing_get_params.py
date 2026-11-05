# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResourceSharingGetParams"]


class ResourceSharingGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier."""

    include_recipient_counts: bool
    """Include recipient counts in the response."""

    include_resources: bool
    """Include resources in the response."""

    include_tags_from: Literal["api", "mirror"]
    """Include share tags in the response.

    `api` reads tags from the tag service; `mirror` reads a local, eventually
    consistent replica. If the tag lookup fails, the response omits `tags`.
    """
