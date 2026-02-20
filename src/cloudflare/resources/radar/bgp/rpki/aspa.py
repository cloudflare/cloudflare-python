# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
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
from .....types.radar.bgp.rpki import aspa_changes_params, aspa_snapshot_params, aspa_timeseries_params
from .....types.radar.bgp.rpki.aspa_changes_response import ASPAChangesResponse
from .....types.radar.bgp.rpki.aspa_snapshot_response import ASPASnapshotResponse
from .....types.radar.bgp.rpki.aspa_timeseries_response import ASPATimeseriesResponse

__all__ = ["ASPAResource", "AsyncASPAResource"]


class ASPAResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ASPAResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ASPAResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ASPAResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ASPAResourceWithStreamingResponse(self)

    def changes(
        self,
        *,
        asn: int | Omit = omit,
        date_end: Union[str, datetime] | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        include_asn_info: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ASPAChangesResponse:
        """
        Retrieves ASPA (Autonomous System Provider Authorization) changes over time.
        Returns daily aggregated changes including additions, removals, and
        modifications of ASPA objects.

        Args:
          asn: Filter changes involving this ASN (as customer or provider).

          date_end: End of the date range (inclusive).

          date_start: Start of the date range (inclusive).

          format: Format in which results will be returned.

          include_asn_info: Include ASN metadata (name, country) in response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/rpki/aspa/changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_start": date_start,
                        "format": format,
                        "include_asn_info": include_asn_info,
                    },
                    aspa_changes_params.ASPAChangesParams,
                ),
                post_parser=ResultWrapper[ASPAChangesResponse]._unwrapper,
            ),
            cast_to=cast(Type[ASPAChangesResponse], ResultWrapper[ASPAChangesResponse]),
        )

    def snapshot(
        self,
        *,
        customer_asn: int | Omit = omit,
        date: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        include_asn_info: bool | Omit = omit,
        provider_asn: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ASPASnapshotResponse:
        """
        Retrieves current or historical ASPA (Autonomous System Provider Authorization)
        objects. ASPA objects define which ASNs are authorized upstream providers for a
        customer ASN.

        Args:
          customer_asn: Filter by customer ASN (the ASN publishing the ASPA object).

          date: Filters results by the specified datetime (ISO 8601).

          format: Format in which results will be returned.

          include_asn_info: Include ASN metadata (name, country) in response.

          provider_asn: Filter by provider ASN (an authorized upstream provider in ASPA objects).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/rpki/aspa/snapshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_asn": customer_asn,
                        "date": date,
                        "format": format,
                        "include_asn_info": include_asn_info,
                        "provider_asn": provider_asn,
                    },
                    aspa_snapshot_params.ASPASnapshotParams,
                ),
                post_parser=ResultWrapper[ASPASnapshotResponse]._unwrapper,
            ),
            cast_to=cast(Type[ASPASnapshotResponse], ResultWrapper[ASPASnapshotResponse]),
        )

    def timeseries(
        self,
        *,
        date_end: Union[str, datetime] | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        rir: List[Literal["RIPE_NCC", "ARIN", "APNIC", "LACNIC", "AFRINIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ASPATimeseriesResponse:
        """Retrieves ASPA (Autonomous System Provider Authorization) object count over
        time.

        Supports filtering by RIR or location (country code) to generate multiple
        named series. If no RIR or location filter is specified, returns total count.

        Args:
          date_end: End of the date range (inclusive).

          date_start: Start of the date range (inclusive).

          format: Format in which results will be returned.

          location: Filters results by location. Specify a comma-separated list of alpha-2 location
              codes.

          name: Array of names used to label the series in the response.

          rir: Filter by Regional Internet Registry (RIR). Multiple RIRs generate multiple
              series.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/bgp/rpki/aspa/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                        "rir": rir,
                    },
                    aspa_timeseries_params.ASPATimeseriesParams,
                ),
                post_parser=ResultWrapper[ASPATimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[ASPATimeseriesResponse], ResultWrapper[ASPATimeseriesResponse]),
        )


class AsyncASPAResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncASPAResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncASPAResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncASPAResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncASPAResourceWithStreamingResponse(self)

    async def changes(
        self,
        *,
        asn: int | Omit = omit,
        date_end: Union[str, datetime] | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        include_asn_info: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ASPAChangesResponse:
        """
        Retrieves ASPA (Autonomous System Provider Authorization) changes over time.
        Returns daily aggregated changes including additions, removals, and
        modifications of ASPA objects.

        Args:
          asn: Filter changes involving this ASN (as customer or provider).

          date_end: End of the date range (inclusive).

          date_start: Start of the date range (inclusive).

          format: Format in which results will be returned.

          include_asn_info: Include ASN metadata (name, country) in response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/rpki/aspa/changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_start": date_start,
                        "format": format,
                        "include_asn_info": include_asn_info,
                    },
                    aspa_changes_params.ASPAChangesParams,
                ),
                post_parser=ResultWrapper[ASPAChangesResponse]._unwrapper,
            ),
            cast_to=cast(Type[ASPAChangesResponse], ResultWrapper[ASPAChangesResponse]),
        )

    async def snapshot(
        self,
        *,
        customer_asn: int | Omit = omit,
        date: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        include_asn_info: bool | Omit = omit,
        provider_asn: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ASPASnapshotResponse:
        """
        Retrieves current or historical ASPA (Autonomous System Provider Authorization)
        objects. ASPA objects define which ASNs are authorized upstream providers for a
        customer ASN.

        Args:
          customer_asn: Filter by customer ASN (the ASN publishing the ASPA object).

          date: Filters results by the specified datetime (ISO 8601).

          format: Format in which results will be returned.

          include_asn_info: Include ASN metadata (name, country) in response.

          provider_asn: Filter by provider ASN (an authorized upstream provider in ASPA objects).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/rpki/aspa/snapshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "customer_asn": customer_asn,
                        "date": date,
                        "format": format,
                        "include_asn_info": include_asn_info,
                        "provider_asn": provider_asn,
                    },
                    aspa_snapshot_params.ASPASnapshotParams,
                ),
                post_parser=ResultWrapper[ASPASnapshotResponse]._unwrapper,
            ),
            cast_to=cast(Type[ASPASnapshotResponse], ResultWrapper[ASPASnapshotResponse]),
        )

    async def timeseries(
        self,
        *,
        date_end: Union[str, datetime] | Omit = omit,
        date_start: Union[str, datetime] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        rir: List[Literal["RIPE_NCC", "ARIN", "APNIC", "LACNIC", "AFRINIC"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ASPATimeseriesResponse:
        """Retrieves ASPA (Autonomous System Provider Authorization) object count over
        time.

        Supports filtering by RIR or location (country code) to generate multiple
        named series. If no RIR or location filter is specified, returns total count.

        Args:
          date_end: End of the date range (inclusive).

          date_start: Start of the date range (inclusive).

          format: Format in which results will be returned.

          location: Filters results by location. Specify a comma-separated list of alpha-2 location
              codes.

          name: Array of names used to label the series in the response.

          rir: Filter by Regional Internet Registry (RIR). Multiple RIRs generate multiple
              series.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/bgp/rpki/aspa/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_end": date_end,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                        "rir": rir,
                    },
                    aspa_timeseries_params.ASPATimeseriesParams,
                ),
                post_parser=ResultWrapper[ASPATimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[ASPATimeseriesResponse], ResultWrapper[ASPATimeseriesResponse]),
        )


