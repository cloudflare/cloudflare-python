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
from ....types.magic_network_monitoring.configuration import Configuration

__all__ = ["FullResource", "AsyncFullResource"]


class FullResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FullResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FullResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FullResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FullResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Lists default sampling, router IPs, warp devices, and rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/mnm/config/full",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )


class AsyncFullResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFullResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFullResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFullResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFullResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Lists default sampling, router IPs, warp devices, and rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/mnm/config/full",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Configuration]._unwrapper,
            ),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )


class FullResourceWithRawResponse:
    def __init__(self, full: FullResource) -> None:
        self._full = full

        self.get = to_raw_response_wrapper(
            full.get,
        )


class AsyncFullResourceWithRawResponse:
    def __init__(self, full: AsyncFullResource) -> None:
        self._full = full

        self.get = async_to_raw_response_wrapper(
            full.get,
        )


class FullResourceWithStreamingResponse:
    def __init__(self, full: FullResource) -> None:
        self._full = full

        self.get = to_streamed_response_wrapper(
            full.get,
        )


class AsyncFullResourceWithStreamingResponse:
    def __init__(self, full: AsyncFullResource) -> None:
        self._full = full

        self.get = async_to_streamed_response_wrapper(
            full.get,
        )
