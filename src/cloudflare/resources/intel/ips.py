# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.intel import IPGetResponse, ip_get_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["IPs", "AsyncIPs"]


class IPs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPsWithRawResponse:
        return IPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPsWithStreamingResponse:
        return IPsWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        ipv4: str | NotGiven = NOT_GIVEN,
        ipv6: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPGetResponse]:
        """
        Get IP Overview

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ipv4": ipv4,
                        "ipv6": ipv6,
                    },
                    ip_get_params.IPGetParams,
                ),
                post_parser=ResultWrapper[Optional[IPGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IPGetResponse]], ResultWrapper[IPGetResponse]),
        )


class AsyncIPs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPsWithRawResponse:
        return AsyncIPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsWithStreamingResponse:
        return AsyncIPsWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        ipv4: str | NotGiven = NOT_GIVEN,
        ipv6: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPGetResponse]:
        """
        Get IP Overview

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ipv4": ipv4,
                        "ipv6": ipv6,
                    },
                    ip_get_params.IPGetParams,
                ),
                post_parser=ResultWrapper[Optional[IPGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IPGetResponse]], ResultWrapper[IPGetResponse]),
        )


class IPsWithRawResponse:
    def __init__(self, ips: IPs) -> None:
        self._ips = ips

        self.get = to_raw_response_wrapper(
            ips.get,
        )


class AsyncIPsWithRawResponse:
    def __init__(self, ips: AsyncIPs) -> None:
        self._ips = ips

        self.get = async_to_raw_response_wrapper(
            ips.get,
        )


class IPsWithStreamingResponse:
    def __init__(self, ips: IPs) -> None:
        self._ips = ips

        self.get = to_streamed_response_wrapper(
            ips.get,
        )


class AsyncIPsWithStreamingResponse:
    def __init__(self, ips: AsyncIPs) -> None:
        self._ips = ips

        self.get = async_to_streamed_response_wrapper(
            ips.get,
        )
