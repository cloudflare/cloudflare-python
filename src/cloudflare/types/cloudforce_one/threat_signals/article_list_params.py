# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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

    feed_id: str

    fetched_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    fetched_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    include_total: bool

    per_page: int

    published_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    published_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    read: bool

    search: str

    sort: str

    source_type: Literal["curated", "custom"]

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
