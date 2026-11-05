# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import is_given, path_template, required_args, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.r2.buckets import job_list_params, job_create_params
from ....types.r2.buckets.job_get_response import JobGetResponse
from ....types.r2.buckets.job_list_response import JobListResponse
from ....types.r2.buckets.job_create_response import JobCreateResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        bucket_name: str,
        *,
        account_id: str,
        job_type: Literal["prefixDelete"],
        prefix: str,
        cf_r2_data_catalog_check: str | Omit = omit,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCreateResponse:
        """Creates a background job for an R2 bucket.

        The `jobType` field selects the job:

        - **`prefixDelete`**: deletes every object whose key begins with `prefix`. A
          non-empty prefix must end in `/`. An empty prefix (`""`) empties the entire
          bucket.
        - **`storageClassMigration`**: migrates every object in the bucket between
          storage classes. `sourceStorageClass` and `destinationStorageClass` must be
          provided together and must differ; omitting both migrates from
          `InfrequentAccess` to `Standard`.

        Poll the returned `id` with the Get Bucket Job endpoint. Small prefix-delete
        jobs can finish synchronously and return `COMPLETED`. Objects uploaded after a
        background job starts are not affected by that job.

        For prefix-delete jobs: abort active multipart uploads before submitting the
        request, since a synchronously completed job does not abort them, and avoid
        writing objects or starting multipart uploads while a bucket-emptying job is in
        progress. Each request creates a distinct job, and the number of active
        prefix-delete jobs is limited per bucket; wait for an existing job to finish
        before retrying a request rejected with HTTP 429. A bucket cannot be emptied
        while event notifications are configured (HTTP 409 / error code 10083). To
        protect a bucket with R2 Data Catalog enabled, send the
        `cf-r2-data-catalog-check` header; a conflict is returned with HTTP 409 / error
        code 10081.

        Prefix-delete jobs require permission to delete objects; storage-class migration
        jobs require permission to write to the bucket.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          prefix: Prefix matched against object keys. A non-empty value must end in `/`. An empty
              string empties the entire bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        bucket_name: str,
        *,
        account_id: str,
        job_type: Literal["storageClassMigration"],
        destination_storage_class: Literal["Standard", "InfrequentAccess"] | Omit = omit,
        source_storage_class: Literal["Standard", "InfrequentAccess"] | Omit = omit,
        cf_r2_data_catalog_check: str | Omit = omit,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCreateResponse:
        """Creates a background job for an R2 bucket.

        The `jobType` field selects the job:

        - **`prefixDelete`**: deletes every object whose key begins with `prefix`. A
          non-empty prefix must end in `/`. An empty prefix (`""`) empties the entire
          bucket.
        - **`storageClassMigration`**: migrates every object in the bucket between
          storage classes. `sourceStorageClass` and `destinationStorageClass` must be
          provided together and must differ; omitting both migrates from
          `InfrequentAccess` to `Standard`.

        Poll the returned `id` with the Get Bucket Job endpoint. Small prefix-delete
        jobs can finish synchronously and return `COMPLETED`. Objects uploaded after a
        background job starts are not affected by that job.

        For prefix-delete jobs: abort active multipart uploads before submitting the
        request, since a synchronously completed job does not abort them, and avoid
        writing objects or starting multipart uploads while a bucket-emptying job is in
        progress. Each request creates a distinct job, and the number of active
        prefix-delete jobs is limited per bucket; wait for an existing job to finish
        before retrying a request rejected with HTTP 429. A bucket cannot be emptied
        while event notifications are configured (HTTP 409 / error code 10083). To
        protect a bucket with R2 Data Catalog enabled, send the
        `cf-r2-data-catalog-check` header; a conflict is returned with HTTP 409 / error
        code 10081.

        Prefix-delete jobs require permission to delete objects; storage-class migration
        jobs require permission to write to the bucket.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "job_type", "prefix"], ["account_id", "job_type"])
    def create(
        self,
        bucket_name: str,
        *,
        account_id: str,
        job_type: Literal["prefixDelete"] | Literal["storageClassMigration"],
        prefix: str | Omit = omit,
        cf_r2_data_catalog_check: str | Omit = omit,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        destination_storage_class: Literal["Standard", "InfrequentAccess"] | Omit = omit,
        source_storage_class: Literal["Standard", "InfrequentAccess"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "cf-r2-data-catalog-check": cf_r2_data_catalog_check,
                    "cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            JobCreateResponse,
            self._post(
                path_template(
                    "/accounts/{account_id}/r2/buckets/{bucket_name}/jobs",
                    account_id=account_id,
                    bucket_name=bucket_name,
                ),
                body=maybe_transform(
                    {
                        "job_type": job_type,
                        "prefix": prefix,
                        "destination_storage_class": destination_storage_class,
                        "source_storage_class": source_storage_class,
                    },
                    job_create_params.JobCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[JobCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[JobCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        bucket_name: str,
        *,
        account_id: str,
        continuation_token: str | Omit = omit,
        job_type: Literal["prefixDelete", "storageClassMigration"] | Omit = omit,
        max_keys: int | Omit = omit,
        status: Literal["ENQUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"] | Omit = omit,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListResponse:
        """
        Lists background jobs for an R2 bucket, including prefix-delete (and
        bucket-emptying) jobs and storage-class migration jobs. Jobs of every type are
        returned unless `jobType` is provided.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          continuation_token: Pagination token received as `nextContinuationToken` in the previous response.

          job_type: Restricts results to jobs of the specified type.

          max_keys: Maximum number of jobs to return.

          status: Restricts results to jobs with the specified status. `jobType` is required when
              this parameter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template(
                "/accounts/{account_id}/r2/buckets/{bucket_name}/jobs", account_id=account_id, bucket_name=bucket_name
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continuation_token": continuation_token,
                        "job_type": job_type,
                        "max_keys": max_keys,
                        "status": status,
                    },
                    job_list_params.JobListParams,
                ),
                post_parser=ResultWrapper[JobListResponse]._unwrapper,
            ),
            cast_to=cast(Type[JobListResponse], ResultWrapper[JobListResponse]),
        )

    def get(
        self,
        job_id: str,
        *,
        account_id: str,
        bucket_name: str,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetResponse:
        """Gets the current status of a background job of any type for an R2 bucket.

        Poll
        this endpoint with the job identifier returned by Create Bucket Job until the
        status is `COMPLETED`, `FAILED`, or `CANCELLED`.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return cast(
            JobGetResponse,
            self._get(
                path_template(
                    "/accounts/{account_id}/r2/buckets/{bucket_name}/jobs/{job_id}",
                    account_id=account_id,
                    bucket_name=bucket_name,
                    job_id=job_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[JobGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[JobGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        bucket_name: str,
        *,
        account_id: str,
        job_type: Literal["prefixDelete"],
        prefix: str,
        cf_r2_data_catalog_check: str | Omit = omit,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCreateResponse:
        """Creates a background job for an R2 bucket.

        The `jobType` field selects the job:

        - **`prefixDelete`**: deletes every object whose key begins with `prefix`. A
          non-empty prefix must end in `/`. An empty prefix (`""`) empties the entire
          bucket.
        - **`storageClassMigration`**: migrates every object in the bucket between
          storage classes. `sourceStorageClass` and `destinationStorageClass` must be
          provided together and must differ; omitting both migrates from
          `InfrequentAccess` to `Standard`.

        Poll the returned `id` with the Get Bucket Job endpoint. Small prefix-delete
        jobs can finish synchronously and return `COMPLETED`. Objects uploaded after a
        background job starts are not affected by that job.

        For prefix-delete jobs: abort active multipart uploads before submitting the
        request, since a synchronously completed job does not abort them, and avoid
        writing objects or starting multipart uploads while a bucket-emptying job is in
        progress. Each request creates a distinct job, and the number of active
        prefix-delete jobs is limited per bucket; wait for an existing job to finish
        before retrying a request rejected with HTTP 429. A bucket cannot be emptied
        while event notifications are configured (HTTP 409 / error code 10083). To
        protect a bucket with R2 Data Catalog enabled, send the
        `cf-r2-data-catalog-check` header; a conflict is returned with HTTP 409 / error
        code 10081.

        Prefix-delete jobs require permission to delete objects; storage-class migration
        jobs require permission to write to the bucket.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          prefix: Prefix matched against object keys. A non-empty value must end in `/`. An empty
              string empties the entire bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        bucket_name: str,
        *,
        account_id: str,
        job_type: Literal["storageClassMigration"],
        destination_storage_class: Literal["Standard", "InfrequentAccess"] | Omit = omit,
        source_storage_class: Literal["Standard", "InfrequentAccess"] | Omit = omit,
        cf_r2_data_catalog_check: str | Omit = omit,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCreateResponse:
        """Creates a background job for an R2 bucket.

        The `jobType` field selects the job:

        - **`prefixDelete`**: deletes every object whose key begins with `prefix`. A
          non-empty prefix must end in `/`. An empty prefix (`""`) empties the entire
          bucket.
        - **`storageClassMigration`**: migrates every object in the bucket between
          storage classes. `sourceStorageClass` and `destinationStorageClass` must be
          provided together and must differ; omitting both migrates from
          `InfrequentAccess` to `Standard`.

        Poll the returned `id` with the Get Bucket Job endpoint. Small prefix-delete
        jobs can finish synchronously and return `COMPLETED`. Objects uploaded after a
        background job starts are not affected by that job.

        For prefix-delete jobs: abort active multipart uploads before submitting the
        request, since a synchronously completed job does not abort them, and avoid
        writing objects or starting multipart uploads while a bucket-emptying job is in
        progress. Each request creates a distinct job, and the number of active
        prefix-delete jobs is limited per bucket; wait for an existing job to finish
        before retrying a request rejected with HTTP 429. A bucket cannot be emptied
        while event notifications are configured (HTTP 409 / error code 10083). To
        protect a bucket with R2 Data Catalog enabled, send the
        `cf-r2-data-catalog-check` header; a conflict is returned with HTTP 409 / error
        code 10081.

        Prefix-delete jobs require permission to delete objects; storage-class migration
        jobs require permission to write to the bucket.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "job_type", "prefix"], ["account_id", "job_type"])
    async def create(
        self,
        bucket_name: str,
        *,
        account_id: str,
        job_type: Literal["prefixDelete"] | Literal["storageClassMigration"],
        prefix: str | Omit = omit,
        cf_r2_data_catalog_check: str | Omit = omit,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        destination_storage_class: Literal["Standard", "InfrequentAccess"] | Omit = omit,
        source_storage_class: Literal["Standard", "InfrequentAccess"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "cf-r2-data-catalog-check": cf_r2_data_catalog_check,
                    "cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            JobCreateResponse,
            await self._post(
                path_template(
                    "/accounts/{account_id}/r2/buckets/{bucket_name}/jobs",
                    account_id=account_id,
                    bucket_name=bucket_name,
                ),
                body=await async_maybe_transform(
                    {
                        "job_type": job_type,
                        "prefix": prefix,
                        "destination_storage_class": destination_storage_class,
                        "source_storage_class": source_storage_class,
                    },
                    job_create_params.JobCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[JobCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[JobCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        bucket_name: str,
        *,
        account_id: str,
        continuation_token: str | Omit = omit,
        job_type: Literal["prefixDelete", "storageClassMigration"] | Omit = omit,
        max_keys: int | Omit = omit,
        status: Literal["ENQUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"] | Omit = omit,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListResponse:
        """
        Lists background jobs for an R2 bucket, including prefix-delete (and
        bucket-emptying) jobs and storage-class migration jobs. Jobs of every type are
        returned unless `jobType` is provided.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          continuation_token: Pagination token received as `nextContinuationToken` in the previous response.

          job_type: Restricts results to jobs of the specified type.

          max_keys: Maximum number of jobs to return.

          status: Restricts results to jobs with the specified status. `jobType` is required when
              this parameter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template(
                "/accounts/{account_id}/r2/buckets/{bucket_name}/jobs", account_id=account_id, bucket_name=bucket_name
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "continuation_token": continuation_token,
                        "job_type": job_type,
                        "max_keys": max_keys,
                        "status": status,
                    },
                    job_list_params.JobListParams,
                ),
                post_parser=ResultWrapper[JobListResponse]._unwrapper,
            ),
            cast_to=cast(Type[JobListResponse], ResultWrapper[JobListResponse]),
        )

    async def get(
        self,
        job_id: str,
        *,
        account_id: str,
        bucket_name: str,
        cf_r2_jurisdiction: Literal["default", "eu", "us", "fedramp", "fedramp-high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetResponse:
        """Gets the current status of a background job of any type for an R2 bucket.

        Poll
        this endpoint with the job identifier returned by Create Bucket Job until the
        status is `COMPLETED`, `FAILED`, or `CANCELLED`.

        Args:
          account_id: Cloudflare account ID that owns the R2 resource.

          bucket_name: Name of the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else not_given}
            ),
            **(extra_headers or {}),
        }
        return cast(
            JobGetResponse,
            await self._get(
                path_template(
                    "/accounts/{account_id}/r2/buckets/{bucket_name}/jobs/{job_id}",
                    account_id=account_id,
                    bucket_name=bucket_name,
                    job_id=job_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[JobGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[JobGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_raw_response_wrapper(
            jobs.create,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.get = to_raw_response_wrapper(
            jobs.get,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_raw_response_wrapper(
            jobs.create,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.get = async_to_raw_response_wrapper(
            jobs.get,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_streamed_response_wrapper(
            jobs.create,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.get = to_streamed_response_wrapper(
            jobs.get,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.get = async_to_streamed_response_wrapper(
            jobs.get,
        )
