# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ArticleGetResponse", "BulletPoints", "Tag"]


class BulletPoints(BaseModel):
    impact: str

    what_happened: str

    who_affected: str


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

    source_count: float

    summary: Optional[str] = None
    """Persisted enrichment summary. Null until enrichment produces a summary."""

    summary_r2_key: Optional[str] = None

    tags: List[Tag]

    title: Optional[str] = None

    skill_version: Optional[str] = None

    tag_skill_version: Optional[str] = None
