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
from ....._base_client import (
    make_request_options,
)
from .....types.radar.bgp.top import AseGetResponse, AsePrefixesResponse, ase_get_params, ase_prefixes_params

__all__ = ["Ases", "AsyncAses"]


class Ases(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsesWithRawResponse:
        return AsesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsesWithStreamingResponse:
        return AsesWithStreamingResponse(self)

    def get(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
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
        """Get the top autonomous systems (AS) by BGP updates (announcements only).

        Values
        are a percentage out of the total updates.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          name: Array of names that will be used to name the series in responses.

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
                post_parser=ResultWrapper._unwrapper,
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
        Get the full list of autonomous systems on the global routing table ordered by
        announced prefixes count. The data comes from public BGP MRT data archives and
        updates every 2 hours.

        Args:
          country: Alpha-2 country code.

          format: Format results are returned in.

          limit: Maximum number of ASes to return

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AsePrefixesResponse], ResultWrapper[AsePrefixesResponse]),
        )


class AsyncAses(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAsesWithRawResponse:
        return AsyncAsesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAsesWithStreamingResponse:
        return AsyncAsesWithStreamingResponse(self)

    async def get(
        self,
        *,
        asn: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
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
        """Get the top autonomous systems (AS) by BGP updates (announcements only).

        Values
        are a percentage out of the total updates.

        Args:
          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          name: Array of names that will be used to name the series in responses.

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
                post_parser=ResultWrapper._unwrapper,
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
        Get the full list of autonomous systems on the global routing table ordered by
        announced prefixes count. The data comes from public BGP MRT data archives and
        updates every 2 hours.

        Args:
          country: Alpha-2 country code.

          format: Format results are returned in.

          limit: Maximum number of ASes to return

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AsePrefixesResponse], ResultWrapper[AsePrefixesResponse]),
        )


class AsesWithRawResponse:
    def __init__(self, ases: Ases) -> None:
        self._ases = ases

        self.get = to_raw_response_wrapper(
            ases.get,
        )
        self.prefixes = to_raw_response_wrapper(
            ases.prefixes,
        )


class AsyncAsesWithRawResponse:
    def __init__(self, ases: AsyncAses) -> None:
        self._ases = ases

        self.get = async_to_raw_response_wrapper(
            ases.get,
        )
        self.prefixes = async_to_raw_response_wrapper(
            ases.prefixes,
        )


class AsesWithStreamingResponse:
    def __init__(self, ases: Ases) -> None:
        self._ases = ases

        self.get = to_streamed_response_wrapper(
            ases.get,
        )
        self.prefixes = to_streamed_response_wrapper(
            ases.prefixes,
        )


class AsyncAsesWithStreamingResponse:
    def __init__(self, ases: AsyncAses) -> None:
        self._ases = ases

        self.get = async_to_streamed_response_wrapper(
            ases.get,
        )
        self.prefixes = async_to_streamed_response_wrapper(
            ases.prefixes,
        )
