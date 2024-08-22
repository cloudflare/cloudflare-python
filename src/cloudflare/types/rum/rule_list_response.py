# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from .rum_rule import RUMRule

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RuleListResponse", "Ruleset"]

class Ruleset(BaseModel):
    id: Optional[str] = None
    """The Web Analytics ruleset identifier."""

    enabled: Optional[bool] = None
    """Whether the ruleset is enabled."""

    zone_name: Optional[str] = None

    zone_tag: Optional[str] = None
    """The zone identifier."""

class RuleListResponse(BaseModel):
    rules: Optional[List[RUMRule]] = None
    """A list of rules."""

    ruleset: Optional[Ruleset] = None