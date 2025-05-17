# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.queues import purge_start_params
from ...types.queues.queue import Queue
from ...types.queues.purge_status_response import PurgeStatusResponse

__all__ = ["PurgeResource", "AsyncPurgeResource"]


class PurgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PurgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PurgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PurgeResourceWithStreamingResponse(self)

    def start(
        self,
        queue_id: str,
        *,
        account_id: str,
        delete_messages_permanently: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Queue]:
        """
        Deletes all messages from the Queue.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          delete_messages_permanently: Confimation that all messages will be deleted permanently.

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
            f"/accounts/{account_id}/queues/{queue_id}/purge",
            body=maybe_transform(
                {"delete_messages_permanently": delete_messages_permanently}, purge_start_params.PurgeStartParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Queue]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Queue]], ResultWrapper[Queue]),
        )

    def status(
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
    ) -> Optional[PurgeStatusResponse]:
        """
        Get details about a Queue's purge status.

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
        return self._get(
            f"/accounts/{account_id}/queues/{queue_id}/purge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PurgeStatusResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PurgeStatusResponse]], ResultWrapper[PurgeStatusResponse]),
        )


class AsyncPurgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPurgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPurgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPurgeResourceWithStreamingResponse(self)

    async def start(
        self,
        queue_id: str,
        *,
        account_id: str,
        delete_messages_permanently: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Queue]:
        """
        Deletes all messages from the Queue.

        Args:
          account_id: A Resource identifier.

          queue_id: A Resource identifier.

          delete_messages_permanently: Confimation that all messages will be deleted permanently.

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
            f"/accounts/{account_id}/queues/{queue_id}/purge",
            body=await async_maybe_transform(
                {"delete_messages_permanently": delete_messages_permanently}, purge_start_params.PurgeStartParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Queue]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Queue]], ResultWrapper[Queue]),
        )

    async def status(
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
    ) -> Optional[PurgeStatusResponse]:
        """
        Get details about a Queue's purge status.

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
        return await self._get(
            f"/accounts/{account_id}/queues/{queue_id}/purge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PurgeStatusResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PurgeStatusResponse]], ResultWrapper[PurgeStatusResponse]),
        )


class PurgeResourceWithRawResponse:
    def __init__(self, purge: PurgeResource) -> None:
        self._purge = purge

        self.start = to_raw_response_wrapper(
            purge.start,
        )
        self.status = to_raw_response_wrapper(
            purge.status,
        )


class AsyncPurgeResourceWithRawResponse:
    def __init__(self, purge: AsyncPurgeResource) -> None:
        self._purge = purge

        self.start = async_to_raw_response_wrapper(
            purge.start,
        )
        self.status = async_to_raw_response_wrapper(
            purge.status,
        )


class PurgeResourceWithStreamingResponse:
    def __init__(self, purge: PurgeResource) -> None:
        self._purge = purge

        self.start = to_streamed_response_wrapper(
            purge.start,
        )
        self.status = to_streamed_response_wrapper(
            purge.status,
        )


class AsyncPurgeResourceWithStreamingResponse:
    def __init__(self, purge: AsyncPurgeResource) -> None:
        self._purge = purge

        self.start = async_to_streamed_response_wrapper(
            purge.start,
        )
        self.status = async_to_streamed_response_wrapper(
            purge.status,
        )
