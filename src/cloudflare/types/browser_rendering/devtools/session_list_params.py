# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    account_id: str
    """Account ID."""

    limit: float

    offset: float
