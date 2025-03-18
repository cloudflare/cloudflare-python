# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InsightCreateParams"]


class InsightCreateParams(TypedDict, total=False):
    account_id: Required[float]
    """Account ID"""

    content: Required[str]
