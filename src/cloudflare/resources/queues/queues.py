# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from ...types import (
    QueueGetResponse,
    QueueListResponse,
    QueueCreateResponse,
    QueueDeleteResponse,
    QueueUpdateResponse,
    queue_create_params,
    queue_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .messages import (
    Messages,
    AsyncMessages,
    MessagesWithRawResponse,
    AsyncMessagesWithRawResponse,
    MessagesWithStreamingResponse,
    AsyncMessagesWithStreamingResponse,
)
from ..._compat import cached_property
from .consumers import (
    Consumers,
    AsyncConsumers,
    ConsumersWithRawResponse,
    AsyncConsumersWithRawResponse,
    ConsumersWithStreamingResponse,
    AsyncConsumersWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)

__all__ = ["Queues", "AsyncQueues"]


class Queues(SyncAPIResource):
    @cached_property
    def consumers(self) -> Consumers:
        return Consumers(self._client)

    @cached_property
    def messages(self) -> Messages:
        return Messages(self._client)

    @cached_property
    def with_raw_response(self) -> QueuesWithRawResponse:
        return QueuesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueuesWithStreamingResponse:
        return QueuesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[QueueCreateResponse]:
        """
        Creates a new queue.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/queues",
            body=maybe_transform(body, queue_create_params.QueueCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueCreateResponse]], ResultWrapper[QueueCreateResponse]),
        )

    def update(
        self,
        queue_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[QueueUpdateResponse]:
        """
        Updates a queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

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
            body=maybe_transform(body, queue_update_params.QueueUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueUpdateResponse]], ResultWrapper[QueueUpdateResponse]),
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
    ) -> Optional[QueueListResponse]:
        """
        Returns the queues owned by an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/queues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueListResponse]], ResultWrapper[QueueListResponse]),
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
    ) -> Optional[QueueDeleteResponse]:
        """
        Deletes a queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return cast(
            Optional[QueueDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/queues/{queue_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[QueueDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> Optional[QueueGetResponse]:
        """
        Get information about a specific queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueGetResponse]], ResultWrapper[QueueGetResponse]),
        )


class AsyncQueues(AsyncAPIResource):
    @cached_property
    def consumers(self) -> AsyncConsumers:
        return AsyncConsumers(self._client)

    @cached_property
    def messages(self) -> AsyncMessages:
        return AsyncMessages(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQueuesWithRawResponse:
        return AsyncQueuesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueuesWithStreamingResponse:
        return AsyncQueuesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[QueueCreateResponse]:
        """
        Creates a new queue.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/queues",
            body=await async_maybe_transform(body, queue_create_params.QueueCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueCreateResponse]], ResultWrapper[QueueCreateResponse]),
        )

    async def update(
        self,
        queue_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[QueueUpdateResponse]:
        """
        Updates a queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

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
            body=await async_maybe_transform(body, queue_update_params.QueueUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueUpdateResponse]], ResultWrapper[QueueUpdateResponse]),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[QueueListResponse]:
        """
        Returns the queues owned by an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/queues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueListResponse]], ResultWrapper[QueueListResponse]),
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
    ) -> Optional[QueueDeleteResponse]:
        """
        Deletes a queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return cast(
            Optional[QueueDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/queues/{queue_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[QueueDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> Optional[QueueGetResponse]:
        """
        Get information about a specific queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueGetResponse]], ResultWrapper[QueueGetResponse]),
        )


class QueuesWithRawResponse:
    def __init__(self, queues: Queues) -> None:
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
    def consumers(self) -> ConsumersWithRawResponse:
        return ConsumersWithRawResponse(self._queues.consumers)

    @cached_property
    def messages(self) -> MessagesWithRawResponse:
        return MessagesWithRawResponse(self._queues.messages)


class AsyncQueuesWithRawResponse:
    def __init__(self, queues: AsyncQueues) -> None:
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
    def consumers(self) -> AsyncConsumersWithRawResponse:
        return AsyncConsumersWithRawResponse(self._queues.consumers)

    @cached_property
    def messages(self) -> AsyncMessagesWithRawResponse:
        return AsyncMessagesWithRawResponse(self._queues.messages)


class QueuesWithStreamingResponse:
    def __init__(self, queues: Queues) -> None:
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
    def consumers(self) -> ConsumersWithStreamingResponse:
        return ConsumersWithStreamingResponse(self._queues.consumers)

    @cached_property
    def messages(self) -> MessagesWithStreamingResponse:
        return MessagesWithStreamingResponse(self._queues.messages)


class AsyncQueuesWithStreamingResponse:
    def __init__(self, queues: AsyncQueues) -> None:
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
    def consumers(self) -> AsyncConsumersWithStreamingResponse:
        return AsyncConsumersWithStreamingResponse(self._queues.consumers)

    @cached_property
    def messages(self) -> AsyncMessagesWithStreamingResponse:
        return AsyncMessagesWithStreamingResponse(self._queues.messages)
