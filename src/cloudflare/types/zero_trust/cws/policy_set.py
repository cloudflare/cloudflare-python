# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["PolicySet", "Policy"]


class Policy(BaseModel):
    enforce: bool
    """Whether this policy should enforce when it matches.

    False keeps the policy attached for non-enforcing evaluation.
    """

    policy_id: str
    """ID of the member policy"""


class PolicySet(BaseModel):
    id: str
    """Server-assigned UUID"""

    created_at: datetime

    exclude_workload_ids: Optional[List[str]] = None
    """IDs of workloads that exclude matching requests. Exclusions take precedence."""

    include_workload_ids: Optional[List[str]] = None
    """IDs of workloads that include matching requests.

    Empty includes all requests before exclusions.
    """

    name: str
    """Human-readable name; unique per account"""

    policies: Optional[List[Policy]] = None
    """Member policies and their per-membership enforcement mode"""

    tags: Dict[str, str]
    """Tags attached to this policy set"""

    updated_at: datetime

    description: Optional[str] = None
    """Optional free-form description."""
