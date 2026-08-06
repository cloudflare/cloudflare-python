# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["URL", "ContentCategory", "RiskType"]


class ContentCategory(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    source_id: Optional[int] = None

    super_category_id: Optional[int] = None


class RiskType(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    source_id: Optional[int] = None

    super_category_id: Optional[int] = None


class URL(BaseModel):
    content_categories: List[ContentCategory]
    """Content categories associated with this URL."""

    full_url: str
    """The full URL that was looked up."""

    hostname: str
    """The hostname of the URL."""

    risk_type: List[RiskType]
    """Security risk types associated with this URL."""

    url_path: str
    """The path component of the URL."""
