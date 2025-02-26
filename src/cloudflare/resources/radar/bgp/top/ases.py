# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

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
from .....types.radar.bgp.top import ase_get_params, ase_prefixes_params
from .....types.radar.bgp.top.ase_get_response import AseGetResponse
from .....types.radar.bgp.top.ase_prefixes_response import AsePrefixesResponse

__all__ = ["AsesResource", "AsyncAsesResource"]


class AsesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        prefix: List[str] | NotGiven = NOT_GIVEN,
        update_type: List[Literal["ANNOUNCEMENT", "WITHDRAWAL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AseGetResponse:
        """
        Retrieves the top autonomous systems by BGP updates (announcements only).

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          prefix: Array of BGP network prefixes.

          update_type: Array of BGP update types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/top/ases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                        "name": name,
                        "prefix": prefix,
                        "update_type": update_type,
                    },
                    ase_get_params.AseGetParams,
                ),
                post_parser=ResultWrapper[AseGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AseGetResponse], ResultWrapper[AseGetResponse]),
        )

    def prefixes(
        self,
        *,
        country: str | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsePrefixesResponse:
        """
        Retrieves the full list of autonomous systems on the global routing table
        ordered by announced prefixes count. The data comes from public BGP MRT data
        archives and updates every 2 hours.

        Args:
          country: Alpha-2 country code.

          format: Format in which results will be returned.

          limit: Maximum number of ASes to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/top/ases/prefixes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "format": format,
                        "limit": limit,
                    },
                    ase_prefixes_params.AsePrefixesParams,
                ),
                post_parser=ResultWrapper[AsePrefixesResponse]._unwrapper,
            ),
            cast_to=cast(Type[AsePrefixesResponse], ResultWrapper[AsePrefixesResponse]),
        )


class AsyncAsesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAsesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        prefix: List[str] | NotGiven = NOT_GIVEN,
        update_type: List[Literal["ANNOUNCEMENT", "WITHDRAWAL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AseGetResponse:
        """
        Retrieves the top autonomous systems by BGP updates (announcements only).

        Args:
          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          prefix: Array of BGP network prefixes.

          update_type: Array of BGP update types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/top/ases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                        "name": name,
                        "prefix": prefix,
                        "update_type": update_type,
                    },
                    ase_get_params.AseGetParams,
                ),
                post_parser=ResultWrapper[AseGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AseGetResponse], ResultWrapper[AseGetResponse]),
        )

    async def prefixes(
        self,
        *,
        country: str | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsePrefixesResponse:
        """
        Retrieves the full list of autonomous systems on the global routing table
        ordered by announced prefixes count. The data comes from public BGP MRT data
        archives and updates every 2 hours.

        Args:
          country: Alpha-2 country code.

          format: Format in which results will be returned.

          limit: Maximum number of ASes to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/top/ases/prefixes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "format": format,
                        "limit": limit,
                    },
                    ase_prefixes_params.AsePrefixesParams,
                ),
                post_parser=ResultWrapper[AsePrefixesResponse]._unwrapper,
            ),
            cast_to=cast(Type[AsePrefixesResponse], ResultWrapper[AsePrefixesResponse]),
        )


class AsesResourceWithRawResponse:
    def __init__(self, ases: AsesResource) -> None:
        self._ases = ases

        self.get = to_raw_response_wrapper(
            ases.get,
        )
        self.prefixes = to_raw_response_wrapper(
            ases.prefixes,
        )


class AsyncAsesResourceWithRawResponse:
    def __init__(self, ases: AsyncAsesResource) -> None:
        self._ases = ases

        self.get = async_to_raw_response_wrapper(
            ases.get,
        )
        self.prefixes = async_to_raw_response_wrapper(
            ases.prefixes,
        )


class AsesResourceWithStreamingResponse:
    def __init__(self, ases: AsesResource) -> None:
        self._ases = ases

        self.get = to_streamed_response_wrapper(
            ases.get,
        )
        self.prefixes = to_streamed_response_wrapper(
            ases.prefixes,
        )


class AsyncAsesResourceWithStreamingResponse:
    def __init__(self, ases: AsyncAsesResource) -> None:
        self._ases = ases

        self.get = async_to_streamed_response_wrapper(
            ases.get,
        )
        self.prefixes = async_to_streamed_response_wrapper(
            ases.prefixes,
        )
