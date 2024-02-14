# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .consumers import Consumers, AsyncConsumers

from ...._compat import cached_property

from ....types.workers import (
    QueueUpdateResponse,
    QueueListResponse,
    QueueDeleteResponse,
    QueueGetResponse,
    QueueQueueCreateQueueResponse,
)

from typing import Type, Optional

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.workers import queue_update_params
from ....types.workers import queue_queue_create_queue_params
from .consumers import (
    Consumers,
    AsyncConsumers,
    ConsumersWithRawResponse,
    AsyncConsumersWithRawResponse,
    ConsumersWithStreamingResponse,
    AsyncConsumersWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
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
from typing import cast
from typing import cast

__all__ = ["Queues", "AsyncQueues"]


class Queues(SyncAPIResource):
    @cached_property
    def consumers(self) -> Consumers:
        return Consumers(self._client)

    @cached_property
    def with_raw_response(self) -> QueuesWithRawResponse:
        return QueuesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueuesWithStreamingResponse:
        return QueuesWithStreamingResponse(self)

    def update(
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
    ) -> Optional[QueueUpdateResponse]:
        """
        Updates a queue.

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
        return self._put(
            f"/accounts/{account_id}/workers/queues/{name}",
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
        account_id: str,
        *,
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
            f"/accounts/{account_id}/workers/queues",
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
        name: str,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return cast(
            Optional[QueueDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/workers/queues/{name}",
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
        name: str,
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
            f"/accounts/{account_id}/workers/queues/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueGetResponse]], ResultWrapper[QueueGetResponse]),
        )

    def queue_create_queue(
        self,
        account_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[QueueQueueCreateQueueResponse]:
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
            f"/accounts/{account_id}/workers/queues",
            body=maybe_transform(body, queue_queue_create_queue_params.QueueQueueCreateQueueParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueQueueCreateQueueResponse]], ResultWrapper[QueueQueueCreateQueueResponse]),
        )


class AsyncQueues(AsyncAPIResource):
    @cached_property
    def consumers(self) -> AsyncConsumers:
        return AsyncConsumers(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQueuesWithRawResponse:
        return AsyncQueuesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueuesWithStreamingResponse:
        return AsyncQueuesWithStreamingResponse(self)

    async def update(
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
    ) -> Optional[QueueUpdateResponse]:
        """
        Updates a queue.

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
        return await self._put(
            f"/accounts/{account_id}/workers/queues/{name}",
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

    async def list(
        self,
        account_id: str,
        *,
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
            f"/accounts/{account_id}/workers/queues",
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
        name: str,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return cast(
            Optional[QueueDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/workers/queues/{name}",
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
        name: str,
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
            f"/accounts/{account_id}/workers/queues/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueGetResponse]], ResultWrapper[QueueGetResponse]),
        )

    async def queue_create_queue(
        self,
        account_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[QueueQueueCreateQueueResponse]:
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
            f"/accounts/{account_id}/workers/queues",
            body=maybe_transform(body, queue_queue_create_queue_params.QueueQueueCreateQueueParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[QueueQueueCreateQueueResponse]], ResultWrapper[QueueQueueCreateQueueResponse]),
        )


class QueuesWithRawResponse:
    def __init__(self, queues: Queues) -> None:
        self._queues = queues

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
        self.queue_create_queue = to_raw_response_wrapper(
            queues.queue_create_queue,
        )

    @cached_property
    def consumers(self) -> ConsumersWithRawResponse:
        return ConsumersWithRawResponse(self._queues.consumers)


class AsyncQueuesWithRawResponse:
    def __init__(self, queues: AsyncQueues) -> None:
        self._queues = queues

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
        self.queue_create_queue = async_to_raw_response_wrapper(
            queues.queue_create_queue,
        )

    @cached_property
    def consumers(self) -> AsyncConsumersWithRawResponse:
        return AsyncConsumersWithRawResponse(self._queues.consumers)


class QueuesWithStreamingResponse:
    def __init__(self, queues: Queues) -> None:
        self._queues = queues

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
        self.queue_create_queue = to_streamed_response_wrapper(
            queues.queue_create_queue,
        )

    @cached_property
    def consumers(self) -> ConsumersWithStreamingResponse:
        return ConsumersWithStreamingResponse(self._queues.consumers)


class AsyncQueuesWithStreamingResponse:
    def __init__(self, queues: AsyncQueues) -> None:
        self._queues = queues

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
        self.queue_create_queue = async_to_streamed_response_wrapper(
            queues.queue_create_queue,
        )

    @cached_property
    def consumers(self) -> AsyncConsumersWithStreamingResponse:
        return AsyncConsumersWithStreamingResponse(self._queues.consumers)
