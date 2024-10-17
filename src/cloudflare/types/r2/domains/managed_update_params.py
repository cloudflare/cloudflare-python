# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ManagedUpdateParams"]


class ManagedUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    enabled: Required[bool]
    """Whether to enable public bucket access at the r2.dev domain"""