class ASPAResourceWithRawResponse:
    def __init__(self, aspa: ASPAResource) -> None:
        self._aspa = aspa

        self.changes = to_raw_response_wrapper(
            aspa.changes,
        )
        self.snapshot = to_raw_response_wrapper(
            aspa.snapshot,
        )
        self.timeseries = to_raw_response_wrapper(
            aspa.timeseries,
        )


class AsyncASPAResourceWithRawResponse:
    def __init__(self, aspa: AsyncASPAResource) -> None:
        self._aspa = aspa

        self.changes = async_to_raw_response_wrapper(
            aspa.changes,
        )
        self.snapshot = async_to_raw_response_wrapper(
            aspa.snapshot,
        )
        self.timeseries = async_to_raw_response_wrapper(
            aspa.timeseries,
        )


class ASPAResourceWithStreamingResponse:
    def __init__(self, aspa: ASPAResource) -> None:
        self._aspa = aspa

        self.changes = to_streamed_response_wrapper(
            aspa.changes,
        )
        self.snapshot = to_streamed_response_wrapper(
            aspa.snapshot,
        )
        self.timeseries = to_streamed_response_wrapper(
            aspa.timeseries,
        )


class AsyncASPAResourceWithStreamingResponse:
    def __init__(self, aspa: AsyncASPAResource) -> None:
        self._aspa = aspa

        self.changes = async_to_streamed_response_wrapper(
            aspa.changes,
        )
        self.snapshot = async_to_streamed_response_wrapper(
            aspa.snapshot,
        )
        self.timeseries = async_to_streamed_response_wrapper(
            aspa.timeseries,
        )
