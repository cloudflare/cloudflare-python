# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CustomUpdateParams"]


class CustomUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    bucket_name: Required[str]
    """Name of the bucket"""

    enabled: bool
    """Whether to enable public bucket access at the specified custom domain"""

    min_tls: Annotated[Literal["1.0", "1.1", "1.2", "1.3"], PropertyInfo(alias="minTLS")]
    """Minimum TLS Version the custom domain will accept for incoming connections.

    If not set, defaults to previous value.
    """

    jurisdiction: Annotated[Literal["default", "eu", "fedramp"], PropertyInfo(alias="cf-r2-jurisdiction")]
    """The bucket jurisdiction"""
