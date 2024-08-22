# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.queues.consumer_create_response import ConsumerCreateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

from ...types.queues.consumer_update_response import ConsumerUpdateResponse

from ...types.queues.consumer_delete_response import ConsumerDeleteResponse

from ...types.queues.consumer_get_response import ConsumerGetResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.queues import consumer_create_params
from ...types.queues import consumer_update_params
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

__all__ = ["ConsumersResource", "AsyncConsumersResource"]

class ConsumersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConsumersResourceWithRawResponse:
        return ConsumersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsumersResourceWithStreamingResponse:
        return ConsumersResourceWithStreamingResponse(self)

    def create(self,
    queue_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConsumerCreateResponse]:
        """
        Creates a new consumer for a queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

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
        return self._post(
            f"/accounts/{account_id}/queues/{queue_id}/consumers",
            body=maybe_transform(body, consumer_create_params.ConsumerCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConsumerCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ConsumerCreateResponse]], ResultWrapper[ConsumerCreateResponse]),
        )

    def update(self,
    consumer_id: str,
    *,
    account_id: str,
    queue_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConsumerUpdateResponse]:
        """
        Updates the consumer for a queue, or creates one if it does not exist.

        Args:
          account_id: Identifier

          queue_id: Identifier

          consumer_id: Identifier

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
        if not consumer_id:
          raise ValueError(
            f'Expected a non-empty value for `consumer_id` but received {consumer_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
            body=maybe_transform(body, consumer_update_params.ConsumerUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConsumerUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ConsumerUpdateResponse]], ResultWrapper[ConsumerUpdateResponse]),
        )

    def delete(self,
    consumer_id: str,
    *,
    account_id: str,
    queue_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConsumerDeleteResponse]:
        """
        Deletes the consumer for a queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

          consumer_id: Identifier

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
        if not consumer_id:
          raise ValueError(
            f'Expected a non-empty value for `consumer_id` but received {consumer_id!r}'
          )
        return cast(Optional[ConsumerDeleteResponse], self._delete(
            f"/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConsumerDeleteResponse]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[ConsumerDeleteResponse]),  # Union types cannot be passed in as arguments in the type system
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConsumerGetResponse]:
        """
        Returns the consumers for a queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

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
            f"/accounts/{account_id}/queues/{queue_id}/consumers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConsumerGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ConsumerGetResponse]], ResultWrapper[ConsumerGetResponse]),
        )

class AsyncConsumersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConsumersResourceWithRawResponse:
        return AsyncConsumersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsumersResourceWithStreamingResponse:
        return AsyncConsumersResourceWithStreamingResponse(self)

    async def create(self,
    queue_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConsumerCreateResponse]:
        """
        Creates a new consumer for a queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

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
        return await self._post(
            f"/accounts/{account_id}/queues/{queue_id}/consumers",
            body=await async_maybe_transform(body, consumer_create_params.ConsumerCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConsumerCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ConsumerCreateResponse]], ResultWrapper[ConsumerCreateResponse]),
        )

    async def update(self,
    consumer_id: str,
    *,
    account_id: str,
    queue_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConsumerUpdateResponse]:
        """
        Updates the consumer for a queue, or creates one if it does not exist.

        Args:
          account_id: Identifier

          queue_id: Identifier

          consumer_id: Identifier

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
        if not consumer_id:
          raise ValueError(
            f'Expected a non-empty value for `consumer_id` but received {consumer_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
            body=await async_maybe_transform(body, consumer_update_params.ConsumerUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConsumerUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ConsumerUpdateResponse]], ResultWrapper[ConsumerUpdateResponse]),
        )

    async def delete(self,
    consumer_id: str,
    *,
    account_id: str,
    queue_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConsumerDeleteResponse]:
        """
        Deletes the consumer for a queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

          consumer_id: Identifier

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
        if not consumer_id:
          raise ValueError(
            f'Expected a non-empty value for `consumer_id` but received {consumer_id!r}'
          )
        return cast(Optional[ConsumerDeleteResponse], await self._delete(
            f"/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConsumerDeleteResponse]]._unwrapper),
            cast_to=cast(Any, ResultWrapper[ConsumerDeleteResponse]),  # Union types cannot be passed in as arguments in the type system
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ConsumerGetResponse]:
        """
        Returns the consumers for a queue.

        Args:
          account_id: Identifier

          queue_id: Identifier

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
            f"/accounts/{account_id}/queues/{queue_id}/consumers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ConsumerGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ConsumerGetResponse]], ResultWrapper[ConsumerGetResponse]),
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