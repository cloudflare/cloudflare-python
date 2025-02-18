# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RatePlan"]


class RatePlan(BaseModel):
    id: Optional[
        Literal[
            "free",
            "lite",
            "pro",
            "pro_plus",
            "business",
            "enterprise",
            "partners_free",
            "partners_pro",
            "partners_business",
            "partners_enterprise",
        ]
    ] = None
    """The ID of the rate plan."""

    currency: Optional[str] = None
    """The currency applied to the rate plan subscription."""

    externally_managed: Optional[bool] = None
    """Whether this rate plan is managed externally from Cloudflare."""

    is_contract: Optional[bool] = None
    """Whether a rate plan is enterprise-based (or newly adopted term contract)."""

    public_name: Optional[str] = None
    """The full name of the rate plan."""

    scope: Optional[str] = None
    """The scope that this rate plan applies to."""

    sets: Optional[List[str]] = None
    """The list of sets this rate plan applies to."""
