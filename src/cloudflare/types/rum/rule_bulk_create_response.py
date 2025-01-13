# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .rum_rule import RUMRule
from ..._models import BaseModel

__all__ = ["RuleBulkCreateResponse", "Ruleset"]


class Ruleset(BaseModel):
    id: Optional[str] = None
    """The Web Analytics ruleset identifier."""

    enabled: Optional[bool] = None
    """Whether the ruleset is enabled."""

    zone_name: Optional[str] = None

    zone_tag: Optional[str] = None
    """The zone identifier."""


class RuleBulkCreateResponse(BaseModel):
    rules: Optional[List[RUMRule]] = None
    """A list of rules."""

    ruleset: Optional[Ruleset] = None
