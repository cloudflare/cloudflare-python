# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from .operations import (
    OperationsResource,
    AsyncOperationsResource,
    OperationsResourceWithRawResponse,
    AsyncOperationsResourceWithRawResponse,
    OperationsResourceWithStreamingResponse,
    AsyncOperationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.api_gateway.discovery_get_response import DiscoveryGetResponse

__all__ = ["DiscoveryResource", "AsyncDiscoveryResource"]


class DiscoveryResource(SyncAPIResource):
    @cached_property
    def operations(self) -> OperationsResource:
        return OperationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DiscoveryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DiscoveryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiscoveryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DiscoveryResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscoveryGetResponse:
        """
        Retrieve the most up to date view of discovered operations, rendered as OpenAPI
        schemas

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/discovery",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DiscoveryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DiscoveryGetResponse], ResultWrapper[DiscoveryGetResponse]),
        )


class AsyncDiscoveryResource(AsyncAPIResource):
    @cached_property
    def operations(self) -> AsyncOperationsResource:
        return AsyncOperationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDiscoveryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDiscoveryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiscoveryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDiscoveryResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscoveryGetResponse:
        """
        Retrieve the most up to date view of discovered operations, rendered as OpenAPI
        schemas

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/discovery",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DiscoveryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DiscoveryGetResponse], ResultWrapper[DiscoveryGetResponse]),
        )


class DiscoveryResourceWithRawResponse:
    def __init__(self, discovery: DiscoveryResource) -> None:
        self._discovery = discovery

        self.get = to_raw_response_wrapper(
            discovery.get,
        )

    @cached_property
    def operations(self) -> OperationsResourceWithRawResponse:
        return OperationsResourceWithRawResponse(self._discovery.operations)


class AsyncDiscoveryResourceWithRawResponse:
    def __init__(self, discovery: AsyncDiscoveryResource) -> None:
        self._discovery = discovery

        self.get = async_to_raw_response_wrapper(
            discovery.get,
        )

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithRawResponse:
        return AsyncOperationsResourceWithRawResponse(self._discovery.operations)


class DiscoveryResourceWithStreamingResponse:
    def __init__(self, discovery: DiscoveryResource) -> None:
        self._discovery = discovery

        self.get = to_streamed_response_wrapper(
            discovery.get,
        )

    @cached_property
    def operations(self) -> OperationsResourceWithStreamingResponse:
        return OperationsResourceWithStreamingResponse(self._discovery.operations)


class AsyncDiscoveryResourceWithStreamingResponse:
    def __init__(self, discovery: AsyncDiscoveryResource) -> None:
        self._discovery = discovery

        self.get = async_to_streamed_response_wrapper(
            discovery.get,
        )

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithStreamingResponse:
        return AsyncOperationsResourceWithStreamingResponse(self._discovery.operations)
