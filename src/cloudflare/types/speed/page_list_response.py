# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .pages.test import Test
from .labeled_region import LabeledRegion

__all__ = ["PageListResponse"]


class PageListResponse(BaseModel):
    region: Optional[LabeledRegion] = None
    """A test region with a label."""

    schedule_frequency: Optional[Literal["DAILY", "WEEKLY"]] = FieldInfo(alias="scheduleFrequency", default=None)
    """The frequency of the test."""

    tests: Optional[List[Test]] = None

    url: Optional[str] = None
    """A URL."""
