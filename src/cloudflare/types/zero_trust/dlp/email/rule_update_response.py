# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["RuleUpdateResponse", "Action", "Condition"]


class Action(BaseModel):
    action: Literal["Block"]

    message: Optional[str] = None


class Condition(BaseModel):
    operator: Literal["InList", "NotInList", "MatchRegex", "NotMatchRegex"]

    selector: Literal["Recipients", "Sender", "DLPProfiles"]

    value: Union[List[str], str]


class RuleUpdateResponse(BaseModel):
    action: Action

    conditions: List[Condition]
    """Rule is triggered if all conditions match"""

    created_at: datetime

    enabled: bool

    name: str

    priority: int

    rule_id: str

    updated_at: datetime

    description: Optional[str] = None
