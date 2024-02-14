# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Union, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.analytics import (
    DashboardZoneAnalyticsDeprecatedGetDashboardResponse,
    dashboard_zone_analytics_deprecated_get_dashboard_params,
)

__all__ = ["Dashboards", "AsyncDashboards"]


class Dashboards(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DashboardsWithRawResponse:
        return DashboardsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DashboardsWithStreamingResponse:
        return DashboardsWithStreamingResponse(self)

    def zone_analytics_deprecated_get_dashboard(
        self,
        zone_identifier: str,
        *,
        continuous: bool | NotGiven = NOT_GIVEN,
        since: Union[str, int] | NotGiven = NOT_GIVEN,
        until: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DashboardZoneAnalyticsDeprecatedGetDashboardResponse:
        """
        The dashboard view provides both totals and timeseries data for the given zone
        and time period across the entire Cloudflare network.

        Args:
          zone_identifier: Identifier

          continuous: When set to true, the API will move the requested time window backward, until it
              finds a region with completely aggregated data.

              The API response _may not represent the requested time window_.

          since: The (inclusive) beginning of the requested time frame. This value can be a
              negative integer representing the number of minutes in the past relative to time
              the request is made, or can be an absolute timestamp that conforms to RFC 3339.
              At this point in time, it cannot exceed a time in the past greater than one
              year.

              Ranges that the Cloudflare web application provides will provide the following
              period length for each point:

              - Last 60 minutes (from -59 to -1): 1 minute resolution
              - Last 7 hours (from -419 to -60): 15 minutes resolution
              - Last 15 hours (from -899 to -420): 30 minutes resolution
              - Last 72 hours (from -4320 to -900): 1 hour resolution
              - Older than 3 days (-525600 to -4320): 1 day resolution.

          until: The (exclusive) end of the requested time frame. This value can be a negative
              integer representing the number of minutes in the past relative to time the
              request is made, or can be an absolute timestamp that conforms to RFC 3339. If
              omitted, the time of the request is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/analytics/dashboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continuous": continuous,
                        "since": since,
                        "until": until,
                    },
                    dashboard_zone_analytics_deprecated_get_dashboard_params.DashboardZoneAnalyticsDeprecatedGetDashboardParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DashboardZoneAnalyticsDeprecatedGetDashboardResponse],
                ResultWrapper[DashboardZoneAnalyticsDeprecatedGetDashboardResponse],
            ),
        )


class AsyncDashboards(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDashboardsWithRawResponse:
        return AsyncDashboardsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDashboardsWithStreamingResponse:
        return AsyncDashboardsWithStreamingResponse(self)

    async def zone_analytics_deprecated_get_dashboard(
        self,
        zone_identifier: str,
        *,
        continuous: bool | NotGiven = NOT_GIVEN,
        since: Union[str, int] | NotGiven = NOT_GIVEN,
        until: Union[str, int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DashboardZoneAnalyticsDeprecatedGetDashboardResponse:
        """
        The dashboard view provides both totals and timeseries data for the given zone
        and time period across the entire Cloudflare network.

        Args:
          zone_identifier: Identifier

          continuous: When set to true, the API will move the requested time window backward, until it
              finds a region with completely aggregated data.

              The API response _may not represent the requested time window_.

          since: The (inclusive) beginning of the requested time frame. This value can be a
              negative integer representing the number of minutes in the past relative to time
              the request is made, or can be an absolute timestamp that conforms to RFC 3339.
              At this point in time, it cannot exceed a time in the past greater than one
              year.

              Ranges that the Cloudflare web application provides will provide the following
              period length for each point:

              - Last 60 minutes (from -59 to -1): 1 minute resolution
              - Last 7 hours (from -419 to -60): 15 minutes resolution
              - Last 15 hours (from -899 to -420): 30 minutes resolution
              - Last 72 hours (from -4320 to -900): 1 hour resolution
              - Older than 3 days (-525600 to -4320): 1 day resolution.

          until: The (exclusive) end of the requested time frame. This value can be a negative
              integer representing the number of minutes in the past relative to time the
              request is made, or can be an absolute timestamp that conforms to RFC 3339. If
              omitted, the time of the request is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/analytics/dashboard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continuous": continuous,
                        "since": since,
                        "until": until,
                    },
                    dashboard_zone_analytics_deprecated_get_dashboard_params.DashboardZoneAnalyticsDeprecatedGetDashboardParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DashboardZoneAnalyticsDeprecatedGetDashboardResponse],
                ResultWrapper[DashboardZoneAnalyticsDeprecatedGetDashboardResponse],
            ),
        )


class DashboardsWithRawResponse:
    def __init__(self, dashboards: Dashboards) -> None:
        self._dashboards = dashboards

        self.zone_analytics_deprecated_get_dashboard = to_raw_response_wrapper(
            dashboards.zone_analytics_deprecated_get_dashboard,
        )


class AsyncDashboardsWithRawResponse:
    def __init__(self, dashboards: AsyncDashboards) -> None:
        self._dashboards = dashboards

        self.zone_analytics_deprecated_get_dashboard = async_to_raw_response_wrapper(
            dashboards.zone_analytics_deprecated_get_dashboard,
        )


class DashboardsWithStreamingResponse:
    def __init__(self, dashboards: Dashboards) -> None:
        self._dashboards = dashboards

        self.zone_analytics_deprecated_get_dashboard = to_streamed_response_wrapper(
            dashboards.zone_analytics_deprecated_get_dashboard,
        )


class AsyncDashboardsWithStreamingResponse:
    def __init__(self, dashboards: AsyncDashboards) -> None:
        self._dashboards = dashboards

        self.zone_analytics_deprecated_get_dashboard = async_to_streamed_response_wrapper(
            dashboards.zone_analytics_deprecated_get_dashboard,
        )
