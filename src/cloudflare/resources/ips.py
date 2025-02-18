# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from ..types.ips import ip_list_params
from .._base_client import make_request_options
from ..types.ips.ip_list_response import IPListResponse

__all__ = ["IPsResource", "AsyncIPsResource"]


class IPsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IPsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        networks: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPListResponse]:
        """
        Get IPs used on the Cloudflare/JD Cloud network, see
        https://www.cloudflare.com/ips for Cloudflare IPs or
        https://developers.cloudflare.com/china-network/reference/infrastructure/ for JD
        Cloud IPs.

        Args:
          networks: Specified as `jdcloud` to list IPs used by JD Cloud data centers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Optional[IPListResponse],
            self._get(
                "/ips",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"networks": networks}, ip_list_params.IPListParams),
                    post_parser=ResultWrapper[Optional[IPListResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IPListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncIPsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIPsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        networks: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPListResponse]:
        """
        Get IPs used on the Cloudflare/JD Cloud network, see
        https://www.cloudflare.com/ips for Cloudflare IPs or
        https://developers.cloudflare.com/china-network/reference/infrastructure/ for JD
        Cloud IPs.

        Args:
          networks: Specified as `jdcloud` to list IPs used by JD Cloud data centers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Optional[IPListResponse],
            await self._get(
                "/ips",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform({"networks": networks}, ip_list_params.IPListParams),
                    post_parser=ResultWrapper[Optional[IPListResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IPListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class IPsResourceWithRawResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.list = to_raw_response_wrapper(
            ips.list,
        )


class AsyncIPsResourceWithRawResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.list = async_to_raw_response_wrapper(
            ips.list,
        )


class IPsResourceWithStreamingResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.list = to_streamed_response_wrapper(
            ips.list,
        )


class AsyncIPsResourceWithStreamingResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.list = async_to_streamed_response_wrapper(
            ips.list,
        )
