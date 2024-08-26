# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .consumers import ConsumersResource, AsyncConsumersResource

from ..._compat import cached_property

from .messages import MessagesResource, AsyncMessagesResource

from ...types.queues.queue_created import QueueCreated

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options, AsyncPaginator

from ...types.queues.queue_updated import QueueUpdated

from ...types.queues.queue import Queue

from ...pagination import SyncSinglePage, AsyncSinglePage

from ...types.queues.queue_delete_response import QueueDeleteResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.queues import queue_create_params
from ...types.queues import queue_update_params
from .consumers import ConsumersResource, AsyncConsumersResource, ConsumersResourceWithRawResponse, AsyncConsumersResourceWithRawResponse, ConsumersResourceWithStreamingResponse, AsyncConsumersResourceWithStreamingResponse
from .messages import MessagesResource, AsyncMessagesResource, MessagesResourceWithRawResponse, AsyncMessagesResourceWithRawResponse, MessagesResourceWithStreamingResponse, AsyncMessagesResourceWithStreamingResponse
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

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
        return QueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueuesResourceWithStreamingResponse:
        return QueuesResourceWithStreamingResponse(self)

    def create(self,
    *,
    account_id: str,
    queue_name: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[QueueCreated]:
        """
        Creates a new queue.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/queues",
            body=maybe_transform({
                "queue_name": queue_name
            }, queue_create_params.QueueCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[QueueCreated]]._unwrapper),
            cast_to=cast(Type[Optional[QueueCreated]], ResultWrapper[QueueCreated]),
        )

    def update(self,
    queue_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[QueueUpdated]:
        """
        Updates a queue.

        Args:
          account_id: Identifier.

          queue_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not queue_id:
          raise ValueError(
            f'Expected a non-empty value for `queue_id` but received {queue_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/queues/{queue_id}",
            body=maybe_transform(body, queue_update_params.QueueUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[QueueUpdated]]._unwrapper),
            cast_to=cast(Type[Optional[QueueUpdated]], ResultWrapper[QueueUpdated]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[Queue]:
        """
        Returns the queues owned by an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/queues",
            page = SyncSinglePage[Queue],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=Queue,
        )

    def delete(self,
    queue_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[QueueDeleteResponse]:
        """
        Deletes a queue.

        Args:
          account_id: Identifier.

          queue_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not queue_id:
          raise ValueError(
            f'Expected a non-empty value for `queue_id` but received {queue_id!r}'
          )
        return cast(Optional[QueueDeleteResponse], self._delete(
            f"/accounts/{account_id}/queues/{queue_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[QueueDeleteResponse]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[QueueDeleteResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

    def get(self,
    queue_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Queue]:
        """
        Get information about a specific queue.

        Args:
          account_id: Identifier.

          queue_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not queue_id:
          raise ValueError(
            f'Expected a non-empty value for `queue_id` but received {queue_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/queues/{queue_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Queue]]._unwrapper),
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
        return AsyncQueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueuesResourceWithStreamingResponse:
        return AsyncQueuesResourceWithStreamingResponse(self)

    async def create(self,
    *,
    account_id: str,
    queue_name: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[QueueCreated]:
        """
        Creates a new queue.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/queues",
            body=await async_maybe_transform({
                "queue_name": queue_name
            }, queue_create_params.QueueCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[QueueCreated]]._unwrapper),
            cast_to=cast(Type[Optional[QueueCreated]], ResultWrapper[QueueCreated]),
        )

    async def update(self,
    queue_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[QueueUpdated]:
        """
        Updates a queue.

        Args:
          account_id: Identifier.

          queue_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not queue_id:
          raise ValueError(
            f'Expected a non-empty value for `queue_id` but received {queue_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/queues/{queue_id}",
            body=await async_maybe_transform(body, queue_update_params.QueueUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[QueueUpdated]]._unwrapper),
            cast_to=cast(Type[Optional[QueueUpdated]], ResultWrapper[QueueUpdated]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Queue, AsyncSinglePage[Queue]]:
        """
        Returns the queues owned by an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/queues",
            page = AsyncSinglePage[Queue],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=Queue,
        )

    async def delete(self,
    queue_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[QueueDeleteResponse]:
        """
        Deletes a queue.

        Args:
          account_id: Identifier.

          queue_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not queue_id:
          raise ValueError(
            f'Expected a non-empty value for `queue_id` but received {queue_id!r}'
          )
        return cast(Optional[QueueDeleteResponse], await self._delete(
            f"/accounts/{account_id}/queues/{queue_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[QueueDeleteResponse]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[QueueDeleteResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

    async def get(self,
    queue_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Queue]:
        """
        Get information about a specific queue.

        Args:
          account_id: Identifier.

          queue_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not queue_id:
          raise ValueError(
            f'Expected a non-empty value for `queue_id` but received {queue_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/queues/{queue_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Queue]]._unwrapper),
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