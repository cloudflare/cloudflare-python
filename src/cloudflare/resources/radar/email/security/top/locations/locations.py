# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .arc import (
    ARC,
    AsyncARC,
    ARCWithRawResponse,
    AsyncARCWithRawResponse,
    ARCWithStreamingResponse,
    AsyncARCWithStreamingResponse,
)
from .spf import (
    SPF,
    AsyncSPF,
    SPFWithRawResponse,
    AsyncSPFWithRawResponse,
    SPFWithStreamingResponse,
    AsyncSPFWithStreamingResponse,
)
from .dkim import (
    DKIM,
    AsyncDKIM,
    DKIMWithRawResponse,
    AsyncDKIMWithRawResponse,
    DKIMWithStreamingResponse,
    AsyncDKIMWithStreamingResponse,
)
from .spam import (
    Spam,
    AsyncSpam,
    SpamWithRawResponse,
    AsyncSpamWithRawResponse,
    SpamWithStreamingResponse,
    AsyncSpamWithStreamingResponse,
)
from .dmarc import (
    DMARC,
    AsyncDMARC,
    DMARCWithRawResponse,
    AsyncDMARCWithRawResponse,
    DMARCWithStreamingResponse,
    AsyncDMARCWithStreamingResponse,
)
from .malicious import (
    Malicious,
    AsyncMalicious,
    MaliciousWithRawResponse,
    AsyncMaliciousWithRawResponse,
    MaliciousWithStreamingResponse,
    AsyncMaliciousWithStreamingResponse,
)
from ......._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......._utils import maybe_transform
from ......._compat import cached_property
from ......._resource import SyncAPIResource, AsyncAPIResource
from ......._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......._wrappers import ResultWrapper
from ......._base_client import (
    make_request_options,
)
from .......types.radar.email.security.top import LocationGetResponse, location_get_params

__all__ = ["Locations", "AsyncLocations"]


class Locations(SyncAPIResource):
    @cached_property
    def arc(self) -> ARC:
        return ARC(self._client)

    @cached_property
    def dkim(self) -> DKIM:
        return DKIM(self._client)

    @cached_property
    def dmarc(self) -> DMARC:
        return DMARC(self._client)

    @cached_property
    def malicious(self) -> Malicious:
        return Malicious(self._client)

    @cached_property
    def spam(self) -> Spam:
        return Spam(self._client)

    @cached_property
    def spf(self) -> SPF:
        return SPF(self._client)

    @cached_property
    def with_raw_response(self) -> LocationsWithRawResponse:
        return LocationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsWithStreamingResponse:
        return LocationsWithStreamingResponse(self)

    def get(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
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
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationGetResponse:
        """Get the top locations by email messages.

        Values are a percentage out of the
        total emails.

        Args:
          arc: Filter for arc (Authenticated Received Chain).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/top/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "spf": spf,
                    },
                    location_get_params.LocationGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LocationGetResponse], ResultWrapper[LocationGetResponse]),
        )


class AsyncLocations(AsyncAPIResource):
    @cached_property
    def arc(self) -> AsyncARC:
        return AsyncARC(self._client)

    @cached_property
    def dkim(self) -> AsyncDKIM:
        return AsyncDKIM(self._client)

    @cached_property
    def dmarc(self) -> AsyncDMARC:
        return AsyncDMARC(self._client)

    @cached_property
    def malicious(self) -> AsyncMalicious:
        return AsyncMalicious(self._client)

    @cached_property
    def spam(self) -> AsyncSpam:
        return AsyncSpam(self._client)

    @cached_property
    def spf(self) -> AsyncSPF:
        return AsyncSPF(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLocationsWithRawResponse:
        return AsyncLocationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsWithStreamingResponse:
        return AsyncLocationsWithStreamingResponse(self)

    async def get(
        self,
        *,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
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
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocationGetResponse:
        """Get the top locations by email messages.

        Values are a percentage out of the
        total emails.

        Args:
          arc: Filter for arc (Authenticated Received Chain).

          asn: Array of comma separated list of ASNs, start with `-` to exclude from results.
              For example, `-174, 3356` excludes results from AS174, but includes results from
              AS3356.

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/top/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "arc": arc,
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "name": name,
                        "spf": spf,
                    },
                    location_get_params.LocationGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LocationGetResponse], ResultWrapper[LocationGetResponse]),
        )


