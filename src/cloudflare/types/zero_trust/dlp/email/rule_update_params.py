# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleUpdateParams", "Action", "Condition"]


class RuleUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    action: Required[Action]

    conditions: Required[Iterable[Condition]]
    """Rule is triggered if all conditions match"""

    enabled: Required[bool]

    name: Required[str]

    description: Optional[str]


class Action(TypedDict, total=False):
    action: Required[Literal["Block"]]

    message: Optional[str]


class Condition(TypedDict, total=False):
    operator: Required[Literal["InList", "NotInList", "MatchRegex", "NotMatchRegex"]]

    selector: Required[Literal["Recipients", "Sender", "DLPProfiles"]]

    value: Required[Union[List[str], str]]
