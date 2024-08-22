# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .label import Label

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
