# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["RatePlanParam"]


class RatePlanParam(TypedDict, total=False):
    id: str
    """The ID of the rate plan."""

    currency: str
    """The currency applied to the rate plan subscription."""

    externally_managed: bool
    """Whether this rate plan is managed externally from Cloudflare."""

    is_contract: bool
    """Whether a rate plan is enterprise-based (or newly adopted term contract)."""

    public_name: str
    """The full name of the rate plan."""

    scope: str
    """The scope that this rate plan applies to."""

    sets: List[str]
    """The list of sets this rate plan applies to."""
