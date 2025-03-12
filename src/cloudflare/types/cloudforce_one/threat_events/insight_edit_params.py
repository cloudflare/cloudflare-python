# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InsightEditParams"]


class InsightEditParams(TypedDict, total=False):
    account_id: Required[float]
    """Account ID"""

    event_id: Required[str]
    """Event UUID"""

    content: Required[str]
