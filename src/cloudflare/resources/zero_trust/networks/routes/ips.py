# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
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
from .....types.zero_trust.networks.routes import ip_get_params
from .....types.zero_trust.networks.teamnet import Teamnet

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

    def get(
        self,
        ip: str,
        *,
        account_id: str,
        default_virtual_network_fallback: bool | NotGiven = NOT_GIVEN,
        virtual_network_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Teamnet:
        """
        Fetches routes that contain the given IP address.

        Args:
          account_id: Cloudflare account ID

          default_virtual_network_fallback: When the virtual_network_id parameter is not provided the request filter will
              default search routes that are in the default virtual network for the account.
              If this parameter is set to false, the search will include routes that do not
              have a virtual network.

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ip:
            raise ValueError(f"Expected a non-empty value for `ip` but received {ip!r}")
        return self._get(
            f"/accounts/{account_id}/teamnet/routes/ip/{ip}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "default_virtual_network_fallback": default_virtual_network_fallback,
                        "virtual_network_id": virtual_network_id,
                    },
                    ip_get_params.IPGetParams,
                ),
                post_parser=ResultWrapper[Teamnet]._unwrapper,
            ),
            cast_to=cast(Type[Teamnet], ResultWrapper[Teamnet]),
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

    async def get(
        self,
        ip: str,
        *,
        account_id: str,
        default_virtual_network_fallback: bool | NotGiven = NOT_GIVEN,
        virtual_network_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Teamnet:
        """
        Fetches routes that contain the given IP address.

        Args:
          account_id: Cloudflare account ID

          default_virtual_network_fallback: When the virtual_network_id parameter is not provided the request filter will
              default search routes that are in the default virtual network for the account.
              If this parameter is set to false, the search will include routes that do not
              have a virtual network.

          virtual_network_id: UUID of the virtual network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ip:
            raise ValueError(f"Expected a non-empty value for `ip` but received {ip!r}")
        return await self._get(
            f"/accounts/{account_id}/teamnet/routes/ip/{ip}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "default_virtual_network_fallback": default_virtual_network_fallback,
                        "virtual_network_id": virtual_network_id,
                    },
                    ip_get_params.IPGetParams,
                ),
                post_parser=ResultWrapper[Teamnet]._unwrapper,
            ),
            cast_to=cast(Type[Teamnet], ResultWrapper[Teamnet]),
        )


class IPsResourceWithRawResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.get = to_raw_response_wrapper(
            ips.get,
        )


class AsyncIPsResourceWithRawResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.get = async_to_raw_response_wrapper(
            ips.get,
        )


class IPsResourceWithStreamingResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.get = to_streamed_response_wrapper(
            ips.get,
        )


class AsyncIPsResourceWithStreamingResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.get = async_to_streamed_response_wrapper(
            ips.get,
        )
