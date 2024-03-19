# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleListParams"]


class RuleListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    direction: Literal["asc", "desc"]
    """The direction used to sort returned rules."""

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
