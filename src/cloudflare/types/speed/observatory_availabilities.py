# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObservatoryAvailabilities", "Quota", "Region"]


class Quota(BaseModel):
    plan: Optional[str] = None
    """Cloudflare plan."""

    quotas_per_plan: Optional[Dict[str, float]] = FieldInfo(alias="quotasPerPlan", default=None)
    """The number of tests available per plan."""

    remaining_schedules: Optional[float] = FieldInfo(alias="remainingSchedules", default=None)
    """The number of remaining schedules available."""

    remaining_tests: Optional[float] = FieldInfo(alias="remainingTests", default=None)
    """The number of remaining tests available."""

    schedule_quotas_per_plan: Optional[Dict[str, float]] = FieldInfo(alias="scheduleQuotasPerPlan", default=None)
    """The number of schedules available per plan."""


class Region(BaseModel):
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


class ObservatoryAvailabilities(BaseModel):
    quota: Optional[Quota] = None

    regions: Optional[List[Region]] = None

    regions_per_plan: Optional[object] = FieldInfo(alias="regionsPerPlan", default=None)
