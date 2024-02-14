# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.analytics import ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse

from typing import Type, Union

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.analytics import colo_zone_analytics_deprecated_get_analytics_by_co_locations_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Colo", "AsyncColo"]


class Colo(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ColoWithRawResponse:
        return ColoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ColoWithStreamingResponse:
        return ColoWithStreamingResponse(self)

    def zone_analytics_deprecated_get_analytics_by_co_locations(
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
    ) -> ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse:
        """This view provides a breakdown of analytics data by datacenter.

        Note: This is
        available to Enterprise customers only.

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
            f"/zones/{zone_identifier}/analytics/colos",
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
                    colo_zone_analytics_deprecated_get_analytics_by_co_locations_params.ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse],
                ResultWrapper[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse],
            ),
        )


class AsyncColo(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncColoWithRawResponse:
        return AsyncColoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncColoWithStreamingResponse:
        return AsyncColoWithStreamingResponse(self)

    async def zone_analytics_deprecated_get_analytics_by_co_locations(
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
    ) -> ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse:
        """This view provides a breakdown of analytics data by datacenter.

        Note: This is
        available to Enterprise customers only.

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
            f"/zones/{zone_identifier}/analytics/colos",
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
                    colo_zone_analytics_deprecated_get_analytics_by_co_locations_params.ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse],
                ResultWrapper[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse],
            ),
        )


class ColoWithRawResponse:
    def __init__(self, colo: Colo) -> None:
        self._colo = colo

        self.zone_analytics_deprecated_get_analytics_by_co_locations = to_raw_response_wrapper(
            colo.zone_analytics_deprecated_get_analytics_by_co_locations,
        )


class AsyncColoWithRawResponse:
    def __init__(self, colo: AsyncColo) -> None:
        self._colo = colo

        self.zone_analytics_deprecated_get_analytics_by_co_locations = async_to_raw_response_wrapper(
            colo.zone_analytics_deprecated_get_analytics_by_co_locations,
        )


class ColoWithStreamingResponse:
    def __init__(self, colo: Colo) -> None:
        self._colo = colo

        self.zone_analytics_deprecated_get_analytics_by_co_locations = to_streamed_response_wrapper(
            colo.zone_analytics_deprecated_get_analytics_by_co_locations,
        )


class AsyncColoWithStreamingResponse:
    def __init__(self, colo: AsyncColo) -> None:
        self._colo = colo

        self.zone_analytics_deprecated_get_analytics_by_co_locations = async_to_streamed_response_wrapper(
            colo.zone_analytics_deprecated_get_analytics_by_co_locations,
        )
