# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SippyUpdateParams", "Destination", "Source"]


class SippyUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    destination: Destination

    source: Source


class Destination(TypedDict, total=False):
    access_key_id: Annotated[str, PropertyInfo(alias="accessKeyId")]
    """
    ID of a Cloudflare API token. This is the value labelled "Access Key ID" when
    creating an API token from the
    [R2 dashboard](https://dash.cloudflare.com/?to=/:account/r2/api-tokens).

    Sippy will use this token when writing objects to R2, so it is best to scope
    this token to the bucket you're enabling Sippy for.
    """

    provider: Literal["r2"]

    secret_access_key: Annotated[str, PropertyInfo(alias="secretAccessKey")]
    """
    Value of a Cloudflare API token. This is the value labelled "Secret Access Key"
    when creating an API token from the
    [R2 dashboard](https://dash.cloudflare.com/?to=/:account/r2/api-tokens).

    Sippy will use this token when writing objects to R2, so it is best to scope
    this token to the bucket you're enabling Sippy for.
    """


class Source(TypedDict, total=False):
    access_key_id: Annotated[str, PropertyInfo(alias="accessKeyId")]
    """Access Key ID of an IAM credential (ideally scoped to a single S3 bucket)"""

    bucket: str
    """Name of the GCS bucket"""

    client_email: Annotated[str, PropertyInfo(alias="clientEmail")]
    """Client email of an IAM credential (ideally scoped to a single GCS bucket)"""

    private_key: Annotated[str, PropertyInfo(alias="privateKey")]
    """Private Key of an IAM credential (ideally scoped to a single GCS bucket)"""

    provider: Literal["gcs", "aws"]

    region: str
    """Name of the AWS availability zone"""

    secret_access_key: Annotated[str, PropertyInfo(alias="secretAccessKey")]
    """Secret Access Key of an IAM credential (ideally scoped to a single S3 bucket)"""
