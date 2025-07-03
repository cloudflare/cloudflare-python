# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UARuleListParams"]


class UARuleListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines an identifier."""

    description: str
    """A string to search for in the description of existing rules."""

    page: float
    """Page number of paginated results."""

    paused: bool
    """When true, indicates that the rule is currently paused."""

    per_page: float
    """The maximum number of results per page.

    You can only set the value to `1` or to a multiple of 5 such as `5`, `10`, `15`,
    or `20`.
    """

    user_agent: str
    """A string to search for in the user agent values of existing rules."""
