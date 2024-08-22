# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OperationListParams"]


class OperationListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    diff: bool
    """
    When `true`, only return API Discovery results that are not saved into API
    Shield Endpoint Management
    """

    direction: Literal["asc", "desc"]
    """Direction to order results."""

    endpoint: str
    """Filter results to only include endpoints containing this pattern."""

    host: List[str]
    """Filter results to only include the specified hosts."""

    method: List[str]
    """Filter results to only include the specified HTTP methods."""

    order: Literal["host", "method", "endpoint", "traffic_stats.requests", "traffic_stats.last_updated"]
    """Field to order by"""

    origin: Literal["ML", "SessionIdentifier"]
    """
    Filter results to only include discovery results sourced from a particular
    discovery engine

    - `ML` - Discovered operations that were sourced using ML API Discovery
    - `SessionIdentifier` - Discovered operations that were sourced using Session
      Identifier API Discovery
    """

    page: int
    """Page number of paginated results."""

    per_page: int
    """Maximum number of results per page."""

    state: Literal["review", "saved", "ignored"]
    """Filter results to only include discovery results in a particular state.

    States are as follows

    - `review` - Discovered operations that are not saved into API Shield Endpoint
      Management
    - `saved` - Discovered operations that are already saved into API Shield
      Endpoint Management
    - `ignored` - Discovered operations that have been marked as ignored
    """
