# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ManagedUpdateParams"]


class ManagedUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    enabled: Required[bool]
    """Whether to enable public bucket access at the r2.dev domain"""

    jurisdiction: Annotated[Literal["default", "eu", "fedramp"], PropertyInfo(alias="cf-r2-jurisdiction")]
    """The bucket jurisdiction"""
