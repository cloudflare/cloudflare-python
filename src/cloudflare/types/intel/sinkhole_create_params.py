# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SinkholeCreateParams"]


class SinkholeCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """An identifier for the resource."""

    name: Required[str]
    """The name of the sinkhole."""

    r2_bucket: str
    """The name of the R2 bucket to store results.

    Required if you want to store large request bodies in R2.
    """

    r2_id: str
    """The id of the R2 instance.

    Required if you want to store large request bodies in R2.
    """

    r2_secret: str
    """The secret key for the R2 API token.

    Required if you want to store large request bodies in R2.
    """
