# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.r2.event_notifications.configuration import queue_update_params

__all__ = ["QueuesResource", "AsyncQueuesResource"]


class QueuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return QueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return QueuesResourceWithStreamingResponse(self)

    def update(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        rules: Iterable[queue_update_params.Rule] | NotGiven = NOT_GIVEN,
        cf_r2_jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create event notification rule.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          queue_id: Queue ID

          rules: Array of rules to drive notifications

          cf_r2_jurisdiction: The bucket jurisdiction

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
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else NOT_GIVEN}
            ),
            **(extra_headers or {}),
        }
        return self._put(
            f"/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
            body=maybe_transform({"rules": rules}, queue_update_params.QueueUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def delete(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        cf_r2_jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete an event notification rule.

        **If no body is provided, all rules for
        specified queue will be deleted**.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          queue_id: Queue ID

          cf_r2_jurisdiction: The bucket jurisdiction

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
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else NOT_GIVEN}
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            f"/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncQueuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncQueuesResourceWithStreamingResponse(self)

    async def update(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        rules: Iterable[queue_update_params.Rule] | NotGiven = NOT_GIVEN,
        cf_r2_jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create event notification rule.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          queue_id: Queue ID

          rules: Array of rules to drive notifications

          cf_r2_jurisdiction: The bucket jurisdiction

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
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else NOT_GIVEN}
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            f"/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
            body=await async_maybe_transform({"rules": rules}, queue_update_params.QueueUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def delete(
        self,
        queue_id: str,
        *,
        account_id: str,
        bucket_name: str,
        cf_r2_jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete an event notification rule.

        **If no body is provided, all rules for
        specified queue will be deleted**.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          queue_id: Queue ID

          cf_r2_jurisdiction: The bucket jurisdiction

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
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else NOT_GIVEN}
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            f"/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
