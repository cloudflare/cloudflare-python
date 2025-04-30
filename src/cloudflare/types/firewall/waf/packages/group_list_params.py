# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroupListParams"]


class GroupListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier of a schema."""

    direction: Literal["asc", "desc"]
    """Defines the direction used to sort returned rule groups."""

    match: Literal["any", "all"]
    """Defines the condition for search requirements.

    When set to `all`, all the search requirements must match. When set to `any`,
    only one of the search requirements has to match.
    """

    mode: Literal["on", "off"]
    """Defines the state of the rules contained in the rule group.

    When `on`, the rules in the group are configurable/usable.
    """

    name: str
    """Defines the name of the rule group."""

    order: Literal["mode", "rules_count"]
    """Defines the field used to sort returned rule groups."""

    page: float
    """Defines the page number of paginated results."""

    per_page: float
    """Defines the number of rule groups per page."""

    rules_count: float
    """Defines the number of rules in the current rule group."""
