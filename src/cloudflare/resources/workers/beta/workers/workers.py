# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
from ....._utils import maybe_transform, async_maybe_transform
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
from .....types.workers.beta import worker_edit_params, worker_list_params, worker_create_params, worker_update_params
from .....types.workers.beta.worker import Worker
from .....types.workers.beta.worker_delete_response import WorkerDeleteResponse

__all__ = ["WorkersResource", "AsyncWorkersResource"]


class WorkersResource(SyncAPIResource):
    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WorkersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        logpush: bool | NotGiven = NOT_GIVEN,
        observability: worker_create_params.Observability | NotGiven = NOT_GIVEN,
        subdomain: worker_create_params.Subdomain | NotGiven = NOT_GIVEN,
        tags: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        tail_consumers: Iterable[worker_create_params.TailConsumer] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Worker:
        """
        Create a new Worker.

        Args:
          account_id: Identifier.

          name: Name of the Worker.

          logpush: Whether logpush is enabled for the Worker.

          observability: Observability settings for the Worker.

          subdomain: Subdomain settings for the Worker.

          tags: Tags associated with the Worker.

          tail_consumers: Other Workers that should consume logs from the Worker.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/workers/workers",
            body=maybe_transform(
                {
                    "name": name,
                    "logpush": logpush,
                    "observability": observability,
                    "subdomain": subdomain,
                    "tags": tags,
                    "tail_consumers": tail_consumers,
                },
                worker_create_params.WorkerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Worker]._unwrapper,
            ),
            cast_to=cast(Type[Worker], ResultWrapper[Worker]),
        )

    def update(
        self,
        worker_id: str,
        *,
        account_id: str,
        name: str,
        logpush: bool | NotGiven = NOT_GIVEN,
        observability: worker_update_params.Observability | NotGiven = NOT_GIVEN,
        subdomain: worker_update_params.Subdomain | NotGiven = NOT_GIVEN,
        tags: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        tail_consumers: Iterable[worker_update_params.TailConsumer] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Worker:
        """
        Perform a complete replacement of a Worker, where omitted properties are set to
        their default values. This is the exact same as the Create Worker endpoint, but
        operates on an existing Worker. To perform a partial update instead, use the
        Edit Worker endpoint.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          name: Name of the Worker.

          logpush: Whether logpush is enabled for the Worker.

          observability: Observability settings for the Worker.

          subdomain: Subdomain settings for the Worker.

          tags: Tags associated with the Worker.

          tail_consumers: Other Workers that should consume logs from the Worker.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._put(
            f"/accounts/{account_id}/workers/workers/{worker_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "logpush": logpush,
                    "observability": observability,
                    "subdomain": subdomain,
                    "tags": tags,
                    "tail_consumers": tail_consumers,
                },
                worker_update_params.WorkerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Worker]._unwrapper,
            ),
            cast_to=cast(Type[Worker], ResultWrapper[Worker]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Worker]:
        """
        List all Workers for an account.

        Args:
          account_id: Identifier.

          page: Current page.

          per_page: Items per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/workers",
            page=SyncV4PagePaginationArray[Worker],
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
                    worker_list_params.WorkerListParams,
                ),
            ),
            model=Worker,
        )

    def delete(
        self,
        worker_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerDeleteResponse:
        """
        Delete a Worker and all its associated resources (versions, deployments, etc.).

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._delete(
            f"/accounts/{account_id}/workers/workers/{worker_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerDeleteResponse,
        )

    def edit(
        self,
        worker_id: str,
        *,
        account_id: str,
        logpush: bool,
        name: str,
        observability: worker_edit_params.Observability,
        subdomain: worker_edit_params.Subdomain,
        tags: SequenceNotStr[str],
        tail_consumers: Iterable[worker_edit_params.TailConsumer],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Worker:
        """
        Perform a partial update on a Worker, where omitted properties are left
        unchanged from their current values.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          logpush: Whether logpush is enabled for the Worker.

          name: Name of the Worker.

          observability: Observability settings for the Worker.

          subdomain: Subdomain settings for the Worker.

          tags: Tags associated with the Worker.

          tail_consumers: Other Workers that should consume logs from the Worker.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._patch(
            f"/accounts/{account_id}/workers/workers/{worker_id}",
            body=maybe_transform(
                {
                    "logpush": logpush,
                    "name": name,
                    "observability": observability,
                    "subdomain": subdomain,
                    "tags": tags,
                    "tail_consumers": tail_consumers,
                },
                worker_edit_params.WorkerEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Worker]._unwrapper,
            ),
            cast_to=cast(Type[Worker], ResultWrapper[Worker]),
        )

    def get(
        self,
        worker_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Worker:
        """
        Get details about a specific Worker.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/workers/{worker_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Worker]._unwrapper,
            ),
            cast_to=cast(Type[Worker], ResultWrapper[Worker]),
        )


