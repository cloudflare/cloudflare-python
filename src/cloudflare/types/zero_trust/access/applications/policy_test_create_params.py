# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from ..decision import Decision
from ...access_rule_param import AccessRuleParam
from .approval_group_param import ApprovalGroupParam

__all__ = ["PolicyTestCreateParams", "ConnectionRules", "ConnectionRulesSSH"]


class PolicyTestCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: ConnectionRules
    """
    The rules that define how users may connect to the targets secured by your
    application.
    """

    decision: Decision
    """The action Access will take if a user matches this policy."""

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Iterable[AccessRuleParam]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    name: str
    """The name of the Access policy."""

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class ConnectionRulesSSH(TypedDict, total=False):
    usernames: Required[List[str]]
    """Contains the Unix usernames that may be used when connecting over SSH."""


class ConnectionRules(TypedDict, total=False):
    ssh: ConnectionRulesSSH
    """
    The SSH-specific rules that define how users may connect to the targets secured
    by your application.
    """
