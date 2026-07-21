# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ......_base_client import AsyncPaginator, make_request_options
from ......types.zero_trust.casb.posture.remediations import job_list_params, job_create_params, job_export_params
from ......types.zero_trust.casb.posture.remediations.job_list_response import JobListResponse
from ......types.zero_trust.casb.posture.remediations.job_create_response import JobCreateResponse
from ......types.zero_trust.casb.posture.remediations.job_export_response import JobExportResponse

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

    def create(
        self,
        *,
        account_id: str,
        finding_instance_ids: SequenceNotStr[str],
        remediation_type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCreateResponse:
        """
        Create one or more remediation jobs tied to a specific Cloudflare Account.

        Args:
          finding_instance_ids: UUIDs identifying Finding Instances.

          remediation_type_id: A UUID identifying this Remediation Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/data-security/posture/remediations/jobs", account_id=account_id),
            body=maybe_transform(
                {
                    "finding_instance_ids": finding_instance_ids,
                    "remediation_type_id": remediation_type_id,
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
            cast_to=cast(Type[JobCreateResponse], ResultWrapper[JobCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        integration_id: str | Omit = omit,
        max_updated_at: Union[str, datetime] | Omit = omit,
        min_updated_at: Union[str, datetime] | Omit = omit,
        order: Literal[
            "created_at",
            "affliction_date",
            "integration_name",
            "status",
            "last_updated_at",
            "asset_name",
            "finding_type_name",
        ]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["pending", "processing", "completed", "failed", "validating"] | Omit = omit,
        triggered_by_actor: List[Literal["user", "account_token"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[JobListResponse]:
        """List all remediation jobs tied to a specific Cloudflare Account.

        Note that
        `cursor` and `page` are mutually exclusive.

        Args:
          cursor: A cursor for pagination.

          direction: Direction to order results.

          integration_id: Filter by an integration ID

          max_updated_at: Filter to view remediations updated on or before the max updated datetime. Can
              be a date-time in ISO 8601 format or an epoch timestamp.

          min_updated_at: Filter to view remediations updated on or after the min updated datetime. Can be
              a date-time in ISO 8601 format or an epoch timestamp.

          order: An optional param to sort the results by the given field.

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          search: A search term.

          status: Filter to view remediations with the given status.

          triggered_by_actor: Filter remediations by what kind of actor triggered them. Supports multiple
              comma-separated values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/remediations/jobs", account_id=account_id),
            page=SyncV4PagePaginationArray[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "integration_id": integration_id,
                        "max_updated_at": max_updated_at,
                        "min_updated_at": min_updated_at,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "status": status,
                        "triggered_by_actor": triggered_by_actor,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    def export(
        self,
        *,
        account_id: str,
        integration_id: SequenceNotStr[str] | Omit = omit,
        max_updated_at: Union[str, datetime] | Omit = omit,
        min_updated_at: Union[str, datetime] | Omit = omit,
        orders: Iterable[job_export_params.Order] | Omit = omit,
        search: str | Omit = omit,
        status: List[Literal["pending", "processing", "completed", "failed", "validating"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[JobExportResponse]:
        """
        Creates a CSV export for remediation jobs and accepts optional filters in the
        payload.

        Args:
          integration_id: Filter by multiple integration IDs.

          max_updated_at: Filter to view remediation jobs updated on or before this datetime. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_updated_at: Filter to view remediation jobs updated on or after this datetime. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          orders: Ordering specifications for the export.

          search: A search term.

          status: Filter by remediation job status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/data-security/posture/remediations/jobs/export", account_id=account_id
            ),
            body=maybe_transform(
                {
                    "integration_id": integration_id,
                    "max_updated_at": max_updated_at,
                    "min_updated_at": min_updated_at,
                    "orders": orders,
                    "search": search,
                    "status": status,
                },
                job_export_params.JobExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobExportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobExportResponse]], ResultWrapper[JobExportResponse]),
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

    async def create(
        self,
        *,
        account_id: str,
        finding_instance_ids: SequenceNotStr[str],
        remediation_type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCreateResponse:
        """
        Create one or more remediation jobs tied to a specific Cloudflare Account.

        Args:
          finding_instance_ids: UUIDs identifying Finding Instances.

          remediation_type_id: A UUID identifying this Remediation Type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/data-security/posture/remediations/jobs", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "finding_instance_ids": finding_instance_ids,
                    "remediation_type_id": remediation_type_id,
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
            cast_to=cast(Type[JobCreateResponse], ResultWrapper[JobCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        integration_id: str | Omit = omit,
        max_updated_at: Union[str, datetime] | Omit = omit,
        min_updated_at: Union[str, datetime] | Omit = omit,
        order: Literal[
            "created_at",
            "affliction_date",
            "integration_name",
            "status",
            "last_updated_at",
            "asset_name",
            "finding_type_name",
        ]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["pending", "processing", "completed", "failed", "validating"] | Omit = omit,
        triggered_by_actor: List[Literal["user", "account_token"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JobListResponse, AsyncV4PagePaginationArray[JobListResponse]]:
        """List all remediation jobs tied to a specific Cloudflare Account.

        Note that
        `cursor` and `page` are mutually exclusive.

        Args:
          cursor: A cursor for pagination.

          direction: Direction to order results.

          integration_id: Filter by an integration ID

          max_updated_at: Filter to view remediations updated on or before the max updated datetime. Can
              be a date-time in ISO 8601 format or an epoch timestamp.

          min_updated_at: Filter to view remediations updated on or after the min updated datetime. Can be
              a date-time in ISO 8601 format or an epoch timestamp.

          order: An optional param to sort the results by the given field.

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          search: A search term.

          status: Filter to view remediations with the given status.

          triggered_by_actor: Filter remediations by what kind of actor triggered them. Supports multiple
              comma-separated values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/remediations/jobs", account_id=account_id),
            page=AsyncV4PagePaginationArray[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "integration_id": integration_id,
                        "max_updated_at": max_updated_at,
                        "min_updated_at": min_updated_at,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "status": status,
                        "triggered_by_actor": triggered_by_actor,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    async def export(
        self,
        *,
        account_id: str,
        integration_id: SequenceNotStr[str] | Omit = omit,
        max_updated_at: Union[str, datetime] | Omit = omit,
        min_updated_at: Union[str, datetime] | Omit = omit,
        orders: Iterable[job_export_params.Order] | Omit = omit,
        search: str | Omit = omit,
        status: List[Literal["pending", "processing", "completed", "failed", "validating"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[JobExportResponse]:
        """
        Creates a CSV export for remediation jobs and accepts optional filters in the
        payload.

        Args:
          integration_id: Filter by multiple integration IDs.

          max_updated_at: Filter to view remediation jobs updated on or before this datetime. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_updated_at: Filter to view remediation jobs updated on or after this datetime. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          orders: Ordering specifications for the export.

          search: A search term.

          status: Filter by remediation job status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/data-security/posture/remediations/jobs/export", account_id=account_id
            ),
            body=await async_maybe_transform(
                {
                    "integration_id": integration_id,
                    "max_updated_at": max_updated_at,
                    "min_updated_at": min_updated_at,
                    "orders": orders,
                    "search": search,
                    "status": status,
                },
                job_export_params.JobExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobExportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobExportResponse]], ResultWrapper[JobExportResponse]),
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
        self.export = to_raw_response_wrapper(
            jobs.export,
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
        self.export = async_to_raw_response_wrapper(
            jobs.export,
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
        self.export = to_streamed_response_wrapper(
            jobs.export,
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
        self.export = async_to_streamed_response_wrapper(
            jobs.export,
        )
