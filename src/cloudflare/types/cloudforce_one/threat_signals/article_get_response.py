# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ArticleGetResponse", "BulletPoints", "Relevance", "RelevancePir", "Tag"]


class BulletPoints(BaseModel):
    impact: str

    what_happened: str

    who_affected: str


class RelevancePir(BaseModel):
    band: Literal["low", "medium", "high"]
    """Beta.

    How relevant the article is to a Priority Intelligence Requirement: high,
    medium, or low. Cloudflare may change the scores behind each band as relevance
    scoring is calibrated.
    """

    pir_id: str


class Relevance(BaseModel):
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

    pirs: List[RelevancePir]
    """Beta.

    Every active PIR the article was scored against, most relevant first. Draft and
    deleted PIRs are excluded.
    """


class Tag(BaseModel):
    applied_by: Literal["ai", "analyst", "system"]

    category_id: Optional[str] = FieldInfo(alias="categoryId", default=None)

    uuid: str

    value: str


class ArticleGetResponse(BaseModel):
    id: str

    bullet_points: Optional[BulletPoints] = None

    content_r2_key: Optional[str] = None

    feed_display_name: Optional[str] = None

    feed_id: str

    fetched_at: str

    indicator_extraction_status: Literal["in_progress", "complete", "failed", "unknown"]
    """Progress of the article's indicator extraction and IOC contextualization run.

    complete and failed are terminal; unknown means no run has been recorded.
    """

    link: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    published_at: Optional[str] = None

    read: bool

    read_at: Optional[str] = None

    relevance: Optional[Relevance] = None
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

    source_count: float

    summary: Optional[str] = None
    """Persisted enrichment summary. Null until enrichment produces a summary."""

    summary_r2_key: Optional[str] = None

    tags: List[Tag]

    title: Optional[str] = None

    skill_version: Optional[str] = None

    tag_skill_version: Optional[str] = None
