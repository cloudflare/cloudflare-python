# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .label import Label
from ...._types import SequenceNotStr

__all__ = ["PriorityUpdateParams"]


class PriorityUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    labels: Required[SequenceNotStr[Label]]
    """List of labels."""

    priority: Required[int]
    """Priority."""

    requirement: Required[str]
    """Requirement."""

    tlp: Required[Literal["clear", "amber", "amber-strict", "green", "red"]]
    """The CISA defined Traffic Light Protocol (TLP)."""
