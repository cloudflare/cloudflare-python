# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .observatory_page_test import ObservatoryPageTest

__all__ = ["PageListResponse", "PageListResponseItem", "PageListResponseItemRegion"]


class PageListResponseItemRegion(BaseModel):
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


class PageListResponseItem(BaseModel):
    region: Optional[PageListResponseItemRegion] = None
    """A test region with a label."""

    schedule_frequency: Optional[Literal["DAILY", "WEEKLY"]] = FieldInfo(alias="scheduleFrequency", default=None)
    """The frequency of the test."""

    tests: Optional[List[ObservatoryPageTest]] = None

    url: Optional[str] = None
    """A URL."""


PageListResponse = List[PageListResponseItem]
