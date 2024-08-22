# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List, Dict

from .phase import Phase

from typing_extensions import Literal

from datetime import datetime

from .logging import Logging

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SkipRule", "ActionParameters"]

class ActionParameters(BaseModel):
    phases: Optional[List[Phase]] = None
    """A list of phases to skip the execution of.

    This option is incompatible with the ruleset and rulesets options.
    """

    products: Optional[List[Literal["bic", "hot", "rateLimit", "securityLevel", "uaBlock", "waf", "zoneLockdown"]]] = None
    """A list of legacy security products to skip the execution of."""

    rules: Optional[Dict[str, List[str]]] = None
    """
    A mapping of ruleset IDs to a list of rule IDs in that ruleset to skip the
    execution of. This option is incompatible with the ruleset option.
    """

    ruleset: Optional[Literal["current"]] = None
    """A ruleset to skip the execution of.

    This option is incompatible with the rulesets, rules and phases options.
    """

    rulesets: Optional[List[str]] = None
    """A list of ruleset IDs to skip the execution of.

    This option is incompatible with the ruleset and phases options.
    """

class SkipRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["skip"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[ActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""