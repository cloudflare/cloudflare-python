# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events.relate_delete_response import RelateDeleteResponse

__all__ = ["RelateResource", "AsyncRelateResource"]


class RelateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RelateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RelateResourceWithStreamingResponse(self)

    def delete(
        self,
        event_id: str,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelateDeleteResponse:
        """
        Removes an event reference

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._delete(
            f"/accounts/{account_id}/cloudforce-one/events/relate/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RelateDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RelateDeleteResponse], ResultWrapper[RelateDeleteResponse]),
        )


class AsyncRelateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRelateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRelateResourceWithStreamingResponse(self)

    async def delete(
        self,
        event_id: str,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelateDeleteResponse:
        """
        Removes an event reference

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/cloudforce-one/events/relate/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RelateDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RelateDeleteResponse], ResultWrapper[RelateDeleteResponse]),
        )


class RelateResourceWithRawResponse:
    def __init__(self, relate: RelateResource) -> None:
        self._relate = relate

        self.delete = to_raw_response_wrapper(
            relate.delete,
        )


class AsyncRelateResourceWithRawResponse:
    def __init__(self, relate: AsyncRelateResource) -> None:
        self._relate = relate

        self.delete = async_to_raw_response_wrapper(
            relate.delete,
        )


class RelateResourceWithStreamingResponse:
    def __init__(self, relate: RelateResource) -> None:
        self._relate = relate

        self.delete = to_streamed_response_wrapper(
            relate.delete,
        )


class AsyncRelateResourceWithStreamingResponse:
    def __init__(self, relate: AsyncRelateResource) -> None:
        self._relate = relate

        self.delete = async_to_streamed_response_wrapper(
            relate.delete,
        )
