# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.workers.queues import (
    ConsumerListResponse,
    ConsumerDeleteResponse,
    ConsumerUpdateResponse,
    ConsumerQueueCreateQueueConsumerResponse,
    consumer_update_params,
    consumer_queue_create_queue_consumer_params,
)

__all__ = ["Consumers", "AsyncConsumers"]


class Consumers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConsumersWithRawResponse:
        return ConsumersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsumersWithStreamingResponse:
        return ConsumersWithStreamingResponse(self)

    def update(
        self,
        consumer_name: str,
        *,
        account_id: str,
        name: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConsumerUpdateResponse]:
        """
        Updates the consumer for a queue, or creates one if it does not exist.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not consumer_name:
            raise ValueError(f"Expected a non-empty value for `consumer_name` but received {consumer_name!r}")
        return self._put(
            f"/accounts/{account_id}/workers/queues/{name}/consumers/{consumer_name}",
            body=maybe_transform(body, consumer_update_params.ConsumerUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConsumerUpdateResponse]], ResultWrapper[ConsumerUpdateResponse]),
        )

    def list(
        self,
        name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConsumerListResponse]:
        """
        Returns the consumers for a queue.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/queues/{name}/consumers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConsumerListResponse]], ResultWrapper[ConsumerListResponse]),
        )

    def delete(
        self,
        consumer_name: str,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConsumerDeleteResponse]:
        """
        Deletes the consumer for a queue.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not consumer_name:
            raise ValueError(f"Expected a non-empty value for `consumer_name` but received {consumer_name!r}")
        return cast(
            Optional[ConsumerDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/workers/queues/{name}/consumers/{consumer_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConsumerDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def queue_create_queue_consumer(
        self,
        name: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConsumerQueueCreateQueueConsumerResponse]:
        """
        Creates a new consumer for a queue.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._post(
            f"/accounts/{account_id}/workers/queues/{name}/consumers",
            body=maybe_transform(
                body, consumer_queue_create_queue_consumer_params.ConsumerQueueCreateQueueConsumerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConsumerQueueCreateQueueConsumerResponse]],
                ResultWrapper[ConsumerQueueCreateQueueConsumerResponse],
            ),
        )


class AsyncConsumers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConsumersWithRawResponse:
        return AsyncConsumersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsumersWithStreamingResponse:
        return AsyncConsumersWithStreamingResponse(self)

    async def update(
        self,
        consumer_name: str,
        *,
        account_id: str,
        name: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConsumerUpdateResponse]:
        """
        Updates the consumer for a queue, or creates one if it does not exist.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not consumer_name:
            raise ValueError(f"Expected a non-empty value for `consumer_name` but received {consumer_name!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/queues/{name}/consumers/{consumer_name}",
            body=maybe_transform(body, consumer_update_params.ConsumerUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConsumerUpdateResponse]], ResultWrapper[ConsumerUpdateResponse]),
        )

    async def list(
        self,
        name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConsumerListResponse]:
        """
        Returns the consumers for a queue.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/queues/{name}/consumers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConsumerListResponse]], ResultWrapper[ConsumerListResponse]),
        )

    async def delete(
        self,
        consumer_name: str,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConsumerDeleteResponse]:
        """
        Deletes the consumer for a queue.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        if not consumer_name:
            raise ValueError(f"Expected a non-empty value for `consumer_name` but received {consumer_name!r}")
        return cast(
            Optional[ConsumerDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/workers/queues/{name}/consumers/{consumer_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConsumerDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def queue_create_queue_consumer(
        self,
        name: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConsumerQueueCreateQueueConsumerResponse]:
        """
        Creates a new consumer for a queue.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._post(
            f"/accounts/{account_id}/workers/queues/{name}/consumers",
            body=maybe_transform(
                body, consumer_queue_create_queue_consumer_params.ConsumerQueueCreateQueueConsumerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConsumerQueueCreateQueueConsumerResponse]],
                ResultWrapper[ConsumerQueueCreateQueueConsumerResponse],
            ),
        )


class ConsumersWithRawResponse:
    def __init__(self, consumers: Consumers) -> None:
        self._consumers = consumers

        self.update = to_raw_response_wrapper(
            consumers.update,
        )
        self.list = to_raw_response_wrapper(
            consumers.list,
        )
        self.delete = to_raw_response_wrapper(
            consumers.delete,
        )
        self.queue_create_queue_consumer = to_raw_response_wrapper(
            consumers.queue_create_queue_consumer,
        )


class AsyncConsumersWithRawResponse:
    def __init__(self, consumers: AsyncConsumers) -> None:
        self._consumers = consumers

        self.update = async_to_raw_response_wrapper(
            consumers.update,
        )
        self.list = async_to_raw_response_wrapper(
            consumers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            consumers.delete,
        )
        self.queue_create_queue_consumer = async_to_raw_response_wrapper(
            consumers.queue_create_queue_consumer,
        )


class ConsumersWithStreamingResponse:
    def __init__(self, consumers: Consumers) -> None:
        self._consumers = consumers

        self.update = to_streamed_response_wrapper(
            consumers.update,
        )
        self.list = to_streamed_response_wrapper(
            consumers.list,
        )
        self.delete = to_streamed_response_wrapper(
            consumers.delete,
        )
        self.queue_create_queue_consumer = to_streamed_response_wrapper(
            consumers.queue_create_queue_consumer,
        )


class AsyncConsumersWithStreamingResponse:
    def __init__(self, consumers: AsyncConsumers) -> None:
        self._consumers = consumers

        self.update = async_to_streamed_response_wrapper(
            consumers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            consumers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            consumers.delete,
        )
        self.queue_create_queue_consumer = async_to_streamed_response_wrapper(
            consumers.queue_create_queue_consumer,
        )
