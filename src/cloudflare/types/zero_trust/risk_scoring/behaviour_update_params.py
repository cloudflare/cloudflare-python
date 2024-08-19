# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BehaviourUpdateParams", "Behaviors"]


class BehaviourUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    behaviors: Required[Dict[str, Behaviors]]


class Behaviors(TypedDict, total=False):
    enabled: Required[bool]

    risk_level: Required[Literal["low", "medium", "high"]]
