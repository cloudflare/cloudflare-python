# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.event_notifications.r2.configuration.queue_update_response import QueueUpdateResponse

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from ....._base_client import make_request_options

from typing import Type, Iterable

from .....types.event_notifications.r2.configuration.queue_delete_response import QueueDeleteResponse

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from .....types.event_notifications.r2.configuration import queue_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.event_notifications.r2.configuration import queue_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["QueuesResource", "AsyncQueuesResource"]


class QueuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueuesResourceWithRawResponse:
        return QueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueuesResourceWithStreamingResponse:
        return QueuesResourceWithStreamingResponse(self)

    def update(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        rules: Iterable[queue_update_params.Rule] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueueUpdateResponse:
        """
        Define the rules for a given queue which will determine event notification
        production.

        Args:
          account_id: Identifier.

          bucket_name: Identifier.

          queue_id: Identifier.

          rules: Array of rules to drive notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._put(
            f"/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
            body=maybe_transform({"rules": rules}, queue_update_params.QueueUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[QueueUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[QueueUpdateResponse], ResultWrapper[QueueUpdateResponse]),
        )

    def delete(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueueDeleteResponse:
        """Turn off all event notifications configured for delivery to a given queue.

        No
        further notifications will be produced for the queue once complete.

        Args:
          account_id: Identifier.

          bucket_name: Identifier.

          queue_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return cast(
            QueueDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[QueueDeleteResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[QueueDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncQueuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueuesResourceWithRawResponse:
        return AsyncQueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueuesResourceWithStreamingResponse:
        return AsyncQueuesResourceWithStreamingResponse(self)

    async def update(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        rules: Iterable[queue_update_params.Rule] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueueUpdateResponse:
        """
        Define the rules for a given queue which will determine event notification
        production.

        Args:
          account_id: Identifier.

          bucket_name: Identifier.

          queue_id: Identifier.

          rules: Array of rules to drive notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return await self._put(
            f"/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
            body=await async_maybe_transform({"rules": rules}, queue_update_params.QueueUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[QueueUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[QueueUpdateResponse], ResultWrapper[QueueUpdateResponse]),
        )

    async def delete(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueueDeleteResponse:
        """Turn off all event notifications configured for delivery to a given queue.

        No
        further notifications will be produced for the queue once complete.

        Args:
          account_id: Identifier.

          bucket_name: Identifier.

          queue_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return cast(
            QueueDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[QueueDeleteResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[QueueDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class QueuesResourceWithRawResponse:
    def __init__(self, queues: QueuesResource) -> None:
        self._queues = queues

        self.update = to_raw_response_wrapper(
            queues.update,
        )
        self.delete = to_raw_response_wrapper(
            queues.delete,
        )


class AsyncQueuesResourceWithRawResponse:
    def __init__(self, queues: AsyncQueuesResource) -> None:
        self._queues = queues

        self.update = async_to_raw_response_wrapper(
            queues.update,
        )
        self.delete = async_to_raw_response_wrapper(
            queues.delete,
        )


class QueuesResourceWithStreamingResponse:
    def __init__(self, queues: QueuesResource) -> None:
        self._queues = queues

        self.update = to_streamed_response_wrapper(
            queues.update,
        )
        self.delete = to_streamed_response_wrapper(
            queues.delete,
        )


class AsyncQueuesResourceWithStreamingResponse:
    def __init__(self, queues: AsyncQueuesResource) -> None:
        self._queues = queues

        self.update = async_to_streamed_response_wrapper(
            queues.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            queues.delete,
        )
