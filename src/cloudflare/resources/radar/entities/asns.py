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
from ...._base_client import make_request_options
from ....types.radar.entities import asn_ip_params, asn_get_params, asn_rel_params, asn_list_params
from ....types.radar.entities.asn_ip_response import ASNIPResponse
from ....types.radar.entities.asn_get_response import ASNGetResponse
from ....types.radar.entities.asn_rel_response import ASNRelResponse
from ....types.radar.entities.asn_list_response import ASNListResponse

__all__ = ["ASNsResource", "AsyncASNsResource"]


class ASNsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ASNsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ASNsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ASNsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ASNsResourceWithStreamingResponse(self)

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
        Retrieves a list of autonomous systems.

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs).

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          location: Location alpha-2 code.

          offset: Skips the specified number of objects before fetching the results.

          order_by: Metric to order the ASNs by.

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
                post_parser=ResultWrapper[ASNListResponse]._unwrapper,
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
        """Retrieves the requested autonomous system information.

        (A confidence level below
        `5` indicates a low level of confidence in the traffic data - normally this
        happens because Cloudflare has a small amount of traffic from/to this AS).
        Population estimates come from APNIC (refer to https://labs.apnic.net/?p=526).

        Args:
          asn: Single Autonomous System Number (ASN) as integer.

          format: Format in which results will be returned.

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
                post_parser=ResultWrapper[ASNGetResponse]._unwrapper,
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
        """
        Retrieves the requested autonomous system information based on IP address.
        Population estimates come from APNIC (refer to https://labs.apnic.net/?p=526).

        Args:
          ip: IP address.

          format: Format in which results will be returned.

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
                post_parser=ResultWrapper[ASNIPResponse]._unwrapper,
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
        Retrieves AS-level relationship for given networks.

        Args:
          asn: Retrieves all ASNs with provider-customer or peering relationships with the
              given ASN.

          asn2: Retrieves the AS relationship of ASN2 with respect to the given ASN.

          format: Format in which results will be returned.

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
                post_parser=ResultWrapper[ASNRelResponse]._unwrapper,
            ),
            cast_to=cast(Type[ASNRelResponse], ResultWrapper[ASNRelResponse]),
        )


class AsyncASNsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncASNsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncASNsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncASNsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncASNsResourceWithStreamingResponse(self)

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
        Retrieves a list of autonomous systems.

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs).

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          location: Location alpha-2 code.

          offset: Skips the specified number of objects before fetching the results.

          order_by: Metric to order the ASNs by.

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
                post_parser=ResultWrapper[ASNListResponse]._unwrapper,
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
        """Retrieves the requested autonomous system information.

        (A confidence level below
        `5` indicates a low level of confidence in the traffic data - normally this
        happens because Cloudflare has a small amount of traffic from/to this AS).
        Population estimates come from APNIC (refer to https://labs.apnic.net/?p=526).

        Args:
          asn: Single Autonomous System Number (ASN) as integer.

          format: Format in which results will be returned.

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
                post_parser=ResultWrapper[ASNGetResponse]._unwrapper,
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
        """
        Retrieves the requested autonomous system information based on IP address.
        Population estimates come from APNIC (refer to https://labs.apnic.net/?p=526).

        Args:
          ip: IP address.

          format: Format in which results will be returned.

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
                post_parser=ResultWrapper[ASNIPResponse]._unwrapper,
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
        Retrieves AS-level relationship for given networks.

        Args:
          asn: Retrieves all ASNs with provider-customer or peering relationships with the
              given ASN.

          asn2: Retrieves the AS relationship of ASN2 with respect to the given ASN.

          format: Format in which results will be returned.

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
                post_parser=ResultWrapper[ASNRelResponse]._unwrapper,
            ),
            cast_to=cast(Type[ASNRelResponse], ResultWrapper[ASNRelResponse]),
        )


class ASNsResourceWithRawResponse:
    def __init__(self, asns: ASNsResource) -> None:
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


class AsyncASNsResourceWithRawResponse:
    def __init__(self, asns: AsyncASNsResource) -> None:
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


class ASNsResourceWithStreamingResponse:
    def __init__(self, asns: ASNsResource) -> None:
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


class AsyncASNsResourceWithStreamingResponse:
    def __init__(self, asns: AsyncASNsResource) -> None:
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
