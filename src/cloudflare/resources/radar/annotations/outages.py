# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.radar.annotations.outage_get_response import OutageGetResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type, Union

from datetime import datetime

from typing_extensions import Literal

from ....types.radar.annotations.outage_locations_response import OutageLocationsResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.radar.annotations import outage_get_params
from ....types.radar.annotations import outage_locations_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["OutagesResource", "AsyncOutagesResource"]


class OutagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OutagesResourceWithRawResponse:
        return OutagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutagesResourceWithStreamingResponse:
        return OutagesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        asn: int | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutageGetResponse:
        """
        Get latest Internet outages and anomalies.

        Args:
          asn: Single ASN as integer.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 code.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/annotations/outages",
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
                        "location": location,
                        "offset": offset,
                    },
                    outage_get_params.OutageGetParams,
                ),
                post_parser=ResultWrapper[OutageGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageGetResponse], ResultWrapper[OutageGetResponse]),
        )

    def locations(
        self,
        *,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutageLocationsResponse:
        """
        Get the number of outages for locations.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/annotations/outages/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                    },
                    outage_locations_params.OutageLocationsParams,
                ),
                post_parser=ResultWrapper[OutageLocationsResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageLocationsResponse], ResultWrapper[OutageLocationsResponse]),
        )


class AsyncOutagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOutagesResourceWithRawResponse:
        return AsyncOutagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutagesResourceWithStreamingResponse:
        return AsyncOutagesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        asn: int | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutageGetResponse:
        """
        Get latest Internet outages and anomalies.

        Args:
          asn: Single ASN as integer.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 code.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/annotations/outages",
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
                        "location": location,
                        "offset": offset,
                    },
                    outage_get_params.OutageGetParams,
                ),
                post_parser=ResultWrapper[OutageGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageGetResponse], ResultWrapper[OutageGetResponse]),
        )

    async def locations(
        self,
        *,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: str | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutageLocationsResponse:
        """
        Get the number of outages for locations.

        Args:
          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/annotations/outages/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                    },
                    outage_locations_params.OutageLocationsParams,
                ),
                post_parser=ResultWrapper[OutageLocationsResponse]._unwrapper,
            ),
            cast_to=cast(Type[OutageLocationsResponse], ResultWrapper[OutageLocationsResponse]),
        )


class OutagesResourceWithRawResponse:
    def __init__(self, outages: OutagesResource) -> None:
        self._outages = outages

        self.get = to_raw_response_wrapper(
            outages.get,
        )
        self.locations = to_raw_response_wrapper(
            outages.locations,
        )


class AsyncOutagesResourceWithRawResponse:
    def __init__(self, outages: AsyncOutagesResource) -> None:
        self._outages = outages

        self.get = async_to_raw_response_wrapper(
            outages.get,
        )
        self.locations = async_to_raw_response_wrapper(
            outages.locations,
        )


class OutagesResourceWithStreamingResponse:
    def __init__(self, outages: OutagesResource) -> None:
        self._outages = outages

        self.get = to_streamed_response_wrapper(
            outages.get,
        )
        self.locations = to_streamed_response_wrapper(
            outages.locations,
        )


class AsyncOutagesResourceWithStreamingResponse:
    def __init__(self, outages: AsyncOutagesResource) -> None:
        self._outages = outages

        self.get = async_to_streamed_response_wrapper(
            outages.get,
        )
        self.locations = async_to_streamed_response_wrapper(
            outages.locations,
        )
