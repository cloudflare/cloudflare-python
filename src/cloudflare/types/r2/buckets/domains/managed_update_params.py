# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ManagedUpdateParams"]


class ManagedUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID that owns the R2 resource."""

    enabled: Required[bool]
    """Whether to enable public bucket access at the r2.dev domain."""

    cf_r2_jurisdiction: Annotated[
        Literal["default", "eu", "us", "fedramp", "fedramp-high"], PropertyInfo(alias="cf-r2-jurisdiction")
    ]
