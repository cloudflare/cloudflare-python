# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .enforcement_rule_param import EnforcementRuleParam

__all__ = ["PrecursorUpdateParams"]


class PrecursorUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    default_mode: Literal["off", "min-friction", "max-security"]
    """
    The zone-level Precursor enforcement mode applied to requests that do not match
    a more specific enforcement rule.
    """

    enforcement_rules: Iterable[EnforcementRuleParam]
    """The ordered list of enforcement rules for the zone."""
