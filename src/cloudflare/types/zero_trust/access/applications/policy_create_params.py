# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ...exclude_item_param import ExcludeItemParam
from ...include_item_param import IncludeItemParam
from ...require_item_param import RequireItemParam
from .approval_group_item_param import ApprovalGroupItemParam

__all__ = ["PolicyCreateParams"]


class PolicyCreateParams(TypedDict, total=False):
    decision: Required[Literal["allow", "deny", "non_identity", "bypass"]]
    """The action Access will take if a user matches this policy."""

    include: Required[Iterable[IncludeItemParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    approval_groups: Iterable[ApprovalGroupItemParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    exclude: Iterable[ExcludeItemParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    precedence: int
    """The order of execution for this policy. Must be unique for each policy."""

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    require: Iterable[RequireItemParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """
