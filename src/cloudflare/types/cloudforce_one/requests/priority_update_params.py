# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PriorityUpdateParams"]


class PriorityUpdateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    labels: Required[List[str]]
    """List of labels"""

    priority: Required[int]
    """Priority"""

    requirement: Required[str]
    """Requirement"""

    tlp: Required[Literal["clear", "amber", "amber-strict", "green", "red"]]
    """The CISA defined Traffic Light Protocol (TLP)"""
