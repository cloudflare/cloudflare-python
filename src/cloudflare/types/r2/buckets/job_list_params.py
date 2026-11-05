# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID that owns the R2 resource."""

    continuation_token: Annotated[str, PropertyInfo(alias="continuationToken")]
    """Pagination token received as `nextContinuationToken` in the previous response."""

    job_type: Annotated[Literal["prefixDelete", "storageClassMigration"], PropertyInfo(alias="jobType")]
    """Restricts results to jobs of the specified type."""

    max_keys: Annotated[int, PropertyInfo(alias="maxKeys")]
    """Maximum number of jobs to return."""

    status: Literal["ENQUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    """Restricts results to jobs with the specified status.

    `jobType` is required when this parameter is provided.
    """

    cf_r2_jurisdiction: Annotated[
        Literal["default", "eu", "us", "fedramp", "fedramp-high"], PropertyInfo(alias="cf-r2-jurisdiction")
    ]
