# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomUpdateParams"]


class CustomUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    bucket_name: Required[str]
    """Name of the bucket"""

    enabled: bool
    """Whether to enable public bucket access at the specified custom domain"""
