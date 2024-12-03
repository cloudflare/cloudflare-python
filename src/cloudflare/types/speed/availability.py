# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .labeled_region import LabeledRegion

__all__ = [
    "Availability",
    "Quota",
    "QuotaQuotasPerPlan",
    "QuotaQuotasPerPlanValue",
    "QuotaScheduleQuotasPerPlan",
    "QuotaScheduleQuotasPerPlanValue",
    "RegionsPerPlan",
]


class QuotaQuotasPerPlanValue(BaseModel):
    business: Optional[int] = None

    enterprise: Optional[int] = None

    free: Optional[int] = None

    pro: Optional[int] = None


class QuotaQuotasPerPlan(BaseModel):
    value: Optional[QuotaQuotasPerPlanValue] = None
    """Counts per account plan."""


class QuotaScheduleQuotasPerPlanValue(BaseModel):
    business: Optional[int] = None

    enterprise: Optional[int] = None

    free: Optional[int] = None

    pro: Optional[int] = None


class QuotaScheduleQuotasPerPlan(BaseModel):
    value: Optional[QuotaScheduleQuotasPerPlanValue] = None
    """Counts per account plan."""


class Quota(BaseModel):
    plan: Optional[str] = None
    """Cloudflare plan."""

    quotas_per_plan: Optional[QuotaQuotasPerPlan] = FieldInfo(alias="quotasPerPlan", default=None)
    """The number of tests available per plan."""

    remaining_schedules: Optional[float] = FieldInfo(alias="remainingSchedules", default=None)
    """The number of remaining schedules available."""

    remaining_tests: Optional[float] = FieldInfo(alias="remainingTests", default=None)
    """The number of remaining tests available."""

    schedule_quotas_per_plan: Optional[QuotaScheduleQuotasPerPlan] = FieldInfo(
        alias="scheduleQuotasPerPlan", default=None
    )
    """The number of schedules available per plan."""


class RegionsPerPlan(BaseModel):
    business: Optional[List[LabeledRegion]] = None

    enterprise: Optional[List[LabeledRegion]] = None

    free: Optional[List[LabeledRegion]] = None

    pro: Optional[List[LabeledRegion]] = None


class Availability(BaseModel):
    quota: Optional[Quota] = None

    regions: Optional[List[LabeledRegion]] = None

    regions_per_plan: Optional[RegionsPerPlan] = FieldInfo(alias="regionsPerPlan", default=None)
    """Available regions."""