class AsyncWorkersResource(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWorkersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        logpush: bool | NotGiven = NOT_GIVEN,
        observability: worker_create_params.Observability | NotGiven = NOT_GIVEN,
        subdomain: worker_create_params.Subdomain | NotGiven = NOT_GIVEN,
        tags: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        tail_consumers: Iterable[worker_create_params.TailConsumer] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Worker:
        """
        Create a new Worker.

        Args:
          account_id: Identifier.

          name: Name of the Worker.

          logpush: Whether logpush is enabled for the Worker.

          observability: Observability settings for the Worker.

          subdomain: Subdomain settings for the Worker.

          tags: Tags associated with the Worker.

          tail_consumers: Other Workers that should consume logs from the Worker.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/workers/workers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "logpush": logpush,
                    "observability": observability,
                    "subdomain": subdomain,
                    "tags": tags,
                    "tail_consumers": tail_consumers,
                },
                worker_create_params.WorkerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Worker]._unwrapper,
            ),
            cast_to=cast(Type[Worker], ResultWrapper[Worker]),
        )

    async def update(
        self,
        worker_id: str,
        *,
        account_id: str,
        name: str,
        logpush: bool | NotGiven = NOT_GIVEN,
        observability: worker_update_params.Observability | NotGiven = NOT_GIVEN,
        subdomain: worker_update_params.Subdomain | NotGiven = NOT_GIVEN,
        tags: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        tail_consumers: Iterable[worker_update_params.TailConsumer] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Worker:
        """
        Perform a complete replacement of a Worker, where omitted properties are set to
        their default values. This is the exact same as the Create Worker endpoint, but
        operates on an existing Worker. To perform a partial update instead, use the
        Edit Worker endpoint.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          name: Name of the Worker.

          logpush: Whether logpush is enabled for the Worker.

          observability: Observability settings for the Worker.

          subdomain: Subdomain settings for the Worker.

          tags: Tags associated with the Worker.

          tail_consumers: Other Workers that should consume logs from the Worker.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/workers/{worker_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "logpush": logpush,
                    "observability": observability,
                    "subdomain": subdomain,
                    "tags": tags,
                    "tail_consumers": tail_consumers,
                },
                worker_update_params.WorkerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Worker]._unwrapper,
            ),
            cast_to=cast(Type[Worker], ResultWrapper[Worker]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Worker, AsyncV4PagePaginationArray[Worker]]:
        """
        List all Workers for an account.

        Args:
          account_id: Identifier.

          page: Current page.

          per_page: Items per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/workers",
            page=AsyncV4PagePaginationArray[Worker],
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
                    worker_list_params.WorkerListParams,
                ),
            ),
            model=Worker,
        )

    async def delete(
        self,
        worker_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerDeleteResponse:
        """
        Delete a Worker and all its associated resources (versions, deployments, etc.).

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/workers/workers/{worker_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerDeleteResponse,
        )

    async def edit(
        self,
        worker_id: str,
        *,
        account_id: str,
        logpush: bool,
        name: str,
        observability: worker_edit_params.Observability,
        subdomain: worker_edit_params.Subdomain,
        tags: SequenceNotStr[str],
        tail_consumers: Iterable[worker_edit_params.TailConsumer],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Worker:
        """
        Perform a partial update on a Worker, where omitted properties are left
        unchanged from their current values.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          logpush: Whether logpush is enabled for the Worker.

          name: Name of the Worker.

          observability: Observability settings for the Worker.

          subdomain: Subdomain settings for the Worker.

          tags: Tags associated with the Worker.

          tail_consumers: Other Workers that should consume logs from the Worker.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/workers/workers/{worker_id}",
            body=await async_maybe_transform(
                {
                    "logpush": logpush,
                    "name": name,
                    "observability": observability,
                    "subdomain": subdomain,
                    "tags": tags,
                    "tail_consumers": tail_consumers,
                },
                worker_edit_params.WorkerEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Worker]._unwrapper,
            ),
            cast_to=cast(Type[Worker], ResultWrapper[Worker]),
        )

    async def get(
        self,
        worker_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Worker:
        """
        Get details about a specific Worker.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/workers/{worker_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Worker]._unwrapper,
            ),
            cast_to=cast(Type[Worker], ResultWrapper[Worker]),
        )


class WorkersResourceWithRawResponse:
    def __init__(self, workers: WorkersResource) -> None:
        self._workers = workers

        self.create = to_raw_response_wrapper(
            workers.create,
        )
        self.update = to_raw_response_wrapper(
            workers.update,
        )
        self.list = to_raw_response_wrapper(
            workers.list,
        )
        self.delete = to_raw_response_wrapper(
            workers.delete,
        )
        self.edit = to_raw_response_wrapper(
            workers.edit,
        )
        self.get = to_raw_response_wrapper(
            workers.get,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._workers.versions)


class AsyncWorkersResourceWithRawResponse:
    def __init__(self, workers: AsyncWorkersResource) -> None:
        self._workers = workers

        self.create = async_to_raw_response_wrapper(
            workers.create,
        )
        self.update = async_to_raw_response_wrapper(
            workers.update,
        )
        self.list = async_to_raw_response_wrapper(
            workers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workers.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            workers.edit,
        )
        self.get = async_to_raw_response_wrapper(
            workers.get,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._workers.versions)


class WorkersResourceWithStreamingResponse:
    def __init__(self, workers: WorkersResource) -> None:
        self._workers = workers

        self.create = to_streamed_response_wrapper(
            workers.create,
        )
        self.update = to_streamed_response_wrapper(
            workers.update,
        )
        self.list = to_streamed_response_wrapper(
            workers.list,
        )
        self.delete = to_streamed_response_wrapper(
            workers.delete,
        )
        self.edit = to_streamed_response_wrapper(
            workers.edit,
        )
        self.get = to_streamed_response_wrapper(
            workers.get,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._workers.versions)


class AsyncWorkersResourceWithStreamingResponse:
    def __init__(self, workers: AsyncWorkersResource) -> None:
        self._workers = workers

        self.create = async_to_streamed_response_wrapper(
            workers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            workers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workers.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            workers.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            workers.get,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._workers.versions)
