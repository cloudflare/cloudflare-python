# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.r2.super_slurper import job_list_params, job_create_params
from .....types.r2.super_slurper.job_get_response import JobGetResponse
from .....types.r2.super_slurper.job_list_response import JobListResponse
from .....types.r2.super_slurper.job_abort_response import JobAbortResponse
from .....types.r2.super_slurper.job_pause_response import JobPauseResponse
from .....types.r2.super_slurper.job_create_response import JobCreateResponse
from .....types.r2.super_slurper.job_resume_response import JobResumeResponse
from .....types.r2.super_slurper.job_progress_response import JobProgressResponse
from .....types.r2.super_slurper.job_abort_all_response import JobAbortAllResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

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
        account_id: str | None = None,
        overwrite: bool | Omit = omit,
        source: job_create_params.Source | Omit = omit,
        target: job_create_params.Target | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[JobCreateResponse]:
        """
        Creates a new R2 Super Slurper migration job to transfer objects from a source
        bucket (e.g. S3, GCS, R2) to R2.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/slurper/jobs", account_id=account_id),
            body=maybe_transform(
                {
                    "overwrite": overwrite,
                    "source": source,
                    "target": target,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobCreateResponse]], ResultWrapper[JobCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[JobListResponse]:
        """
        Lists all R2 Super Slurper migration jobs for the account with their status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/slurper/jobs", account_id=account_id),
            page=SyncSinglePage[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    def abort(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Cancels a specific R2 Super Slurper migration job.

        Any objects in the middle of
        a transfer will finish, but no new objects will start transferring.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._put(
            path_template("/accounts/{account_id}/slurper/jobs/{job_id}/abort", account_id=account_id, job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobAbortResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def abort_all(
        self,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Cancels all running R2 Super Slurper migration jobs for the account.

        Any objects
        in the middle of a transfer will finish, but no new objects will start
        transferring.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            path_template("/accounts/{account_id}/slurper/jobs/abortAll", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobAbortAllResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def get(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[JobGetResponse]:
        """
        Retrieves detailed status and configuration for a specific R2 Super Slurper
        migration job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/slurper/jobs/{job_id}", account_id=account_id, job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobGetResponse]], ResultWrapper[JobGetResponse]),
        )

    def pause(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Pauses a running R2 Super Slurper migration job.

        The job can be resumed later to
        continue transferring.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._put(
            path_template("/accounts/{account_id}/slurper/jobs/{job_id}/pause", account_id=account_id, job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobPauseResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def progress(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[JobProgressResponse]:
        """
        Retrieves current progress metrics for an R2 Super Slurper migration job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/slurper/jobs/{job_id}/progress", account_id=account_id, job_id=job_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobProgressResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobProgressResponse]], ResultWrapper[JobProgressResponse]),
        )

    def resume(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Resumes a paused R2 Super Slurper migration job, continuing the transfer from
        where it stopped.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._put(
            path_template("/accounts/{account_id}/slurper/jobs/{job_id}/resume", account_id=account_id, job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobResumeResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

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
        account_id: str | None = None,
        overwrite: bool | Omit = omit,
        source: job_create_params.Source | Omit = omit,
        target: job_create_params.Target | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[JobCreateResponse]:
        """
        Creates a new R2 Super Slurper migration job to transfer objects from a source
        bucket (e.g. S3, GCS, R2) to R2.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/slurper/jobs", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "overwrite": overwrite,
                    "source": source,
                    "target": target,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobCreateResponse]], ResultWrapper[JobCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JobListResponse, AsyncSinglePage[JobListResponse]]:
        """
        Lists all R2 Super Slurper migration jobs for the account with their status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/slurper/jobs", account_id=account_id),
            page=AsyncSinglePage[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    async def abort(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Cancels a specific R2 Super Slurper migration job.

        Any objects in the middle of
        a transfer will finish, but no new objects will start transferring.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._put(
            path_template("/accounts/{account_id}/slurper/jobs/{job_id}/abort", account_id=account_id, job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobAbortResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def abort_all(
        self,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Cancels all running R2 Super Slurper migration jobs for the account.

        Any objects
        in the middle of a transfer will finish, but no new objects will start
        transferring.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            path_template("/accounts/{account_id}/slurper/jobs/abortAll", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobAbortAllResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def get(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[JobGetResponse]:
        """
        Retrieves detailed status and configuration for a specific R2 Super Slurper
        migration job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/slurper/jobs/{job_id}", account_id=account_id, job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobGetResponse]], ResultWrapper[JobGetResponse]),
        )

    async def pause(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Pauses a running R2 Super Slurper migration job.

        The job can be resumed later to
        continue transferring.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._put(
            path_template("/accounts/{account_id}/slurper/jobs/{job_id}/pause", account_id=account_id, job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobPauseResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def progress(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[JobProgressResponse]:
        """
        Retrieves current progress metrics for an R2 Super Slurper migration job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/slurper/jobs/{job_id}/progress", account_id=account_id, job_id=job_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobProgressResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobProgressResponse]], ResultWrapper[JobProgressResponse]),
        )

    async def resume(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Resumes a paused R2 Super Slurper migration job, continuing the transfer from
        where it stopped.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._put(
            path_template("/accounts/{account_id}/slurper/jobs/{job_id}/resume", account_id=account_id, job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobResumeResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
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
        self.abort = to_raw_response_wrapper(
            jobs.abort,
        )
        self.abort_all = to_raw_response_wrapper(
            jobs.abort_all,
        )
        self.get = to_raw_response_wrapper(
            jobs.get,
        )
        self.pause = to_raw_response_wrapper(
            jobs.pause,
        )
        self.progress = to_raw_response_wrapper(
            jobs.progress,
        )
        self.resume = to_raw_response_wrapper(
            jobs.resume,
        )

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._jobs.logs)


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_raw_response_wrapper(
            jobs.create,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.abort = async_to_raw_response_wrapper(
            jobs.abort,
        )
        self.abort_all = async_to_raw_response_wrapper(
            jobs.abort_all,
        )
        self.get = async_to_raw_response_wrapper(
            jobs.get,
        )
        self.pause = async_to_raw_response_wrapper(
            jobs.pause,
        )
        self.progress = async_to_raw_response_wrapper(
            jobs.progress,
        )
        self.resume = async_to_raw_response_wrapper(
            jobs.resume,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._jobs.logs)


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_streamed_response_wrapper(
            jobs.create,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.abort = to_streamed_response_wrapper(
            jobs.abort,
        )
        self.abort_all = to_streamed_response_wrapper(
            jobs.abort_all,
        )
        self.get = to_streamed_response_wrapper(
            jobs.get,
        )
        self.pause = to_streamed_response_wrapper(
            jobs.pause,
        )
        self.progress = to_streamed_response_wrapper(
            jobs.progress,
        )
        self.resume = to_streamed_response_wrapper(
            jobs.resume,
        )

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._jobs.logs)


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.abort = async_to_streamed_response_wrapper(
            jobs.abort,
        )
        self.abort_all = async_to_streamed_response_wrapper(
            jobs.abort_all,
        )
        self.get = async_to_streamed_response_wrapper(
            jobs.get,
        )
        self.pause = async_to_streamed_response_wrapper(
            jobs.pause,
        )
        self.progress = async_to_streamed_response_wrapper(
            jobs.progress,
        )
        self.resume = async_to_streamed_response_wrapper(
            jobs.resume,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._jobs.logs)
