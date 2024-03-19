# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PageShieldPageshieldPolicy"]


class PageShieldPageshieldPolicy(BaseModel):
    id: Optional[str] = None
    """The ID of the policy"""

    action: Optional[Literal["allow", "log"]] = None
    """The action to take if the expression matches"""

    description: Optional[str] = None
    """A description for the policy"""

    enabled: Optional[bool] = None
    """Whether the policy is enabled"""

    expression: Optional[str] = None
    """
    The expression which must match for the policy to be applied, using the
    Cloudflare Firewall rule expression syntax
    """

    value: Optional[str] = None
    """The policy which will be applied"""
