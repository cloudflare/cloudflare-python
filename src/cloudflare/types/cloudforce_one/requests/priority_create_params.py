# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List

from .label import Label

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["PriorityCreateParams"]


class PriorityCreateParams(TypedDict, total=False):
    labels: Required[List[Label]]
    """List of labels"""

    priority: Required[int]
    """Priority"""

    requirement: Required[str]
    """Requirement"""

    tlp: Required[Literal["clear", "amber", "amber-strict", "green", "red"]]
    """The CISA defined Traffic Light Protocol (TLP)"""
