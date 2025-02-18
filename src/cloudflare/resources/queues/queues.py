# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .consumers import (
    ConsumersResource,
    AsyncConsumersResource,
    ConsumersResourceWithRawResponse,
    AsyncConsumersResourceWithRawResponse,
    ConsumersResourceWithStreamingResponse,
    AsyncConsumersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.queues import queue_create_params, queue_update_params
from ...types.queues.queue import Queue
from ...types.queues.queue_delete_response import QueueDeleteResponse

__all__ = ["QueuesResource", "AsyncQueuesResource"]


class QueuesResource(SyncAPIResource):
    @cached_property
    def consumers(self) -> ConsumersResource:
        return ConsumersResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> QueuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return QueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return QueuesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        queue_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Queue]:
        """
        Create a new queue

        Args:
          account_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/queues",
            body=maybe_transform({"queue_name": queue_name}, queue_create_params.QueueCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Queue]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Queue]], ResultWrapper[Queue]),
        )

    def update(
        self,
        queue_id: str,
        *,
        account_id: str,
        queue_name: str | NotGiven = NOT_GIVEN,
        settings: queue_update_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Queue]:
        """Updates a Queue.

        Note that this endpoint does not support partial updates. If
        successful, the Queue's configuration is overwritten with the supplied
        configuration.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._put(
            f"/accounts/{account_id}/queues/{queue_id}",
            body=maybe_transform(
                {
                    "queue_name": queue_name,
                    "settings": settings,
                },
                queue_update_params.QueueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Queue]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Queue]], ResultWrapper[Queue]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Queue]:
        """
        Returns the queues owned by an account.

        Args:
          account_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/queues",
            page=SyncSinglePage[Queue],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Queue,
        )

    def delete(
        self,
        queue_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueueDeleteResponse:
        """
        Deletes a queue

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._delete(
            f"/accounts/{account_id}/queues/{queue_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueDeleteResponse,
        )

    def get(
        self,
        queue_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Queue]:
        """
        Get details about a specific queue.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._get(
            f"/accounts/{account_id}/queues/{queue_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Queue]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Queue]], ResultWrapper[Queue]),
        )


class AsyncQueuesResource(AsyncAPIResource):
    @cached_property
    def consumers(self) -> AsyncConsumersResource:
        return AsyncConsumersResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQueuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncQueuesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        queue_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Queue]:
        """
        Create a new queue

        Args:
          account_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/queues",
            body=await async_maybe_transform({"queue_name": queue_name}, queue_create_params.QueueCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Queue]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Queue]], ResultWrapper[Queue]),
        )

    async def update(
        self,
        queue_id: str,
        *,
        account_id: str,
        queue_name: str | NotGiven = NOT_GIVEN,
        settings: queue_update_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Queue]:
        """Updates a Queue.

        Note that this endpoint does not support partial updates. If
        successful, the Queue's configuration is overwritten with the supplied
        configuration.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return await self._put(
            f"/accounts/{account_id}/queues/{queue_id}",
            body=await async_maybe_transform(
                {
                    "queue_name": queue_name,
                    "settings": settings,
                },
                queue_update_params.QueueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Queue]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Queue]], ResultWrapper[Queue]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Queue, AsyncSinglePage[Queue]]:
        """
        Returns the queues owned by an account.

        Args:
          account_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/queues",
            page=AsyncSinglePage[Queue],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Queue,
        )

    async def delete(
        self,
        queue_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueueDeleteResponse:
        """
        Deletes a queue

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/queues/{queue_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueDeleteResponse,
        )

    async def get(
        self,
        queue_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Queue]:
        """
        Get details about a specific queue.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return await self._get(
            f"/accounts/{account_id}/queues/{queue_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Queue]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Queue]], ResultWrapper[Queue]),
        )


class QueuesResourceWithRawResponse:
    def __init__(self, queues: QueuesResource) -> None:
        self._queues = queues

        self.create = to_raw_response_wrapper(
            queues.create,
        )
        self.update = to_raw_response_wrapper(
            queues.update,
        )
        self.list = to_raw_response_wrapper(
            queues.list,
        )
        self.delete = to_raw_response_wrapper(
            queues.delete,
        )
        self.get = to_raw_response_wrapper(
            queues.get,
        )

    @cached_property
    def consumers(self) -> ConsumersResourceWithRawResponse:
        return ConsumersResourceWithRawResponse(self._queues.consumers)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._queues.messages)


class AsyncQueuesResourceWithRawResponse:
    def __init__(self, queues: AsyncQueuesResource) -> None:
        self._queues = queues

        self.create = async_to_raw_response_wrapper(
            queues.create,
        )
        self.update = async_to_raw_response_wrapper(
            queues.update,
        )
        self.list = async_to_raw_response_wrapper(
            queues.list,
        )
        self.delete = async_to_raw_response_wrapper(
            queues.delete,
        )
        self.get = async_to_raw_response_wrapper(
            queues.get,
        )

    @cached_property
    def consumers(self) -> AsyncConsumersResourceWithRawResponse:
        return AsyncConsumersResourceWithRawResponse(self._queues.consumers)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._queues.messages)


class QueuesResourceWithStreamingResponse:
    def __init__(self, queues: QueuesResource) -> None:
        self._queues = queues

        self.create = to_streamed_response_wrapper(
            queues.create,
        )
        self.update = to_streamed_response_wrapper(
            queues.update,
        )
        self.list = to_streamed_response_wrapper(
            queues.list,
        )
        self.delete = to_streamed_response_wrapper(
            queues.delete,
        )
        self.get = to_streamed_response_wrapper(
            queues.get,
        )

    @cached_property
    def consumers(self) -> ConsumersResourceWithStreamingResponse:
        return ConsumersResourceWithStreamingResponse(self._queues.consumers)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._queues.messages)


class AsyncQueuesResourceWithStreamingResponse:
    def __init__(self, queues: AsyncQueuesResource) -> None:
        self._queues = queues

        self.create = async_to_streamed_response_wrapper(
            queues.create,
        )
        self.update = async_to_streamed_response_wrapper(
            queues.update,
        )
        self.list = async_to_streamed_response_wrapper(
            queues.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            queues.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            queues.get,
        )

    @cached_property
    def consumers(self) -> AsyncConsumersResourceWithStreamingResponse:
        return AsyncConsumersResourceWithStreamingResponse(self._queues.consumers)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._queues.messages)
