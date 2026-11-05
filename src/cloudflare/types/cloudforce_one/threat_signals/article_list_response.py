# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ArticleListResponse", "Article", "ArticleRelevance", "ArticleRelevancePir", "ArticleTag"]


class ArticleRelevancePir(BaseModel):
    band: Literal["low", "medium", "high"]
    """Beta.

    How relevant the article is to a Priority Intelligence Requirement: high,
    medium, or low. Cloudflare may change the scores behind each band as relevance
    scoring is calibrated.
    """

    pir_id: str


class ArticleRelevance(BaseModel):
    """Beta.

    The article's relevance to the account's active Priority Intelligence Requirements. Null when the article has not been scored against them, including when the account has no active PIRs, or has not been scored against the requested pir_id.
    """

    band: Literal["low", "medium", "high"]
    """Beta.

    How relevant the article is to a Priority Intelligence Requirement: high,
    medium, or low. Cloudflare may change the scores behind each band as relevance
    scoring is calibrated.
    """

    pir_id: str
    """Beta.

    The pir_id requested from the article list, or otherwise the account's most
    relevant active PIR for this article.
    """

    pirs: List[ArticleRelevancePir]
    """Beta.

    Every active PIR the article was scored against, most relevant first. Draft and
    deleted PIRs are excluded.
    """


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

    relevance: Optional[ArticleRelevance] = None
    """Beta.

    The article's relevance to the account's active Priority Intelligence
    Requirements. Null when the article has not been scored against them, including
    when the account has no active PIRs, or has not been scored against the
    requested pir_id.
    """

    severity: Optional[Literal["informational", "low", "medium", "high", "critical"]] = None
    """Beta.

    Intrinsic article severity band, from informational to critical, independent of
    any organisation or Priority Intelligence Requirement. Null when the account has
    no active Priority Intelligence Requirements, scoring has not completed, or a
    historic article has not entered an automatic rescore window.
    """

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
