# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BehaviourGetResponse", "Behaviors"]


class Behaviors(BaseModel):
    description: str

    enabled: bool

    name: str

    risk_level: Literal["low", "medium", "high"]


class BehaviourGetResponse(BaseModel):
    behaviors: Dict[str, Behaviors]
