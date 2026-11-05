# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Deployment"]


class Deployment(BaseModel):
    id: str
    """Server-assigned UUID"""

    basic_auth_credential_ids: Optional[List[str]] = None
    """IDs of basic-auth credentials attached to this deployment"""

    created_at: datetime

    default_mode: Literal["ALLOW", "BLOCK"]
    """Default traffic decision when no policy set matches"""

    name: str
    """Human-readable name; unique per account"""

    on_error_action: Literal["BLOCK", "SKIP"]
    """Action applied when an enforcing policy has a runtime Rego error"""

    policy_set_ids: Optional[List[str]] = None
    """IDs of policy sets attached to this deployment"""

    rego_raise_error: bool
    """Whether OPA builtin failures are raised as runtime evaluation errors"""

    tags: Dict[str, str]
    """Tags attached to this deployment"""

    updated_at: datetime

    description: Optional[str] = None
    """Optional free-form description."""

    domain_acl_id: Optional[str] = None
    """ID of the attached domain ACL. Omitted when none."""
