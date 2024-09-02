# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.radar.bgp.top.ase_get_response import AseGetResponse

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from ....._base_client import make_request_options

from typing import Type, List, Union

from datetime import datetime

from typing_extensions import Literal

from .....types.radar.bgp.top.ase_prefixes_response import AsePrefixesResponse

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.radar.bgp.top import ase_get_params
from .....types.radar.bgp.top import ase_prefixes_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AsesResource", "AsyncAsesResource"]


class AsesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsesResourceWithRawResponse:
        return AsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsesResourceWithStreamingResponse:
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
                post_parser=ResultWrapper[AsePrefixesResponse]._unwrapper,
            ),
            cast_to=cast(Type[AsePrefixesResponse], ResultWrapper[AsePrefixesResponse]),
        )


class AsyncAsesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAsesResourceWithRawResponse:
        return AsyncAsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAsesResourceWithStreamingResponse:
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
