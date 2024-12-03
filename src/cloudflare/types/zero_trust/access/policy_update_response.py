# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .decision import Decision
from ...._models import BaseModel
from ..access_rule import AccessRule

__all__ = ["PolicyUpdateResponse"]


class PolicyUpdateResponse(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Optional[str] = None
    """The name of the Access policy."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    updated_at: Optional[datetime] = None
