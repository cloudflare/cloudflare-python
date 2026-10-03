# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["FeedEditResponse"]


class FeedEditResponse(BaseModel):
    id: str

    category_id: Optional[str] = None
    """Feed category identifier. Null when unset."""

    category_name: Optional[str] = None
    """Display name of the feed category. Null when unset or unresolvable."""

    created_at: str

    curated_feed_id: Optional[str] = None
    """Curated catalog feed this subscription was created from. Null for custom feeds."""

    display_name: Optional[str] = None

    enabled: bool

    last_polled_at: Optional[str] = None

    poll_interval_s: int

    source_type: str
    """`custom` for a feed added by URL, `curated` for a curated catalog feed."""

    status: str
    """Polling health: `active`, or `error` after a failed poll."""

    subscribed_at: Optional[str] = None

    title: Optional[str] = None

    updated_at: str

    url: str
