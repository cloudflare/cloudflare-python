# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BehaviourUpdateParams", "Behaviors"]


class BehaviourUpdateParams(TypedDict, total=False):
    behaviors: Dict[str, Behaviors]


class Behaviors(TypedDict, total=False):
    enabled: Required[bool]

    risk_level: Required[Optional[Literal["low", "medium", "high"]]]
