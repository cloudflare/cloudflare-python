# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel
from ...access_rule import AccessRule
from .approval_group import ApprovalGroup

__all__ = ["Policy"]


class Policy(BaseModel):
    id: Optional[str] = None
    """UUID"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy. Must be unique for each policy."""

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None
