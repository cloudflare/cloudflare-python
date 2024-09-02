# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["BehaviourUpdateParams", "Behaviors"]


class BehaviourUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    behaviors: Required[Dict[str, Behaviors]]


class Behaviors(TypedDict, total=False):
    enabled: Required[bool]

    risk_level: Required[Literal["low", "medium", "high"]]
