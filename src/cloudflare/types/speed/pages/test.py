# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..labeled_region import LabeledRegion
from ..lighthouse_report import LighthouseReport

__all__ = ["Test"]


class Test(BaseModel):
    __test__ = False
    id: Optional[str] = None
    """UUID"""

    date: Optional[datetime] = None

    desktop_report: Optional[LighthouseReport] = FieldInfo(alias="desktopReport", default=None)
    """The Lighthouse report."""

    mobile_report: Optional[LighthouseReport] = FieldInfo(alias="mobileReport", default=None)
    """The Lighthouse report."""

    region: Optional[LabeledRegion] = None
    """A test region with a label."""

    schedule_frequency: Optional[Literal["DAILY", "WEEKLY"]] = FieldInfo(alias="scheduleFrequency", default=None)
    """The frequency of the test."""

    url: Optional[str] = None
    """A URL."""
