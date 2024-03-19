# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
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
from ....types.radar.entities import (
    ASNIPResponse,
    ASNGetResponse,
    ASNRelResponse,
    ASNListResponse,
    asn_ip_params,
    asn_get_params,
    asn_rel_params,
    asn_list_params,
)

__all__ = ["ASNs", "AsyncASNs"]


class ASNs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ASNsWithRawResponse:
        return ASNsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ASNsWithStreamingResponse:
        return ASNsWithStreamingResponse(self)

    def list(
        self,
        *,
        asn: str | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: Literal["ASN", "POPULATION"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ASNListResponse:
        """
        Gets a list of autonomous systems (AS).

        Args:
          asn: Comma separated list of ASNs.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 to filter results.

          offset: Number of objects to skip before grabbing results.

          order_by: Order asn list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/entities/asns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    asn_list_params.ASNListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ASNListResponse], ResultWrapper[ASNListResponse]),
        )

    def get(
        self,
        asn: int,
        *,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ASNGetResponse:
        """Get the requested autonomous system information.

        A confidence level below `5`
        indicates a low level of confidence in the traffic data - normally this happens
        because Cloudflare has a small amount of traffic from/to this AS). Population
        estimates come from APNIC (refer to https://labs.apnic.net/?p=526).

        Args:
          asn: Autonomous System Number (ASN).

          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/radar/entities/asns/{asn}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, asn_get_params.ASNGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ASNGetResponse], ResultWrapper[ASNGetResponse]),
        )

    def ip(
        self,
        *,
        ip: str,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ASNIPResponse:
        """Get the requested autonomous system information based on IP address.

        Population
        estimates come from APNIC (refer to https://labs.apnic.net/?p=526).

        Args:
          ip: IP address.

          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/entities/asns/ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ip": ip,
                        "format": format,
                    },
                    asn_ip_params.ASNIPParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ASNIPResponse], ResultWrapper[ASNIPResponse]),
        )

    def rel(
        self,
        asn: int,
        *,
        asn2: int | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ASNRelResponse:
        """
        Get AS-level relationship for given networks.

        Args:
          asn: Get all ASNs with provider-customer or peering relationships with the given ASN

          asn2: Get the AS relationship of ASN2 with respect to the given ASN

          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/radar/entities/asns/{asn}/rel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn2": asn2,
                        "format": format,
                    },
                    asn_rel_params.ASNRelParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ASNRelResponse], ResultWrapper[ASNRelResponse]),
        )


class AsyncASNs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncASNsWithRawResponse:
        return AsyncASNsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncASNsWithStreamingResponse:
        return AsyncASNsWithStreamingResponse(self)

    async def list(
        self,
        *,
        asn: str | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: Literal["ASN", "POPULATION"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ASNListResponse:
        """
        Gets a list of autonomous systems (AS).

        Args:
          asn: Comma separated list of ASNs.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 to filter results.

          offset: Number of objects to skip before grabbing results.

          order_by: Order asn list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/entities/asns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    asn_list_params.ASNListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ASNListResponse], ResultWrapper[ASNListResponse]),
        )

    async def get(
        self,
        asn: int,
        *,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ASNGetResponse:
        """Get the requested autonomous system information.

        A confidence level below `5`
        indicates a low level of confidence in the traffic data - normally this happens
        because Cloudflare has a small amount of traffic from/to this AS). Population
        estimates come from APNIC (refer to https://labs.apnic.net/?p=526).

        Args:
          asn: Autonomous System Number (ASN).

          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/radar/entities/asns/{asn}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, asn_get_params.ASNGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ASNGetResponse], ResultWrapper[ASNGetResponse]),
        )

    async def ip(
        self,
        *,
        ip: str,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ASNIPResponse:
        """Get the requested autonomous system information based on IP address.

        Population
        estimates come from APNIC (refer to https://labs.apnic.net/?p=526).

        Args:
          ip: IP address.

          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/entities/asns/ip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ip": ip,
                        "format": format,
                    },
                    asn_ip_params.ASNIPParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ASNIPResponse], ResultWrapper[ASNIPResponse]),
        )

    async def rel(
        self,
        asn: int,
        *,
        asn2: int | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ASNRelResponse:
        """
        Get AS-level relationship for given networks.

        Args:
          asn: Get all ASNs with provider-customer or peering relationships with the given ASN

          asn2: Get the AS relationship of ASN2 with respect to the given ASN

          format: Format results are returned in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/radar/entities/asns/{asn}/rel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn2": asn2,
                        "format": format,
                    },
                    asn_rel_params.ASNRelParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ASNRelResponse], ResultWrapper[ASNRelResponse]),
        )


class ASNsWithRawResponse:
    def __init__(self, asns: ASNs) -> None:
        self._asns = asns

        self.list = to_raw_response_wrapper(
            asns.list,
        )
        self.get = to_raw_response_wrapper(
            asns.get,
        )
        self.ip = to_raw_response_wrapper(
            asns.ip,
        )
        self.rel = to_raw_response_wrapper(
            asns.rel,
        )


class AsyncASNsWithRawResponse:
    def __init__(self, asns: AsyncASNs) -> None:
        self._asns = asns

        self.list = async_to_raw_response_wrapper(
            asns.list,
        )
        self.get = async_to_raw_response_wrapper(
            asns.get,
        )
        self.ip = async_to_raw_response_wrapper(
            asns.ip,
        )
        self.rel = async_to_raw_response_wrapper(
            asns.rel,
        )


class ASNsWithStreamingResponse:
    def __init__(self, asns: ASNs) -> None:
        self._asns = asns

        self.list = to_streamed_response_wrapper(
            asns.list,
        )
        self.get = to_streamed_response_wrapper(
            asns.get,
        )
        self.ip = to_streamed_response_wrapper(
            asns.ip,
        )
        self.rel = to_streamed_response_wrapper(
            asns.rel,
        )


class AsyncASNsWithStreamingResponse:
    def __init__(self, asns: AsyncASNs) -> None:
        self._asns = asns

        self.list = async_to_streamed_response_wrapper(
            asns.list,
        )
        self.get = async_to_streamed_response_wrapper(
            asns.get,
        )
        self.ip = async_to_streamed_response_wrapper(
            asns.ip,
        )
        self.rel = async_to_streamed_response_wrapper(
            asns.rel,
        )
