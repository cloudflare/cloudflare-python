# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Trend"]


class Trend(BaseModel):
    cls: Optional[List[Optional[float]]] = None
    """Cumulative Layout Shift trend."""

    fcp: Optional[List[Optional[float]]] = None
    """First Contentful Paint trend."""

    lcp: Optional[List[Optional[float]]] = None
    """Largest Contentful Paint trend."""

    performance_score: Optional[List[Optional[float]]] = FieldInfo(alias="performanceScore", default=None)
    """The Lighthouse score trend."""

    si: Optional[List[Optional[float]]] = None
    """Speed Index trend."""

    tbt: Optional[List[Optional[float]]] = None
    """Total Blocking Time trend."""

    ttfb: Optional[List[Optional[float]]] = None
    """Time To First Byte trend."""

    tti: Optional[List[Optional[float]]] = None
    """Time To Interactive trend."""
