# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .decision import Decision
from ..access_rule_param import AccessRuleParam

__all__ = ["PolicyUpdateParams"]


class PolicyUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    decision: Required[Decision]
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """
