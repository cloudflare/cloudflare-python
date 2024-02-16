# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["SpeedAPITestsListParams"]


class SpeedAPITestsListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    page: int

    per_page: int

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
