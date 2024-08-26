# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Schedule"]


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
