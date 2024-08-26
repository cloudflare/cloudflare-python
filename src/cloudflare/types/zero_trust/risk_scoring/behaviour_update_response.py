# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["BehaviourUpdateResponse", "Behaviors"]

class Behaviors(BaseModel):
    enabled: bool

    risk_level: Literal["low", "medium", "high"]

class BehaviourUpdateResponse(BaseModel):
    behaviors: Dict[str, Behaviors]