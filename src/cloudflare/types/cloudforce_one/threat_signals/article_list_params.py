# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ArticleListParams"]


class ArticleListParams(TypedDict, total=False):
    account_id: Required[str]

    article_id: SequenceNotStr[str]
    """Repeatable article UUID filter.

    Returns the union of matching account-owned articles; use this to list every
    Threat Signals article referenced by an indicator's sources.
    """

    cursor: str
    """Opaque cursor from a previous response's `next_cursor`.

    When provided, pagination, ordering, totals, and article filters come from the
    cursor. Sending `per_page`, `sort`, `include_total`, or any article filter
    alongside it returns a 400 `CursorFilterConflictError`.
    """

    feed_category: str
    """Exact feed-category filter after trimming. Omit to include every category."""

    feed_id: str
    """Feed UUID filter. Omit to include articles from every account feed."""

    fetched_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Include articles fetched at or after this ISO 8601 date-time with Z or a numeric
    UTC offset; normalized to UTC.
    """

    fetched_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Include articles fetched at or before this ISO 8601 date-time with Z or a
    numeric UTC offset; normalized to UTC.
    """

    include_total: bool
    """When true on the first page, count matching articles and return an exact total.

    Defaults to false; cursor pages do not recalculate totals.
    """

    min_relevance: Literal["low", "medium", "high"]
    """Beta.

    Return only articles at or above this relevance band for pir_id, or for any
    active PIR when pir_id is omitted. Excludes articles that have not been scored.
    """

    per_page: int
    """Number of articles per cursor page, from 1 to 100. Defaults to 20."""

    pir_id: str
    """Beta.

    Active Priority Intelligence Requirement to report, filter, and sort relevance
    by. Omit to use each article's most relevant active PIR. Returns a 400 error
    unless the PIR is active.
    """

    published_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Include articles published at or after this ISO 8601 date-time with Z or a
    numeric UTC offset; normalized to UTC.
    """

    published_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Include articles published at or before this ISO 8601 date-time with Z or a
    numeric UTC offset; normalized to UTC.
    """

    read: bool
    """Filter by read state.

    Accepts true, false, 1, or 0; omit to include read and unread articles.
    """

    search: str
    """
    NFC-normalized, trimmed literal substring filter on article titles; ASCII
    case-insensitive, from 1 to 500 characters.
    """

    severity: List[Literal["informational", "low", "medium", "high", "critical"]]
    """Beta.

    Repeatable intrinsic severity band filter. An article matches any selected band,
    the band reported as its severity. Excludes articles without a severity. Like
    the severity field, severity is reported only while the account has an active
    Priority Intelligence Requirement; otherwise no articles match.
    """

    sort: str
    """Sort by fetched_at, published_at, title, or relevance (beta).

    Prefix the field with - for descending order; defaults to -fetched_at.
    -relevance lists the most relevant articles first, by pir_id or by each
    article's most relevant active PIR, with unscored articles last.
    """

    source_type: Literal["curated", "custom"]
    """Filter by curated or custom feed source. Omit to include both source types."""

    tag: str
    """Legacy human-readable tag-value filter.

    Ignored when tag_id is supplied; prefer tag_id.
    """

    tag_applied_by: Literal["ai", "analyst", "system"]
    """Assignment provenance filter.

    When combined with tag_id or tag_category_id, the matching assignment must have
    this provenance.
    """

    tag_category: str
    """Legacy category-name disambiguator for tag.

    It has no effect without tag; prefer tag_category_id.
    """

    tag_category_id: SequenceNotStr[str]
    """Repeatable tag-category UUID filter.

    An article matches any selected category; when tag_id is also present, the tag
    and category groups are ANDed.
    """

    tag_id: SequenceNotStr[str]
    """Repeatable tag UUID filter. An article matches any selected tag."""
