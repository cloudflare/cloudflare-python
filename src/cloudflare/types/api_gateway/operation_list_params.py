# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OperationListParams"]


class OperationListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    direction: Literal["asc", "desc"]
    """Direction to order results."""

    endpoint: str
    """Filter results to only include endpoints containing this pattern."""

    feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]]
    """Add feature(s) to the results.

    The feature name that is given here corresponds to the resulting feature object.
    Have a look at the top-level object description for more details on the specific
    meaning.
    """

    host: List[str]
    """Filter results to only include the specified hosts."""

    method: List[str]
    """Filter results to only include the specified HTTP methods."""

    order: Literal["method", "host", "endpoint", "thresholds.$key"]
    """Field to order by.

    When requesting a feature, the feature keys are available for ordering as well,
    e.g., `thresholds.suggested_threshold`.
    """

    page: int
    """Page number of paginated results."""

    per_page: int
    """Maximum number of results per page."""
