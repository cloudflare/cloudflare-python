# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScheduleCreateParams"]


class ScheduleCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    region: Literal[
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
    """A test region."""
