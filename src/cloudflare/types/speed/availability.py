# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .labeled_region import LabeledRegion

__all__ = ["Availability", "Quota"]


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


class Availability(BaseModel):
    quota: Optional[Quota] = None

    regions: Optional[List[LabeledRegion]] = None

    regions_per_plan: Optional[object] = FieldInfo(alias="regionsPerPlan", default=None)
