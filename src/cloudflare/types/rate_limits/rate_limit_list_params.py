# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RateLimitListParams"]


class RateLimitListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    page: float
    """The page number of paginated results."""

    per_page: float
    """The maximum number of results per page.

    You can only set the value to `1` or to a multiple of 5 such as `5`, `10`, `15`,
    or `20`.
    """
