# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo
from .....types import shared_params

__all__ = ["RuleUpdateParams"]


class RuleUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    package_id: Required[str]
    """The unique identifier of a WAF package."""

    mode: Literal["default", "disable", "simulate", "block", "challenge", "on", "off"]
    """The mode/action of the rule when triggered.

    You must use a value from the `allowed_modes` array of the current rule.
    """
