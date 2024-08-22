# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LighthouseReport", "Error"]


class Error(BaseModel):
    code: Optional[Literal["NOT_REACHABLE", "DNS_FAILURE", "NOT_HTML", "LIGHTHOUSE_TIMEOUT", "UNKNOWN"]] = None
    """The error code of the Lighthouse result."""

    detail: Optional[str] = None
    """Detailed error message."""

    final_displayed_url: Optional[str] = FieldInfo(alias="finalDisplayedUrl", default=None)
    """The final URL displayed to the user."""


class LighthouseReport(BaseModel):
    cls: Optional[float] = None
    """Cumulative Layout Shift."""

    device_type: Optional[Literal["DESKTOP", "MOBILE"]] = FieldInfo(alias="deviceType", default=None)
    """The type of device."""

    error: Optional[Error] = None

    fcp: Optional[float] = None
    """First Contentful Paint."""

    json_report_url: Optional[str] = FieldInfo(alias="jsonReportUrl", default=None)
    """The URL to the full Lighthouse JSON report."""

    lcp: Optional[float] = None
    """Largest Contentful Paint."""

    performance_score: Optional[float] = FieldInfo(alias="performanceScore", default=None)
    """The Lighthouse performance score."""

    si: Optional[float] = None
    """Speed Index."""

    state: Optional[Literal["RUNNING", "COMPLETE", "FAILED"]] = None
    """The state of the Lighthouse report."""

    tbt: Optional[float] = None
    """Total Blocking Time."""

    ttfb: Optional[float] = None
    """Time To First Byte."""

    tti: Optional[float] = None
    """Time To Interactive."""
