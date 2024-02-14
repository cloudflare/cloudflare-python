# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["RuleListResponse", "Rule", "Ruleset"]


class Rule(BaseModel):
    id: Optional[str] = None
    """The Web Analytics rule identifier."""

    created: Optional[datetime] = None

    host: Optional[str] = None
    """The hostname the rule will be applied to."""

    inclusive: Optional[bool] = None
    """Whether the rule includes or excludes traffic from being measured."""

    is_paused: Optional[bool] = None
    """Whether the rule is paused or not."""

    paths: Optional[List[str]] = None
    """The paths the rule will be applied to."""

    priority: Optional[float] = None


class Ruleset(BaseModel):
    id: Optional[str] = None
    """The Web Analytics ruleset identifier."""

    enabled: Optional[bool] = None
    """Whether the ruleset is enabled."""

    zone_name: Optional[str] = None

    zone_tag: Optional[str] = None
    """The zone identifier."""


class RuleListResponse(BaseModel):
    rules: Optional[List[Rule]] = None
    """A list of rules."""

    ruleset: Optional[Ruleset] = None
