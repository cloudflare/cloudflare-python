# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BehaviourUpdateResponse", "Behaviors"]


class Behaviors(BaseModel):
    description: Optional[str] = None

    enabled: Optional[bool] = None

    name: Optional[str] = None

    risk_level: Optional[Literal["low", "medium", "high"]] = None


class BehaviourUpdateResponse(BaseModel):
    behaviors: Optional[Dict[str, Behaviors]] = None
