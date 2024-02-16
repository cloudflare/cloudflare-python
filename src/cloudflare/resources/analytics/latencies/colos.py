# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.analytics.latencies import ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse

__all__ = ["Colos", "AsyncColos"]


class Colos(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ColosWithRawResponse:
        return ColosWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ColosWithStreamingResponse:
        return ColosWithStreamingResponse(self)

    def argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse:
        """
        Argo Analytics for a zone at different PoPs

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse,
            self._get(
                f"/zones/{zone_id}/analytics/latency/colos",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncColos(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncColosWithRawResponse:
        return AsyncColosWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncColosWithStreamingResponse:
        return AsyncColosWithStreamingResponse(self)

    async def argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse:
        """
        Argo Analytics for a zone at different PoPs

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse,
            await self._get(
                f"/zones/{zone_id}/analytics/latency/colos",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ColosWithRawResponse:
    def __init__(self, colos: Colos) -> None:
        self._colos = colos

        self.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps = to_raw_response_wrapper(
            colos.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps,
        )


class AsyncColosWithRawResponse:
    def __init__(self, colos: AsyncColos) -> None:
        self._colos = colos

        self.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps = (
            async_to_raw_response_wrapper(
                colos.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps,
            )
        )


class ColosWithStreamingResponse:
    def __init__(self, colos: Colos) -> None:
        self._colos = colos

        self.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps = to_streamed_response_wrapper(
            colos.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps,
        )


class AsyncColosWithStreamingResponse:
    def __init__(self, colos: AsyncColos) -> None:
        self._colos = colos

        self.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps = (
            async_to_streamed_response_wrapper(
                colos.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps,
            )
        )
