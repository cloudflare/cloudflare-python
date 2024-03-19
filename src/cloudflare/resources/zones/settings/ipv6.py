# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import ZonesIPV6, ipv6_edit_params

__all__ = ["IPV6", "AsyncIPV6"]


class IPV6(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPV6WithRawResponse:
        return IPV6WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPV6WithStreamingResponse:
        return IPV6WithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesIPV6]:
        """
        Enable IPv6 on all subdomains that are Cloudflare enabled.
        (https://support.cloudflare.com/hc/en-us/articles/200168586).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/ipv6",
            body=maybe_transform({"value": value}, ipv6_edit_params.IPV6EditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesIPV6]], ResultWrapper[ZonesIPV6]),
        )

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
    ) -> Optional[ZonesIPV6]:
        """
        Enable IPv6 on all subdomains that are Cloudflare enabled.
        (https://support.cloudflare.com/hc/en-us/articles/200168586).

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
            f"/zones/{zone_id}/settings/ipv6",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesIPV6]], ResultWrapper[ZonesIPV6]),
        )


class AsyncIPV6(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPV6WithRawResponse:
        return AsyncIPV6WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPV6WithStreamingResponse:
        return AsyncIPV6WithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesIPV6]:
        """
        Enable IPv6 on all subdomains that are Cloudflare enabled.
        (https://support.cloudflare.com/hc/en-us/articles/200168586).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/ipv6",
            body=await async_maybe_transform({"value": value}, ipv6_edit_params.IPV6EditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesIPV6]], ResultWrapper[ZonesIPV6]),
        )

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
    ) -> Optional[ZonesIPV6]:
        """
        Enable IPv6 on all subdomains that are Cloudflare enabled.
        (https://support.cloudflare.com/hc/en-us/articles/200168586).

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
            f"/zones/{zone_id}/settings/ipv6",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesIPV6]], ResultWrapper[ZonesIPV6]),
        )


class IPV6WithRawResponse:
    def __init__(self, ipv6: IPV6) -> None:
        self._ipv6 = ipv6

        self.edit = to_raw_response_wrapper(
            ipv6.edit,
        )
        self.get = to_raw_response_wrapper(
            ipv6.get,
        )


class AsyncIPV6WithRawResponse:
    def __init__(self, ipv6: AsyncIPV6) -> None:
        self._ipv6 = ipv6

        self.edit = async_to_raw_response_wrapper(
            ipv6.edit,
        )
        self.get = async_to_raw_response_wrapper(
            ipv6.get,
        )


class IPV6WithStreamingResponse:
    def __init__(self, ipv6: IPV6) -> None:
        self._ipv6 = ipv6

        self.edit = to_streamed_response_wrapper(
            ipv6.edit,
        )
        self.get = to_streamed_response_wrapper(
            ipv6.get,
        )


class AsyncIPV6WithStreamingResponse:
    def __init__(self, ipv6: AsyncIPV6) -> None:
        self._ipv6 = ipv6

        self.edit = async_to_streamed_response_wrapper(
            ipv6.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            ipv6.get,
        )
