# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = ["JobCreateParams", "R2CreatePrefixDeleteJobRequest", "R2CreateStorageClassMigrationJobRequest"]


class R2CreatePrefixDeleteJobRequest(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID that owns the R2 resource."""

    job_type: Required[Annotated[Literal["prefixDelete"], PropertyInfo(alias="jobType")]]

    prefix: Required[str]
    """Prefix matched against object keys.

    A non-empty value must end in `/`. An empty string empties the entire bucket.
    """

    cf_r2_data_catalog_check: Annotated[str, PropertyInfo(alias="cf-r2-data-catalog-check")]

    cf_r2_jurisdiction: Annotated[
        Literal["default", "eu", "us", "fedramp", "fedramp-high"], PropertyInfo(alias="cf-r2-jurisdiction")
    ]


class R2CreateStorageClassMigrationJobRequest(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID that owns the R2 resource."""

    job_type: Required[Annotated[Literal["storageClassMigration"], PropertyInfo(alias="jobType")]]

    destination_storage_class: Annotated[
        Literal["Standard", "InfrequentAccess"], PropertyInfo(alias="destinationStorageClass")
    ]

    source_storage_class: Annotated[Literal["Standard", "InfrequentAccess"], PropertyInfo(alias="sourceStorageClass")]

    cf_r2_data_catalog_check: Annotated[str, PropertyInfo(alias="cf-r2-data-catalog-check")]

    cf_r2_jurisdiction: Annotated[
        Literal["default", "eu", "us", "fedramp", "fedramp-high"], PropertyInfo(alias="cf-r2-jurisdiction")
    ]


JobCreateParams: TypeAlias = Union[R2CreatePrefixDeleteJobRequest, R2CreateStorageClassMigrationJobRequest]
