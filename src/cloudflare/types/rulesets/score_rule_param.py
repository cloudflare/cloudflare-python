# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .logging_param import LoggingParam

__all__ = ["ScoreRuleParam", "ActionParameters"]

class ActionParameters(TypedDict, total=False):
    increment: int
    """
    Increment contains the delta to change the score and can be either positive or
    negative.
    """

class ScoreRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["score"]
    """The action to perform when the rule matches."""

    action_parameters: ActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""