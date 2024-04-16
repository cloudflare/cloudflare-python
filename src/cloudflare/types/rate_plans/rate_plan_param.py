# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["RatePlanParam", "Component"]


class Component(TypedDict, total=False):
    default: float
    """The default amount allocated."""

    name: Literal["zones", "page_rules", "dedicated_certificates", "dedicated_certificates_custom"]
    """The unique component."""


class RatePlanParam(TypedDict, total=False):
    components: Iterable[Component]
    """Array of available components values for the plan."""

    duration: float
    """The duration of the plan subscription."""
