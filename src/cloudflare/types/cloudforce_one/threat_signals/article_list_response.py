# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ArticleListResponse", "Article", "ArticleTag"]


class ArticleTag(BaseModel):
    applied_by: Literal["ai", "analyst", "system"]

    category_id: Optional[str] = FieldInfo(alias="categoryId", default=None)

    uuid: str

    value: str


class Article(BaseModel):
    id: str

    dataset_id: Optional[str] = None
    """Threat Events dataset identifier for the article redirect.

    Null when the account feeds dataset mapping is unavailable.
    """

    event_id: Optional[str] = None
    """Threat Events event identifier associated with this article for a UI redirect.

    Null when no event has been linked.
    """

    feed_display_name: Optional[str] = None

    feed_id: str

    fetched_at: str

    link: Optional[str] = None

    published_at: Optional[str] = None

    read: bool

    read_at: Optional[str] = None

    summary: Optional[str] = None
    """Persisted enrichment summary. Null until enrichment produces a summary."""

    tags: List[ArticleTag]

    title: Optional[str] = None


class ArticleListResponse(BaseModel):
    articles: List[Article]

    has_more: bool

    next_cursor: Optional[str] = None

    total_count: Optional[float] = None

    total_count_is_exact: bool
