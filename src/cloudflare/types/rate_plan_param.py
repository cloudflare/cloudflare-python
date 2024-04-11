# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .component import Component

__all__ = ["RatePlanParam"]


class RatePlanParam(TypedDict, total=False):
    components: Iterable[Component]
    """Array of available components values for the plan."""

    duration: float
    """The duration of the plan subscription."""
