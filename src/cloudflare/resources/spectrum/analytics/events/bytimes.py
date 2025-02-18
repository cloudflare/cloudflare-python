# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast
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
from ....._base_client import make_request_options
from .....types.spectrum.analytics.events import bytime_get_params
from .....types.spectrum.analytics.dimension import Dimension
from .....types.spectrum.analytics.events.bytime_get_response import BytimeGetResponse

__all__ = ["BytimesResource", "AsyncBytimesResource"]


class BytimesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BytimesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BytimesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BytimesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BytimesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
        time_delta: Literal["year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"],
        dimensions: List[Dimension] | NotGiven = NOT_GIVEN,
        filters: str | NotGiven = NOT_GIVEN,
        metrics: List[
            Literal[
                "count", "bytesIngress", "bytesEgress", "durationAvg", "durationMedian", "duration90th", "duration99th"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort: List[str] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BytimeGetResponse]:
        """
        Retrieves a list of aggregate metrics grouped by time interval.

        Args:
          zone_id: Identifier

          time_delta: Used to select time series resolution.

          dimensions:
              Can be used to break down the data by given attributes. Options are:

              | Dimension | Name                          | Example                                                    |
              | --------- | ----------------------------- | ---------------------------------------------------------- |
              | event     | Connection Event              | connect, progress, disconnect, originError, clientFiltered |
              | appID     | Application ID                | 40d67c87c6cd4b889a4fd57805225e85                           |
              | coloName  | Colo Name                     | SFO                                                        |
              | ipVersion | IP version used by the client | 4, 6.                                                      |

          filters: Used to filter rows by one or more dimensions. Filters can be combined using OR
              and AND boolean logic. AND takes precedence over OR in all the expressions. The
              OR operator is defined using a comma (,) or OR keyword surrounded by whitespace.
              The AND operator is defined using a semicolon (;) or AND keyword surrounded by
              whitespace. Note that the semicolon is a reserved character in URLs (rfc1738)
              and needs to be percent-encoded as %3B. Comparison options are:

              | Operator | Name                     | URL Encoded |
              | -------- | ------------------------ | ----------- |
              | ==       | Equals                   | %3D%3D      |
              | !=       | Does not equals          | !%3D        |
              | \\>>       | Greater Than             | %3E         |
              | \\<<       | Less Than                | %3C         |
              | \\>>=      | Greater than or equal to | %3E%3D      |
              | \\<<=      | Less than or equal to    | %3C%3D      |

          metrics:
              One or more metrics to compute. Options are:

              | Metric         | Name                                | Example | Unit                  |
              | -------------- | ----------------------------------- | ------- | --------------------- |
              | count          | Count of total events               | 1000    | Count                 |
              | bytesIngress   | Sum of ingress bytes                | 1000    | Sum                   |
              | bytesEgress    | Sum of egress bytes                 | 1000    | Sum                   |
              | durationAvg    | Average connection duration         | 1.0     | Time in milliseconds  |
              | durationMedian | Median connection duration          | 1.0     | Time in milliseconds  |
              | duration90th   | 90th percentile connection duration | 1.0     | Time in milliseconds  |
              | duration99th   | 99th percentile connection duration | 1.0     | Time in milliseconds. |

          since: Start of time interval to query, defaults to `until` - 6 hours. Timestamp must
              be in RFC3339 format and uses UTC unless otherwise specified.

          sort: The sort order for the result set; sort fields must be included in `metrics` or
              `dimensions`.

          until: End of time interval to query, defaults to current time. Timestamp must be in
              RFC3339 format and uses UTC unless otherwise specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/spectrum/analytics/events/bytime",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_delta": time_delta,
                        "dimensions": dimensions,
                        "filters": filters,
                        "metrics": metrics,
                        "since": since,
                        "sort": sort,
                        "until": until,
                    },
                    bytime_get_params.BytimeGetParams,
                ),
                post_parser=ResultWrapper[Optional[BytimeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BytimeGetResponse]], ResultWrapper[BytimeGetResponse]),
        )


class AsyncBytimesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBytimesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBytimesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBytimesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBytimesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
        time_delta: Literal["year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"],
        dimensions: List[Dimension] | NotGiven = NOT_GIVEN,
        filters: str | NotGiven = NOT_GIVEN,
        metrics: List[
            Literal[
                "count", "bytesIngress", "bytesEgress", "durationAvg", "durationMedian", "duration90th", "duration99th"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort: List[str] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BytimeGetResponse]:
        """
        Retrieves a list of aggregate metrics grouped by time interval.

        Args:
          zone_id: Identifier

          time_delta: Used to select time series resolution.

          dimensions:
              Can be used to break down the data by given attributes. Options are:

              | Dimension | Name                          | Example                                                    |
              | --------- | ----------------------------- | ---------------------------------------------------------- |
              | event     | Connection Event              | connect, progress, disconnect, originError, clientFiltered |
              | appID     | Application ID                | 40d67c87c6cd4b889a4fd57805225e85                           |
              | coloName  | Colo Name                     | SFO                                                        |
              | ipVersion | IP version used by the client | 4, 6.                                                      |

          filters: Used to filter rows by one or more dimensions. Filters can be combined using OR
              and AND boolean logic. AND takes precedence over OR in all the expressions. The
              OR operator is defined using a comma (,) or OR keyword surrounded by whitespace.
              The AND operator is defined using a semicolon (;) or AND keyword surrounded by
              whitespace. Note that the semicolon is a reserved character in URLs (rfc1738)
              and needs to be percent-encoded as %3B. Comparison options are:

              | Operator | Name                     | URL Encoded |
              | -------- | ------------------------ | ----------- |
              | ==       | Equals                   | %3D%3D      |
              | !=       | Does not equals          | !%3D        |
              | \\>>       | Greater Than             | %3E         |
              | \\<<       | Less Than                | %3C         |
              | \\>>=      | Greater than or equal to | %3E%3D      |
              | \\<<=      | Less than or equal to    | %3C%3D      |

          metrics:
              One or more metrics to compute. Options are:

              | Metric         | Name                                | Example | Unit                  |
              | -------------- | ----------------------------------- | ------- | --------------------- |
              | count          | Count of total events               | 1000    | Count                 |
              | bytesIngress   | Sum of ingress bytes                | 1000    | Sum                   |
              | bytesEgress    | Sum of egress bytes                 | 1000    | Sum                   |
              | durationAvg    | Average connection duration         | 1.0     | Time in milliseconds  |
              | durationMedian | Median connection duration          | 1.0     | Time in milliseconds  |
              | duration90th   | 90th percentile connection duration | 1.0     | Time in milliseconds  |
              | duration99th   | 99th percentile connection duration | 1.0     | Time in milliseconds. |

          since: Start of time interval to query, defaults to `until` - 6 hours. Timestamp must
              be in RFC3339 format and uses UTC unless otherwise specified.

          sort: The sort order for the result set; sort fields must be included in `metrics` or
              `dimensions`.

          until: End of time interval to query, defaults to current time. Timestamp must be in
              RFC3339 format and uses UTC unless otherwise specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/spectrum/analytics/events/bytime",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_delta": time_delta,
                        "dimensions": dimensions,
                        "filters": filters,
                        "metrics": metrics,
                        "since": since,
                        "sort": sort,
                        "until": until,
                    },
                    bytime_get_params.BytimeGetParams,
                ),
                post_parser=ResultWrapper[Optional[BytimeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BytimeGetResponse]], ResultWrapper[BytimeGetResponse]),
        )


class BytimesResourceWithRawResponse:
    def __init__(self, bytimes: BytimesResource) -> None:
        self._bytimes = bytimes

        self.get = to_raw_response_wrapper(
            bytimes.get,
        )


class AsyncBytimesResourceWithRawResponse:
    def __init__(self, bytimes: AsyncBytimesResource) -> None:
        self._bytimes = bytimes

        self.get = async_to_raw_response_wrapper(
            bytimes.get,
        )


class BytimesResourceWithStreamingResponse:
    def __init__(self, bytimes: BytimesResource) -> None:
        self._bytimes = bytimes

        self.get = to_streamed_response_wrapper(
            bytimes.get,
        )


class AsyncBytimesResourceWithStreamingResponse:
    def __init__(self, bytimes: AsyncBytimesResource) -> None:
        self._bytimes = bytimes

        self.get = async_to_streamed_response_wrapper(
            bytimes.get,
        )
