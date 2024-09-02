# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .logging_param import LoggingParam

from typing import List, Dict

from .phase import Phase

__all__ = ["SkipRuleParam", "ActionParameters"]


class ActionParameters(TypedDict, total=False):
    phases: List[Phase]
    """A list of phases to skip the execution of.

    This option is incompatible with the ruleset and rulesets options.
    """

    products: List[Literal["bic", "hot", "rateLimit", "securityLevel", "uaBlock", "waf", "zoneLockdown"]]
    """A list of legacy security products to skip the execution of."""

    rules: Dict[str, List[str]]
    """
    A mapping of ruleset IDs to a list of rule IDs in that ruleset to skip the
    execution of. This option is incompatible with the ruleset option.
    """

    ruleset: Literal["current"]
    """A ruleset to skip the execution of.

    This option is incompatible with the rulesets, rules and phases options.
    """

    rulesets: List[str]
    """A list of ruleset IDs to skip the execution of.

    This option is incompatible with the ruleset and phases options.
    """


class SkipRuleParam(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["skip"]
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