class LocationsWithRawResponse:
    def __init__(self, locations: Locations) -> None:
        self._locations = locations

        self.get = to_raw_response_wrapper(
            locations.get,
        )

    @cached_property
    def arc(self) -> ARCWithRawResponse:
        return ARCWithRawResponse(self._locations.arc)

    @cached_property
    def dkim(self) -> DKIMWithRawResponse:
        return DKIMWithRawResponse(self._locations.dkim)

    @cached_property
    def dmarc(self) -> DMARCWithRawResponse:
        return DMARCWithRawResponse(self._locations.dmarc)

    @cached_property
    def malicious(self) -> MaliciousWithRawResponse:
        return MaliciousWithRawResponse(self._locations.malicious)

    @cached_property
    def spam(self) -> SpamWithRawResponse:
        return SpamWithRawResponse(self._locations.spam)

    @cached_property
    def spf(self) -> SPFWithRawResponse:
        return SPFWithRawResponse(self._locations.spf)


class AsyncLocationsWithRawResponse:
    def __init__(self, locations: AsyncLocations) -> None:
        self._locations = locations

        self.get = async_to_raw_response_wrapper(
            locations.get,
        )

    @cached_property
    def arc(self) -> AsyncARCWithRawResponse:
        return AsyncARCWithRawResponse(self._locations.arc)

    @cached_property
    def dkim(self) -> AsyncDKIMWithRawResponse:
        return AsyncDKIMWithRawResponse(self._locations.dkim)

    @cached_property
    def dmarc(self) -> AsyncDMARCWithRawResponse:
        return AsyncDMARCWithRawResponse(self._locations.dmarc)

    @cached_property
    def malicious(self) -> AsyncMaliciousWithRawResponse:
        return AsyncMaliciousWithRawResponse(self._locations.malicious)

    @cached_property
    def spam(self) -> AsyncSpamWithRawResponse:
        return AsyncSpamWithRawResponse(self._locations.spam)

    @cached_property
    def spf(self) -> AsyncSPFWithRawResponse:
        return AsyncSPFWithRawResponse(self._locations.spf)


class LocationsWithStreamingResponse:
    def __init__(self, locations: Locations) -> None:
        self._locations = locations

        self.get = to_streamed_response_wrapper(
            locations.get,
        )

    @cached_property
    def arc(self) -> ARCWithStreamingResponse:
        return ARCWithStreamingResponse(self._locations.arc)

    @cached_property
    def dkim(self) -> DKIMWithStreamingResponse:
        return DKIMWithStreamingResponse(self._locations.dkim)

    @cached_property
    def dmarc(self) -> DMARCWithStreamingResponse:
        return DMARCWithStreamingResponse(self._locations.dmarc)

    @cached_property
    def malicious(self) -> MaliciousWithStreamingResponse:
        return MaliciousWithStreamingResponse(self._locations.malicious)

    @cached_property
    def spam(self) -> SpamWithStreamingResponse:
        return SpamWithStreamingResponse(self._locations.spam)

    @cached_property
    def spf(self) -> SPFWithStreamingResponse:
        return SPFWithStreamingResponse(self._locations.spf)


class AsyncLocationsWithStreamingResponse:
    def __init__(self, locations: AsyncLocations) -> None:
        self._locations = locations

        self.get = async_to_streamed_response_wrapper(
            locations.get,
        )

    @cached_property
    def arc(self) -> AsyncARCWithStreamingResponse:
        return AsyncARCWithStreamingResponse(self._locations.arc)

    @cached_property
    def dkim(self) -> AsyncDKIMWithStreamingResponse:
        return AsyncDKIMWithStreamingResponse(self._locations.dkim)

    @cached_property
    def dmarc(self) -> AsyncDMARCWithStreamingResponse:
        return AsyncDMARCWithStreamingResponse(self._locations.dmarc)

    @cached_property
    def malicious(self) -> AsyncMaliciousWithStreamingResponse:
        return AsyncMaliciousWithStreamingResponse(self._locations.malicious)

    @cached_property
    def spam(self) -> AsyncSpamWithStreamingResponse:
        return AsyncSpamWithStreamingResponse(self._locations.spam)

    @cached_property
    def spf(self) -> AsyncSPFWithStreamingResponse:
        return AsyncSPFWithStreamingResponse(self._locations.spf)
