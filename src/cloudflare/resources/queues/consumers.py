# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
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
        account_id: str | None = None,
        script_name: str,
        type: Literal["worker"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_create_params.MqWorkerConsumerRequestSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        account_id: str | None = None,
        type: Literal["http_pull"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_create_params.MqHTTPConsumerRequestSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @required_args(["script_name", "type"], ["type"])
    def create(
        self,
        queue_id: str,
        *,
        account_id: str | None = None,
        script_name: str | Omit = omit,
        type: Literal["worker"] | Literal["http_pull"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_create_params.MqWorkerConsumerRequestSettings
        | consumer_create_params.MqHTTPConsumerRequestSettings
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Consumer]:
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return cast(
            Optional[Consumer],
            self._post(
                path_template(
                    "/accounts/{account_id}/queues/{queue_id}/consumers", account_id=account_id, queue_id=queue_id
                ),
                body=maybe_transform(
                    {
                        "script_name": script_name,
                        "type": type,
                        "dead_letter_queue": dead_letter_queue,
                        "settings": settings,
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
        account_id: str | None = None,
        queue_id: str,
        script_name: str,
        type: Literal["worker"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_update_params.MqWorkerConsumerRequestSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        account_id: str | None = None,
        queue_id: str,
        type: Literal["http_pull"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_update_params.MqHTTPConsumerRequestSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @required_args(["queue_id", "script_name", "type"], ["queue_id", "type"])
    def update(
        self,
        consumer_id: str,
        *,
        account_id: str | None = None,
        queue_id: str,
        script_name: str | Omit = omit,
        type: Literal["worker"] | Literal["http_pull"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_update_params.MqWorkerConsumerRequestSettings
        | consumer_update_params.MqHTTPConsumerRequestSettings
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Consumer]:
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not consumer_id:
            raise ValueError(f"Expected a non-empty value for `consumer_id` but received {consumer_id!r}")
        return cast(
            Optional[Consumer],
            self._put(
                path_template(
                    "/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
                    account_id=account_id,
                    queue_id=queue_id,
                    consumer_id=consumer_id,
                ),
                body=maybe_transform(
                    {
                        "script_name": script_name,
                        "type": type,
                        "dead_letter_queue": dead_letter_queue,
                        "settings": settings,
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

    def list(
        self,
        queue_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/queues/{queue_id}/consumers", account_id=account_id, queue_id=queue_id
            ),
            page=SyncSinglePage[Consumer],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, Consumer),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        consumer_id: str,
        *,
        account_id: str | None = None,
        queue_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not consumer_id:
            raise ValueError(f"Expected a non-empty value for `consumer_id` but received {consumer_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
                account_id=account_id,
                queue_id=queue_id,
                consumer_id=consumer_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsumerDeleteResponse,
        )

    def get(
        self,
        consumer_id: str,
        *,
        account_id: str | None = None,
        queue_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Consumer]:
        """
        Fetches the consumer for a queue by consumer id

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          consumer_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not consumer_id:
            raise ValueError(f"Expected a non-empty value for `consumer_id` but received {consumer_id!r}")
        return cast(
            Optional[Consumer],
            self._get(
                path_template(
                    "/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
                    account_id=account_id,
                    queue_id=queue_id,
                    consumer_id=consumer_id,
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
        account_id: str | None = None,
        script_name: str,
        type: Literal["worker"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_create_params.MqWorkerConsumerRequestSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        account_id: str | None = None,
        type: Literal["http_pull"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_create_params.MqHTTPConsumerRequestSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @required_args(["script_name", "type"], ["type"])
    async def create(
        self,
        queue_id: str,
        *,
        account_id: str | None = None,
        script_name: str | Omit = omit,
        type: Literal["worker"] | Literal["http_pull"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_create_params.MqWorkerConsumerRequestSettings
        | consumer_create_params.MqHTTPConsumerRequestSettings
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Consumer]:
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return cast(
            Optional[Consumer],
            await self._post(
                path_template(
                    "/accounts/{account_id}/queues/{queue_id}/consumers", account_id=account_id, queue_id=queue_id
                ),
                body=await async_maybe_transform(
                    {
                        "script_name": script_name,
                        "type": type,
                        "dead_letter_queue": dead_letter_queue,
                        "settings": settings,
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
        account_id: str | None = None,
        queue_id: str,
        script_name: str,
        type: Literal["worker"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_update_params.MqWorkerConsumerRequestSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        account_id: str | None = None,
        queue_id: str,
        type: Literal["http_pull"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_update_params.MqHTTPConsumerRequestSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @required_args(["queue_id", "script_name", "type"], ["queue_id", "type"])
    async def update(
        self,
        consumer_id: str,
        *,
        account_id: str | None = None,
        queue_id: str,
        script_name: str | Omit = omit,
        type: Literal["worker"] | Literal["http_pull"],
        dead_letter_queue: str | Omit = omit,
        settings: consumer_update_params.MqWorkerConsumerRequestSettings
        | consumer_update_params.MqHTTPConsumerRequestSettings
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Consumer]:
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not consumer_id:
            raise ValueError(f"Expected a non-empty value for `consumer_id` but received {consumer_id!r}")
        return cast(
            Optional[Consumer],
            await self._put(
                path_template(
                    "/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
                    account_id=account_id,
                    queue_id=queue_id,
                    consumer_id=consumer_id,
                ),
                body=await async_maybe_transform(
                    {
                        "script_name": script_name,
                        "type": type,
                        "dead_letter_queue": dead_letter_queue,
                        "settings": settings,
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

    def list(
        self,
        queue_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/queues/{queue_id}/consumers", account_id=account_id, queue_id=queue_id
            ),
            page=AsyncSinglePage[Consumer],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(Any, Consumer),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        consumer_id: str,
        *,
        account_id: str | None = None,
        queue_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not consumer_id:
            raise ValueError(f"Expected a non-empty value for `consumer_id` but received {consumer_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
                account_id=account_id,
                queue_id=queue_id,
                consumer_id=consumer_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConsumerDeleteResponse,
        )

    async def get(
        self,
        consumer_id: str,
        *,
        account_id: str | None = None,
        queue_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Consumer]:
        """
        Fetches the consumer for a queue by consumer id

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          consumer_id: A Resource identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        if not consumer_id:
            raise ValueError(f"Expected a non-empty value for `consumer_id` but received {consumer_id!r}")
        return cast(
            Optional[Consumer],
            await self._get(
                path_template(
                    "/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
                    account_id=account_id,
                    queue_id=queue_id,
                    consumer_id=consumer_id,
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


class ConsumersResourceWithRawResponse:
    def __init__(self, consumers: ConsumersResource) -> None:
        self._consumers = consumers

        self.create = to_raw_response_wrapper(
            consumers.create,
        )
        self.update = to_raw_response_wrapper(
            consumers.update,
        )
        self.list = to_raw_response_wrapper(
            consumers.list,
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
        self.list = async_to_raw_response_wrapper(
            consumers.list,
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
        self.list = to_streamed_response_wrapper(
            consumers.list,
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
        self.list = async_to_streamed_response_wrapper(
            consumers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            consumers.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            consumers.get,
        )
