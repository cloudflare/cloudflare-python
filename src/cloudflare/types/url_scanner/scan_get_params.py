# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScanGetParams"]


class ScanGetParams(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountId")]]
    """Account Id"""

    full: bool
    """Whether to return full report (scan summary and network log)."""
