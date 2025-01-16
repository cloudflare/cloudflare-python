# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .provider import Provider
from ...._utils import PropertyInfo

__all__ = [
    "SippyUpdateParams",
    "R2EnableSippyAws",
    "R2EnableSippyAwsDestination",
    "R2EnableSippyAwsSource",
    "R2EnableSippyGcs",
    "R2EnableSippyGcsDestination",
    "R2EnableSippyGcsSource",
]


class R2EnableSippyAws(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    destination: R2EnableSippyAwsDestination
    """R2 bucket to copy objects to"""

    source: R2EnableSippyAwsSource
    """AWS S3 bucket to copy objects from"""

    jurisdiction: Annotated[Literal["default", "eu", "fedramp"], PropertyInfo(alias="cf-r2-jurisdiction")]
    """The bucket jurisdiction"""


class R2EnableSippyAwsDestination(TypedDict, total=False):
    access_key_id: Annotated[str, PropertyInfo(alias="accessKeyId")]
    """
    ID of a Cloudflare API token. This is the value labelled "Access Key ID" when
    creating an API token from the
    [R2 dashboard](https://dash.cloudflare.com/?to=/:account/r2/api-tokens).

    Sippy will use this token when writing objects to R2, so it is best to scope
    this token to the bucket you're enabling Sippy for.
    """

    provider: Provider

    secret_access_key: Annotated[str, PropertyInfo(alias="secretAccessKey")]
    """
    Value of a Cloudflare API token. This is the value labelled "Secret Access Key"
    when creating an API token from the
    [R2 dashboard](https://dash.cloudflare.com/?to=/:account/r2/api-tokens).

    Sippy will use this token when writing objects to R2, so it is best to scope
    this token to the bucket you're enabling Sippy for.
    """


class R2EnableSippyAwsSource(TypedDict, total=False):
    access_key_id: Annotated[str, PropertyInfo(alias="accessKeyId")]
    """Access Key ID of an IAM credential (ideally scoped to a single S3 bucket)"""

    bucket: str
    """Name of the AWS S3 bucket"""

    provider: Literal["aws"]

    region: str
    """Name of the AWS availability zone"""

    secret_access_key: Annotated[str, PropertyInfo(alias="secretAccessKey")]
    """Secret Access Key of an IAM credential (ideally scoped to a single S3 bucket)"""


class R2EnableSippyGcs(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    destination: R2EnableSippyGcsDestination
    """R2 bucket to copy objects to"""

    source: R2EnableSippyGcsSource
    """GCS bucket to copy objects from"""

    jurisdiction: Annotated[Literal["default", "eu", "fedramp"], PropertyInfo(alias="cf-r2-jurisdiction")]
    """The bucket jurisdiction"""


class R2EnableSippyGcsDestination(TypedDict, total=False):
    access_key_id: Annotated[str, PropertyInfo(alias="accessKeyId")]
    """
    ID of a Cloudflare API token. This is the value labelled "Access Key ID" when
    creating an API token from the
    [R2 dashboard](https://dash.cloudflare.com/?to=/:account/r2/api-tokens).

    Sippy will use this token when writing objects to R2, so it is best to scope
    this token to the bucket you're enabling Sippy for.
    """

    provider: Provider

    secret_access_key: Annotated[str, PropertyInfo(alias="secretAccessKey")]
    """
    Value of a Cloudflare API token. This is the value labelled "Secret Access Key"
    when creating an API token from the
    [R2 dashboard](https://dash.cloudflare.com/?to=/:account/r2/api-tokens).

    Sippy will use this token when writing objects to R2, so it is best to scope
    this token to the bucket you're enabling Sippy for.
    """


class R2EnableSippyGcsSource(TypedDict, total=False):
    bucket: str
    """Name of the GCS bucket"""

    client_email: Annotated[str, PropertyInfo(alias="clientEmail")]
    """Client email of an IAM credential (ideally scoped to a single GCS bucket)"""

    private_key: Annotated[str, PropertyInfo(alias="privateKey")]
    """Private Key of an IAM credential (ideally scoped to a single GCS bucket)"""

    provider: Literal["gcs"]


SippyUpdateParams: TypeAlias = Union[R2EnableSippyAws, R2EnableSippyGcs]
