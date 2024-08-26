# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleListParams"]


class RuleListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    description: str
    """The public description of the WAF rule."""

    direction: Literal["asc", "desc"]
    """The direction used to sort returned rules."""

    group_id: str
    """The unique identifier of the rule group."""

    match: Literal["any", "all"]
    """When set to `all`, all the search requirements must match.

    When set to `any`, only one of the search requirements has to match.
    """

    mode: Literal["DIS", "CHL", "BLK", "SIM"]
    """The action/mode a rule has been overridden to perform."""

    order: Literal["priority", "group_id", "description"]
    """The field used to sort returned rules."""

    page: float
    """The page number of paginated results."""

    per_page: float
    """The number of rules per page."""

    priority: str
    """The order in which the individual WAF rule is executed within its rule group."""
