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
from ..._base_client import make_request_options
from ...types.queues import message_ack_params, message_pull_params
from ...types.queues.message_ack_response import MessageAckResponse
from ...types.queues.message_pull_response import MessagePullResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
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
        Acknowledge + Retry messages from a Queue.

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
        visibility_timeout: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MessagePullResponse]:
        """
        Pull a batch of messages from a Queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

          batch_size: The maximum number of messages to include in a batch.

          visibility_timeout: The number of milliseconds that a message is exclusively leased. After the
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
        return self._post(
            f"/accounts/{account_id}/queues/{queue_id}/messages/pull",
            body=maybe_transform(
                {
                    "batch_size": batch_size,
                    "visibility_timeout": visibility_timeout,
                },
                message_pull_params.MessagePullParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MessagePullResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MessagePullResponse]], ResultWrapper[MessagePullResponse]),
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
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
        Acknowledge + Retry messages from a Queue.

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

    async def pull(
        self,
        queue_id: str,
        *,
        account_id: str,
        batch_size: float | NotGiven = NOT_GIVEN,
        visibility_timeout: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MessagePullResponse]:
        """
        Pull a batch of messages from a Queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

          batch_size: The maximum number of messages to include in a batch.

          visibility_timeout: The number of milliseconds that a message is exclusively leased. After the
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
        return await self._post(
            f"/accounts/{account_id}/queues/{queue_id}/messages/pull",
            body=await async_maybe_transform(
                {
                    "batch_size": batch_size,
                    "visibility_timeout": visibility_timeout,
                },
                message_pull_params.MessagePullParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MessagePullResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MessagePullResponse]], ResultWrapper[MessagePullResponse]),
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
