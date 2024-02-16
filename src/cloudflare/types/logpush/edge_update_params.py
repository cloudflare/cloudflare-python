# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EdgeUpdateParams"]


class EdgeUpdateParams(TypedDict, total=False):
    fields: str
    """Comma-separated list of fields."""

    filter: str
    """Filters to drill down into specific events."""

    sample: int
    """
    The sample parameter is the sample rate of the records set by the client:
    "sample": 1 is 100% of records "sample": 10 is 10% and so on.
    """
