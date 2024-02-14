# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
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
from .....types.spectrums.analytics.aggregates import (
    CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse,
    current_spectrum_aggregate_analytics_get_current_aggregated_analytics_params,
)

__all__ = ["Currents", "AsyncCurrents"]


class Currents(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CurrentsWithRawResponse:
        return CurrentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrentsWithStreamingResponse:
        return CurrentsWithStreamingResponse(self)

    def spectrum_aggregate_analytics_get_current_aggregated_analytics(
        self,
        zone: str,
        *,
        app_id_param: str | NotGiven = NOT_GIVEN,
        app_id: str | NotGiven = NOT_GIVEN,
        colo_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse:
        """
        Retrieves analytics aggregated from the last minute of usage on Spectrum
        applications underneath a given zone.

        Args:
          zone: Identifier

          app_id_param: Comma-delimited list of Spectrum Application Id(s). If provided, the response
              will be limited to Spectrum Application Id(s) that match.

          app_id: Comma-delimited list of Spectrum Application Id(s). If provided, the response
              will be limited to Spectrum Application Id(s) that match.

          colo_name: Co-location identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        return self._get(
            f"/zones/{zone}/spectrum/analytics/aggregate/current",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id_param": app_id_param,
                        "app_id": app_id,
                        "colo_name": colo_name,
                    },
                    current_spectrum_aggregate_analytics_get_current_aggregated_analytics_params.CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse],
                ResultWrapper[CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse],
            ),
        )


class AsyncCurrents(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCurrentsWithRawResponse:
        return AsyncCurrentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrentsWithStreamingResponse:
        return AsyncCurrentsWithStreamingResponse(self)

    async def spectrum_aggregate_analytics_get_current_aggregated_analytics(
        self,
        zone: str,
        *,
        app_id_param: str | NotGiven = NOT_GIVEN,
        app_id: str | NotGiven = NOT_GIVEN,
        colo_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse:
        """
        Retrieves analytics aggregated from the last minute of usage on Spectrum
        applications underneath a given zone.

        Args:
          zone: Identifier

          app_id_param: Comma-delimited list of Spectrum Application Id(s). If provided, the response
              will be limited to Spectrum Application Id(s) that match.

          app_id: Comma-delimited list of Spectrum Application Id(s). If provided, the response
              will be limited to Spectrum Application Id(s) that match.

          colo_name: Co-location identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        return await self._get(
            f"/zones/{zone}/spectrum/analytics/aggregate/current",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id_param": app_id_param,
                        "app_id": app_id,
                        "colo_name": colo_name,
                    },
                    current_spectrum_aggregate_analytics_get_current_aggregated_analytics_params.CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse],
                ResultWrapper[CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse],
            ),
        )


class CurrentsWithRawResponse:
    def __init__(self, currents: Currents) -> None:
        self._currents = currents

        self.spectrum_aggregate_analytics_get_current_aggregated_analytics = to_raw_response_wrapper(
            currents.spectrum_aggregate_analytics_get_current_aggregated_analytics,
        )


class AsyncCurrentsWithRawResponse:
    def __init__(self, currents: AsyncCurrents) -> None:
        self._currents = currents

        self.spectrum_aggregate_analytics_get_current_aggregated_analytics = async_to_raw_response_wrapper(
            currents.spectrum_aggregate_analytics_get_current_aggregated_analytics,
        )


class CurrentsWithStreamingResponse:
    def __init__(self, currents: Currents) -> None:
        self._currents = currents

        self.spectrum_aggregate_analytics_get_current_aggregated_analytics = to_streamed_response_wrapper(
            currents.spectrum_aggregate_analytics_get_current_aggregated_analytics,
        )


class AsyncCurrentsWithStreamingResponse:
    def __init__(self, currents: AsyncCurrents) -> None:
        self._currents = currents

        self.spectrum_aggregate_analytics_get_current_aggregated_analytics = async_to_streamed_response_wrapper(
            currents.spectrum_aggregate_analytics_get_current_aggregated_analytics,
        )
