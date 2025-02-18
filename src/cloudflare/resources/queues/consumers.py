# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
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
from ...types.queues import consumer_create_params, consumer_update_params
from ...types.queues.consumer import Consumer
from ...types.queues.consumer_delete_response import ConsumerDeleteResponse

__all__ = ["ConsumersResource", "AsyncConsumersResource"]


class ConsumersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConsumersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConsumersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsumersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConsumersResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        queue_id: str,
        *,
        account_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        script_name: str | NotGiven = NOT_GIVEN,
        settings: consumer_create_params.MqWorkerConsumerSettings | NotGiven = NOT_GIVEN,
        type: Literal["worker"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        """
        Creates a new consumer for a Queue

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          script_name: Name of a Worker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        queue_id: str,
        *,
        account_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        settings: consumer_create_params.MqHTTPConsumerSettings | NotGiven = NOT_GIVEN,
        type: Literal["http_pull"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        """
        Creates a new consumer for a Queue

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"])
    def create(
        self,
        queue_id: str,
        *,
        account_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        script_name: str | NotGiven = NOT_GIVEN,
        settings: consumer_create_params.MqWorkerConsumerSettings
        | consumer_create_params.MqHTTPConsumerSettings
        | NotGiven = NOT_GIVEN,
        type: Literal["worker"] | Literal["http_pull"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return cast(
            Optional[Consumer],
            self._post(
                f"/accounts/{account_id}/queues/{queue_id}/consumers",
                body=maybe_transform(
                    {
                        "dead_letter_queue": dead_letter_queue,
                        "script_name": script_name,
                        "settings": settings,
                        "type": type,
                    },
                    consumer_create_params.ConsumerCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Consumer]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Consumer]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        consumer_id: str,
        *,
        account_id: str,
        queue_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        script_name: str | NotGiven = NOT_GIVEN,
        settings: consumer_update_params.MqWorkerConsumerSettings | NotGiven = NOT_GIVEN,
        type: Literal["worker"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        """
        Updates the consumer for a queue, or creates one if it does not exist.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          consumer_id: A Resource identifier.

          script_name: Name of a Worker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        consumer_id: str,
        *,
        account_id: str,
        queue_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        settings: consumer_update_params.MqHTTPConsumerSettings | NotGiven = NOT_GIVEN,
        type: Literal["http_pull"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        """
        Updates the consumer for a queue, or creates one if it does not exist.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          consumer_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "queue_id"])
    def update(
        self,
        consumer_id: str,
        *,
        account_id: str,
        queue_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        script_name: str | NotGiven = NOT_GIVEN,
        settings: consumer_update_params.MqWorkerConsumerSettings
        | consumer_update_params.MqHTTPConsumerSettings
        | NotGiven = NOT_GIVEN,
        type: Literal["worker"] | Literal["http_pull"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not consumer_id:
            raise ValueError(f"Expected a non-empty value for `consumer_id` but received {consumer_id!r}")
        return cast(
            Optional[Consumer],
            self._put(
                f"/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
                body=maybe_transform(
                    {
                        "dead_letter_queue": dead_letter_queue,
                        "script_name": script_name,
                        "settings": settings,
                        "type": type,
                    },
                    consumer_update_params.ConsumerUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Consumer]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Consumer]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        consumer_id: str,
        *,
        account_id: str,
        queue_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConsumerDeleteResponse:
        """
        Deletes the consumer for a queue.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          consumer_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not consumer_id:
            raise ValueError(f"Expected a non-empty value for `consumer_id` but received {consumer_id!r}")
        return self._delete(
            f"/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsumerDeleteResponse,
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
    ) -> SyncSinglePage[Consumer]:
        """
        Returns the consumers for a Queue

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
        return self._get_api_list(
            f"/accounts/{account_id}/queues/{queue_id}/consumers",
            page=SyncSinglePage[Consumer],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, Consumer),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncConsumersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConsumersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConsumersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsumersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConsumersResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        queue_id: str,
        *,
        account_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        script_name: str | NotGiven = NOT_GIVEN,
        settings: consumer_create_params.MqWorkerConsumerSettings | NotGiven = NOT_GIVEN,
        type: Literal["worker"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        """
        Creates a new consumer for a Queue

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          script_name: Name of a Worker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        queue_id: str,
        *,
        account_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        settings: consumer_create_params.MqHTTPConsumerSettings | NotGiven = NOT_GIVEN,
        type: Literal["http_pull"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        """
        Creates a new consumer for a Queue

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"])
    async def create(
        self,
        queue_id: str,
        *,
        account_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        script_name: str | NotGiven = NOT_GIVEN,
        settings: consumer_create_params.MqWorkerConsumerSettings
        | consumer_create_params.MqHTTPConsumerSettings
        | NotGiven = NOT_GIVEN,
        type: Literal["worker"] | Literal["http_pull"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return cast(
            Optional[Consumer],
            await self._post(
                f"/accounts/{account_id}/queues/{queue_id}/consumers",
                body=await async_maybe_transform(
                    {
                        "dead_letter_queue": dead_letter_queue,
                        "script_name": script_name,
                        "settings": settings,
                        "type": type,
                    },
                    consumer_create_params.ConsumerCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Consumer]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Consumer]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        consumer_id: str,
        *,
        account_id: str,
        queue_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        script_name: str | NotGiven = NOT_GIVEN,
        settings: consumer_update_params.MqWorkerConsumerSettings | NotGiven = NOT_GIVEN,
        type: Literal["worker"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        """
        Updates the consumer for a queue, or creates one if it does not exist.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          consumer_id: A Resource identifier.

          script_name: Name of a Worker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        consumer_id: str,
        *,
        account_id: str,
        queue_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        settings: consumer_update_params.MqHTTPConsumerSettings | NotGiven = NOT_GIVEN,
        type: Literal["http_pull"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        """
        Updates the consumer for a queue, or creates one if it does not exist.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          consumer_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "queue_id"])
    async def update(
        self,
        consumer_id: str,
        *,
        account_id: str,
        queue_id: str,
        dead_letter_queue: str | NotGiven = NOT_GIVEN,
        script_name: str | NotGiven = NOT_GIVEN,
        settings: consumer_update_params.MqWorkerConsumerSettings
        | consumer_update_params.MqHTTPConsumerSettings
        | NotGiven = NOT_GIVEN,
        type: Literal["worker"] | Literal["http_pull"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Consumer]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not consumer_id:
            raise ValueError(f"Expected a non-empty value for `consumer_id` but received {consumer_id!r}")
        return cast(
            Optional[Consumer],
            await self._put(
                f"/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
                body=await async_maybe_transform(
                    {
                        "dead_letter_queue": dead_letter_queue,
                        "script_name": script_name,
                        "settings": settings,
                        "type": type,
                    },
                    consumer_update_params.ConsumerUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Consumer]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Consumer]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        consumer_id: str,
        *,
        account_id: str,
        queue_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConsumerDeleteResponse:
        """
        Deletes the consumer for a queue.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          consumer_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not consumer_id:
            raise ValueError(f"Expected a non-empty value for `consumer_id` but received {consumer_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsumerDeleteResponse,
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
    ) -> AsyncPaginator[Consumer, AsyncSinglePage[Consumer]]:
        """
        Returns the consumers for a Queue

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
        return self._get_api_list(
            f"/accounts/{account_id}/queues/{queue_id}/consumers",
            page=AsyncSinglePage[Consumer],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, Consumer),  # Union types cannot be passed in as arguments in the type system
        )


class ConsumersResourceWithRawResponse:
    def __init__(self, consumers: ConsumersResource) -> None:
        self._consumers = consumers

        self.create = to_raw_response_wrapper(
            consumers.create,
        )
        self.update = to_raw_response_wrapper(
            consumers.update,
        )
        self.delete = to_raw_response_wrapper(
            consumers.delete,
        )
        self.get = to_raw_response_wrapper(
            consumers.get,
        )


class AsyncConsumersResourceWithRawResponse:
    def __init__(self, consumers: AsyncConsumersResource) -> None:
        self._consumers = consumers

        self.create = async_to_raw_response_wrapper(
            consumers.create,
        )
        self.update = async_to_raw_response_wrapper(
            consumers.update,
        )
        self.delete = async_to_raw_response_wrapper(
            consumers.delete,
        )
        self.get = async_to_raw_response_wrapper(
            consumers.get,
        )


class ConsumersResourceWithStreamingResponse:
    def __init__(self, consumers: ConsumersResource) -> None:
        self._consumers = consumers

        self.create = to_streamed_response_wrapper(
            consumers.create,
        )
        self.update = to_streamed_response_wrapper(
            consumers.update,
        )
        self.delete = to_streamed_response_wrapper(
            consumers.delete,
        )
        self.get = to_streamed_response_wrapper(
            consumers.get,
        )


class AsyncConsumersResourceWithStreamingResponse:
    def __init__(self, consumers: AsyncConsumersResource) -> None:
        self._consumers = consumers

        self.create = async_to_streamed_response_wrapper(
            consumers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            consumers.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            consumers.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            consumers.get,
        )
