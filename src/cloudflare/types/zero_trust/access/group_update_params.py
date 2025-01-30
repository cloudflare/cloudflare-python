# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .applications.access_rule_param import AccessRuleParam

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access group."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match a policy, a user cannot meet any of the Exclude rules.
    """

    is_default: bool
    """Whether this is the default group"""

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match a policy, a user must meet all of the Require rules.
    """
