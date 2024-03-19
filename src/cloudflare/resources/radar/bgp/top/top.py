# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .ases import (
    Ases,
    AsyncAses,
    AsesWithRawResponse,
    AsyncAsesWithRawResponse,
    AsesWithStreamingResponse,
    AsyncAsesWithStreamingResponse,
)
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
from .....types.radar.bgp import TopPrefixesResponse, top_prefixes_params

__all__ = ["Top", "AsyncTop"]


class Top(SyncAPIResource):
    @cached_property
    def ases(self) -> Ases:
        return Ases(self._client)

    @cached_property
    def with_raw_response(self) -> TopWithRawResponse:
        return TopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self)

    def prefixes(
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
        update_type: List[Literal["ANNOUNCEMENT", "WITHDRAWAL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopPrefixesResponse:
        """Get the top network prefixes by BGP updates.

        Values are a percentage out of the
        total BGP updates.

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

          update_type: Array of BGP update types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/top/prefixes",
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
                        "update_type": update_type,
                    },
                    top_prefixes_params.TopPrefixesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TopPrefixesResponse], ResultWrapper[TopPrefixesResponse]),
        )


class AsyncTop(AsyncAPIResource):
    @cached_property
    def ases(self) -> AsyncAses:
        return AsyncAses(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self)

    async def prefixes(
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
        update_type: List[Literal["ANNOUNCEMENT", "WITHDRAWAL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopPrefixesResponse:
        """Get the top network prefixes by BGP updates.

        Values are a percentage out of the
        total BGP updates.

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

          update_type: Array of BGP update types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/top/prefixes",
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
                        "update_type": update_type,
                    },
                    top_prefixes_params.TopPrefixesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TopPrefixesResponse], ResultWrapper[TopPrefixesResponse]),
        )


class TopWithRawResponse:
    def __init__(self, top: Top) -> None:
        self._top = top

        self.prefixes = to_raw_response_wrapper(
            top.prefixes,
        )

    @cached_property
    def ases(self) -> AsesWithRawResponse:
        return AsesWithRawResponse(self._top.ases)


class AsyncTopWithRawResponse:
    def __init__(self, top: AsyncTop) -> None:
        self._top = top

        self.prefixes = async_to_raw_response_wrapper(
            top.prefixes,
        )

    @cached_property
    def ases(self) -> AsyncAsesWithRawResponse:
        return AsyncAsesWithRawResponse(self._top.ases)


class TopWithStreamingResponse:
    def __init__(self, top: Top) -> None:
        self._top = top

        self.prefixes = to_streamed_response_wrapper(
            top.prefixes,
        )

    @cached_property
    def ases(self) -> AsesWithStreamingResponse:
        return AsesWithStreamingResponse(self._top.ases)


class AsyncTopWithStreamingResponse:
    def __init__(self, top: AsyncTop) -> None:
        self._top = top

        self.prefixes = async_to_streamed_response_wrapper(
            top.prefixes,
        )

    @cached_property
    def ases(self) -> AsyncAsesWithStreamingResponse:
        return AsyncAsesWithStreamingResponse(self._top.ases)
