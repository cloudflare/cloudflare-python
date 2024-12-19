# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..decision import Decision
from ...access_rule_param import AccessRuleParam

__all__ = ["PolicyTestCreateParams"]


class PolicyTestCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    id: str
    """The UUID of the policy"""

    decision: Decision
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Iterable[AccessRuleParam]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: str
    """The name of the Access policy."""

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """
