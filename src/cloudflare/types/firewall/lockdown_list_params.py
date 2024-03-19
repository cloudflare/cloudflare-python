# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LockdownListParams"]


class LockdownListParams(TypedDict, total=False):
    description: str
    """A string to search for in the description of existing rules."""

    description_search: str
    """A string to search for in the description of existing rules."""

    ip: str
    """A single IP address to search for in existing rules."""

    ip_range_search: str
    """A single IP address range to search for in existing rules."""

    ip_search: str
    """A single IP address to search for in existing rules."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """The maximum number of results per page.

    You can only set the value to `1` or to a multiple of 5 such as `5`, `10`, `15`,
    or `20`.
    """

    priority: float
    """The priority of the rule to control the processing order.

    A lower number indicates higher priority. If not provided, any rules with a
    configured priority will be processed before rules without a priority.
    """

    uri_search: str
    """A single URI to search for in the list of URLs of existing rules."""
