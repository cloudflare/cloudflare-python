# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

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
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.aisearch.namespaces.instances import (
    job_list_params,
    job_logs_params,
    job_create_params,
    job_update_params,
)
from .....types.aisearch.namespaces.instances.job_get_response import JobGetResponse
from .....types.aisearch.namespaces.instances.job_list_response import JobListResponse
from .....types.aisearch.namespaces.instances.job_logs_response import JobLogsResponse
from .....types.aisearch.namespaces.instances.job_create_response import JobCreateResponse
from .....types.aisearch.namespaces.instances.job_update_response import JobUpdateResponse

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
        id: str,
        *,
        account_id: str | None = None,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCreateResponse:
        """
        Creates a new indexing job for an AI Search instance.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs",
                account_id=account_id,
                name=name,
                id=id,
            ),
            body=maybe_transform({"description": description}, job_create_params.JobCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[JobCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[JobCreateResponse], ResultWrapper[JobCreateResponse]),
        )

    def update(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        action: Literal["cancel"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobUpdateResponse:
        """
        Updates the status of an AI Search indexing job.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}",
                account_id=account_id,
                name=name,
                id=id,
                job_id=job_id,
            ),
            body=maybe_transform({"action": action}, job_update_params.JobUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[JobUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[JobUpdateResponse], ResultWrapper[JobUpdateResponse]),
        )

    def list(
        self,
        id: str,
        *,
        account_id: str | None = None,
        name: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[JobListResponse]:
        """
        Lists indexing jobs for an AI Search instance.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs",
                account_id=account_id,
                name=name,
                id=id,
            ),
            page=SyncV4PagePaginationArray[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    def get(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetResponse:
        """
        Retrieves details for a specific AI Search indexing job.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}",
                account_id=account_id,
                name=name,
                id=id,
                job_id=job_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[JobGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[JobGetResponse], ResultWrapper[JobGetResponse]),
        )

    def logs(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobLogsResponse:
        """
        Lists log entries for an AI Search indexing job.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}/logs",
                account_id=account_id,
                name=name,
                id=id,
                job_id=job_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    job_logs_params.JobLogsParams,
                ),
                post_parser=ResultWrapper[JobLogsResponse]._unwrapper,
            ),
            cast_to=cast(Type[JobLogsResponse], ResultWrapper[JobLogsResponse]),
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
        id: str,
        *,
        account_id: str | None = None,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobCreateResponse:
        """
        Creates a new indexing job for an AI Search instance.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs",
                account_id=account_id,
                name=name,
                id=id,
            ),
            body=await async_maybe_transform({"description": description}, job_create_params.JobCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[JobCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[JobCreateResponse], ResultWrapper[JobCreateResponse]),
        )

    async def update(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        action: Literal["cancel"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobUpdateResponse:
        """
        Updates the status of an AI Search indexing job.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}",
                account_id=account_id,
                name=name,
                id=id,
                job_id=job_id,
            ),
            body=await async_maybe_transform({"action": action}, job_update_params.JobUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[JobUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[JobUpdateResponse], ResultWrapper[JobUpdateResponse]),
        )

    def list(
        self,
        id: str,
        *,
        account_id: str | None = None,
        name: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JobListResponse, AsyncV4PagePaginationArray[JobListResponse]]:
        """
        Lists indexing jobs for an AI Search instance.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs",
                account_id=account_id,
                name=name,
                id=id,
            ),
            page=AsyncV4PagePaginationArray[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    async def get(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetResponse:
        """
        Retrieves details for a specific AI Search indexing job.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}",
                account_id=account_id,
                name=name,
                id=id,
                job_id=job_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[JobGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[JobGetResponse], ResultWrapper[JobGetResponse]),
        )

    async def logs(
        self,
        job_id: str,
        *,
        account_id: str | None = None,
        name: str,
        id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobLogsResponse:
        """
        Lists log entries for an AI Search indexing job.

        Args:
          id: AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/ai-search/namespaces/{name}/instances/{id}/jobs/{job_id}/logs",
                account_id=account_id,
                name=name,
                id=id,
                job_id=job_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    job_logs_params.JobLogsParams,
                ),
                post_parser=ResultWrapper[JobLogsResponse]._unwrapper,
            ),
            cast_to=cast(Type[JobLogsResponse], ResultWrapper[JobLogsResponse]),
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_raw_response_wrapper(
            jobs.create,
        )
        self.update = to_raw_response_wrapper(
            jobs.update,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.get = to_raw_response_wrapper(
            jobs.get,
        )
        self.logs = to_raw_response_wrapper(
            jobs.logs,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_raw_response_wrapper(
            jobs.create,
        )
        self.update = async_to_raw_response_wrapper(
            jobs.update,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.get = async_to_raw_response_wrapper(
            jobs.get,
        )
        self.logs = async_to_raw_response_wrapper(
            jobs.logs,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_streamed_response_wrapper(
            jobs.create,
        )
        self.update = to_streamed_response_wrapper(
            jobs.update,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.get = to_streamed_response_wrapper(
            jobs.get,
        )
        self.logs = to_streamed_response_wrapper(
            jobs.logs,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            jobs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.get = async_to_streamed_response_wrapper(
            jobs.get,
        )
        self.logs = async_to_streamed_response_wrapper(
            jobs.logs,
        )
