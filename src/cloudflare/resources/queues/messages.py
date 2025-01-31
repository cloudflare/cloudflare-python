# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
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
from ...types.queues import message_ack_params, message_pull_params
from ...types.queues.message_ack_response import MessageAckResponse
from ...types.queues.message_pull_response import MessagePullResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def ack(
        self,
        queue_id: str,
        *,
        account_id: str,
        acks: Iterable[message_ack_params.Ack] | NotGiven = NOT_GIVEN,
        retries: Iterable[message_ack_params.Retry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MessageAckResponse]:
        """
        Acknowledge + Retry messages from a Queue

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
        return self._post(
            f"/accounts/{account_id}/queues/{queue_id}/messages/ack",
            body=maybe_transform(
                {
                    "acks": acks,
                    "retries": retries,
                },
                message_ack_params.MessageAckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MessageAckResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MessageAckResponse]], ResultWrapper[MessageAckResponse]),
        )

    def pull(
        self,
        queue_id: str,
        *,
        account_id: str,
        batch_size: float | NotGiven = NOT_GIVEN,
        visibility_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[MessagePullResponse]:
        """
        Pull a batch of messages from a Queue

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          batch_size: The maximum number of messages to include in a batch.

          visibility_timeout_ms: The number of milliseconds that a message is exclusively leased. After the
              timeout, the message becomes available for another attempt.

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
            f"/accounts/{account_id}/queues/{queue_id}/messages/pull",
            page=SyncSinglePage[MessagePullResponse],
            body=maybe_transform(
                {
                    "batch_size": batch_size,
                    "visibility_timeout_ms": visibility_timeout_ms,
                },
                message_pull_params.MessagePullParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MessagePullResponse,
            method="post",
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def ack(
        self,
        queue_id: str,
        *,
        account_id: str,
        acks: Iterable[message_ack_params.Ack] | NotGiven = NOT_GIVEN,
        retries: Iterable[message_ack_params.Retry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MessageAckResponse]:
        """
        Acknowledge + Retry messages from a Queue

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
        return await self._post(
            f"/accounts/{account_id}/queues/{queue_id}/messages/ack",
            body=await async_maybe_transform(
                {
                    "acks": acks,
                    "retries": retries,
                },
                message_ack_params.MessageAckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MessageAckResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MessageAckResponse]], ResultWrapper[MessageAckResponse]),
        )

    def pull(
        self,
        queue_id: str,
        *,
        account_id: str,
        batch_size: float | NotGiven = NOT_GIVEN,
        visibility_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MessagePullResponse, AsyncSinglePage[MessagePullResponse]]:
        """
        Pull a batch of messages from a Queue

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          batch_size: The maximum number of messages to include in a batch.

          visibility_timeout_ms: The number of milliseconds that a message is exclusively leased. After the
              timeout, the message becomes available for another attempt.

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
            f"/accounts/{account_id}/queues/{queue_id}/messages/pull",
            page=AsyncSinglePage[MessagePullResponse],
            body=maybe_transform(
                {
                    "batch_size": batch_size,
                    "visibility_timeout_ms": visibility_timeout_ms,
                },
                message_pull_params.MessagePullParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MessagePullResponse,
            method="post",
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.ack = to_raw_response_wrapper(
            messages.ack,
        )
        self.pull = to_raw_response_wrapper(
            messages.pull,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.ack = async_to_raw_response_wrapper(
            messages.ack,
        )
        self.pull = async_to_raw_response_wrapper(
            messages.pull,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.ack = to_streamed_response_wrapper(
            messages.ack,
        )
        self.pull = to_streamed_response_wrapper(
            messages.pull,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.ack = async_to_streamed_response_wrapper(
            messages.ack,
        )
        self.pull = async_to_streamed_response_wrapper(
            messages.pull,
        )
