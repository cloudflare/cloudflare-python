# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from .....types.zero_trust.dex.traceroute_test_results.network_path_get_response import NetworkPathGetResponse

__all__ = ["NetworkPathResource", "AsyncNetworkPathResource"]


class NetworkPathResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworkPathResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return NetworkPathResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkPathResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return NetworkPathResourceWithStreamingResponse(self)

    def get(
        self,
        test_result_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkPathGetResponse]:
        """
        Get a breakdown of hops and performance metrics for a specific traceroute test
        run

        Args:
          test_result_id: API Resource UUID tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not test_result_id:
            raise ValueError(f"Expected a non-empty value for `test_result_id` but received {test_result_id!r}")
        return self._get(
            f"/accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NetworkPathGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NetworkPathGetResponse]], ResultWrapper[NetworkPathGetResponse]),
        )


class AsyncNetworkPathResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworkPathResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworkPathResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkPathResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncNetworkPathResourceWithStreamingResponse(self)

    async def get(
        self,
        test_result_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NetworkPathGetResponse]:
        """
        Get a breakdown of hops and performance metrics for a specific traceroute test
        run

        Args:
          test_result_id: API Resource UUID tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not test_result_id:
            raise ValueError(f"Expected a non-empty value for `test_result_id` but received {test_result_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[NetworkPathGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[NetworkPathGetResponse]], ResultWrapper[NetworkPathGetResponse]),
        )


class NetworkPathResourceWithRawResponse:
    def __init__(self, network_path: NetworkPathResource) -> None:
        self._network_path = network_path

        self.get = to_raw_response_wrapper(
            network_path.get,
        )


class AsyncNetworkPathResourceWithRawResponse:
    def __init__(self, network_path: AsyncNetworkPathResource) -> None:
        self._network_path = network_path

        self.get = async_to_raw_response_wrapper(
            network_path.get,
        )


class NetworkPathResourceWithStreamingResponse:
    def __init__(self, network_path: NetworkPathResource) -> None:
        self._network_path = network_path

        self.get = to_streamed_response_wrapper(
            network_path.get,
        )


class AsyncNetworkPathResourceWithStreamingResponse:
    def __init__(self, network_path: AsyncNetworkPathResource) -> None:
        self._network_path = network_path

        self.get = async_to_streamed_response_wrapper(
            network_path.get,
        )
