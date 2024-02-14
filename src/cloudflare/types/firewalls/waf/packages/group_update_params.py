# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo
from .....types import shared_params

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    package_id: Required[str]
    """The unique identifier of a WAF package."""

    mode: Literal["on", "off"]
    """The state of the rules contained in the rule group.

    When `on`, the rules in the group are configurable/usable.
    """
