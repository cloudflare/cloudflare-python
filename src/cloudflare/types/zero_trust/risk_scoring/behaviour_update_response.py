# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BehaviourUpdateResponse", "Behaviors"]


class Behaviors(BaseModel):
    enabled: bool

    risk_level: Literal["low", "medium", "high"]


class BehaviourUpdateResponse(BaseModel):
    behaviors: Dict[str, Behaviors]
