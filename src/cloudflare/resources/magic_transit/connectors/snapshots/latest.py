# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .....types.magic_transit.connectors.snapshots.latest_list_response import LatestListResponse

__all__ = ["LatestResource", "AsyncLatestResource"]


class LatestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LatestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LatestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LatestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LatestResourceWithStreamingResponse(self)

    def list(
        self,
        connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LatestListResponse:
        """
        Get latest Snapshots

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LatestListResponse]._unwrapper,
            ),
            cast_to=cast(Type[LatestListResponse], ResultWrapper[LatestListResponse]),
        )


class AsyncLatestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLatestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLatestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLatestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLatestResourceWithStreamingResponse(self)

    async def list(
        self,
        connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LatestListResponse:
        """
        Get latest Snapshots

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LatestListResponse]._unwrapper,
            ),
            cast_to=cast(Type[LatestListResponse], ResultWrapper[LatestListResponse]),
        )


class LatestResourceWithRawResponse:
    def __init__(self, latest: LatestResource) -> None:
        self._latest = latest

        self.list = to_raw_response_wrapper(
            latest.list,
        )


class AsyncLatestResourceWithRawResponse:
    def __init__(self, latest: AsyncLatestResource) -> None:
        self._latest = latest

        self.list = async_to_raw_response_wrapper(
            latest.list,
        )


class LatestResourceWithStreamingResponse:
    def __init__(self, latest: LatestResource) -> None:
        self._latest = latest

        self.list = to_streamed_response_wrapper(
            latest.list,
        )


class AsyncLatestResourceWithStreamingResponse:
    def __init__(self, latest: AsyncLatestResource) -> None:
        self._latest = latest

        self.list = async_to_streamed_response_wrapper(
            latest.list,
        )
