# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .unnamed_schema_ref_b5e16cee4f32382c294201aedb9fc050 import UnnamedSchemaRefB5e16cee4f32382c294201aedb9fc050

__all__ = ["DNSParam"]


class DNSParam(TypedDict, total=False):
    count: float
    """Total results returned based on your search parameters."""

    page: float
    """Current page within paginated list of results."""

    per_page: float
    """Number of results per page of results."""

    reverse_records: Iterable[UnnamedSchemaRefB5e16cee4f32382c294201aedb9fc050]
    """Reverse DNS look-ups observed during the time period."""
