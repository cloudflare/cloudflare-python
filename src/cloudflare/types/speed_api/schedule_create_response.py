# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "ScheduleCreateResponse",
    "Schedule",
    "Test",
    "TestDesktopReport",
    "TestDesktopReportError",
    "TestMobileReport",
    "TestMobileReportError",
    "TestRegion",
]


class Schedule(BaseModel):
    frequency: Optional[Literal["DAILY", "WEEKLY"]] = None
    """The frequency of the test."""

    region: Optional[
        Literal[
            "asia-east1",
            "asia-northeast1",
            "asia-northeast2",
            "asia-south1",
            "asia-southeast1",
            "australia-southeast1",
            "europe-north1",
            "europe-southwest1",
            "europe-west1",
            "europe-west2",
            "europe-west3",
            "europe-west4",
            "europe-west8",
            "europe-west9",
            "me-west1",
            "southamerica-east1",
            "us-central1",
            "us-east1",
            "us-east4",
            "us-south1",
            "us-west1",
        ]
    ] = None
    """A test region."""

    url: Optional[str] = None
    """A URL."""


class TestDesktopReportError(BaseModel):
    __test__ = False
    code: Optional[Literal["NOT_REACHABLE", "DNS_FAILURE", "NOT_HTML", "LIGHTHOUSE_TIMEOUT", "UNKNOWN"]] = None
    """The error code of the Lighthouse result."""

    detail: Optional[str] = None
    """Detailed error message."""

    final_displayed_url: Optional[str] = FieldInfo(alias="finalDisplayedUrl", default=None)
    """The final URL displayed to the user."""


class TestDesktopReport(BaseModel):
    __test__ = False
    cls: Optional[float] = None
    """Cumulative Layout Shift."""

    device_type: Optional[Literal["DESKTOP", "MOBILE"]] = FieldInfo(alias="deviceType", default=None)
    """The type of device."""

    error: Optional[TestDesktopReportError] = None

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


class TestMobileReportError(BaseModel):
    __test__ = False
    code: Optional[Literal["NOT_REACHABLE", "DNS_FAILURE", "NOT_HTML", "LIGHTHOUSE_TIMEOUT", "UNKNOWN"]] = None
    """The error code of the Lighthouse result."""

    detail: Optional[str] = None
    """Detailed error message."""

    final_displayed_url: Optional[str] = FieldInfo(alias="finalDisplayedUrl", default=None)
    """The final URL displayed to the user."""


class TestMobileReport(BaseModel):
    __test__ = False
    cls: Optional[float] = None
    """Cumulative Layout Shift."""

    device_type: Optional[Literal["DESKTOP", "MOBILE"]] = FieldInfo(alias="deviceType", default=None)
    """The type of device."""

    error: Optional[TestMobileReportError] = None

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


class TestRegion(BaseModel):
    __test__ = False
    label: Optional[str] = None

    value: Optional[
        Literal[
            "asia-east1",
            "asia-northeast1",
            "asia-northeast2",
            "asia-south1",
            "asia-southeast1",
            "australia-southeast1",
            "europe-north1",
            "europe-southwest1",
            "europe-west1",
            "europe-west2",
            "europe-west3",
            "europe-west4",
            "europe-west8",
            "europe-west9",
            "me-west1",
            "southamerica-east1",
            "us-central1",
            "us-east1",
            "us-east4",
            "us-south1",
            "us-west1",
        ]
    ] = None
    """A test region."""


class Test(BaseModel):
    __test__ = False
    id: Optional[str] = None
    """UUID"""

    date: Optional[datetime] = None

    desktop_report: Optional[TestDesktopReport] = FieldInfo(alias="desktopReport", default=None)
    """The Lighthouse report."""

    mobile_report: Optional[TestMobileReport] = FieldInfo(alias="mobileReport", default=None)
    """The Lighthouse report."""

    region: Optional[TestRegion] = None
    """A test region with a label."""

    schedule_frequency: Optional[Literal["DAILY", "WEEKLY"]] = FieldInfo(alias="scheduleFrequency", default=None)
    """The frequency of the test."""

    url: Optional[str] = None
    """A URL."""


class ScheduleCreateResponse(BaseModel):
    schedule: Optional[Schedule] = None
    """The test schedule."""

    test: Optional[Test] = None
