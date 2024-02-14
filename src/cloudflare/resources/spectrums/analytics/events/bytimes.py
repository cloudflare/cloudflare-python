# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.spectrums.analytics.events import BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse

from typing import Optional, List, Union, Iterable

from typing_extensions import Literal

from datetime import datetime

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
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .....types.spectrums.analytics.events import bytime_spectrum_analytics_by_time_get_analytics_by_time_params
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Bytimes", "AsyncBytimes"]


class Bytimes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BytimesWithRawResponse:
        return BytimesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BytimesWithStreamingResponse:
        return BytimesWithStreamingResponse(self)

    def spectrum_analytics_by_time_get_analytics_by_time(
        self,
        zone: str,
        *,
        dimensions: List[Literal["event", "appID", "coloName", "ipVersion"]] | NotGiven = NOT_GIVEN,
        filters: str | NotGiven = NOT_GIVEN,
        metrics: List[
            Literal[
                "count", "bytesIngress", "bytesEgress", "durationAvg", "durationMedian", "duration90th", "duration99th"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort: Iterable[object] | NotGiven = NOT_GIVEN,
        time_delta: Literal["year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"]
        | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse]:
        """
        Retrieves a list of aggregate metrics grouped by time interval.

        Args:
          zone: Identifier

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
              | >        | Greater Than             | %3E         |
              | <        | Less Than                | %3C         |
              | >=       | Greater than or equal to | %3E%3D      |
              | <=       | Less than or equal to    | %3C%3D .    |

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

          time_delta: Used to select time series resolution.

          until: End of time interval to query, defaults to current time. Timestamp must be in
              RFC3339 format and uses UTC unless otherwise specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        return cast(
            Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse],
            self._get(
                f"/zones/{zone}/spectrum/analytics/events/bytime",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "dimensions": dimensions,
                            "filters": filters,
                            "metrics": metrics,
                            "since": since,
                            "sort": sort,
                            "time_delta": time_delta,
                            "until": until,
                        },
                        bytime_spectrum_analytics_by_time_get_analytics_by_time_params.BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeParams,
                    ),
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncBytimes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBytimesWithRawResponse:
        return AsyncBytimesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBytimesWithStreamingResponse:
        return AsyncBytimesWithStreamingResponse(self)

    async def spectrum_analytics_by_time_get_analytics_by_time(
        self,
        zone: str,
        *,
        dimensions: List[Literal["event", "appID", "coloName", "ipVersion"]] | NotGiven = NOT_GIVEN,
        filters: str | NotGiven = NOT_GIVEN,
        metrics: List[
            Literal[
                "count", "bytesIngress", "bytesEgress", "durationAvg", "durationMedian", "duration90th", "duration99th"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort: Iterable[object] | NotGiven = NOT_GIVEN,
        time_delta: Literal["year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"]
        | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse]:
        """
        Retrieves a list of aggregate metrics grouped by time interval.

        Args:
          zone: Identifier

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
              | >        | Greater Than             | %3E         |
              | <        | Less Than                | %3C         |
              | >=       | Greater than or equal to | %3E%3D      |
              | <=       | Less than or equal to    | %3C%3D .    |

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

          time_delta: Used to select time series resolution.

          until: End of time interval to query, defaults to current time. Timestamp must be in
              RFC3339 format and uses UTC unless otherwise specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone:
            raise ValueError(f"Expected a non-empty value for `zone` but received {zone!r}")
        return cast(
            Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse],
            await self._get(
                f"/zones/{zone}/spectrum/analytics/events/bytime",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "dimensions": dimensions,
                            "filters": filters,
                            "metrics": metrics,
                            "since": since,
                            "sort": sort,
                            "time_delta": time_delta,
                            "until": until,
                        },
                        bytime_spectrum_analytics_by_time_get_analytics_by_time_params.BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeParams,
                    ),
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class BytimesWithRawResponse:
    def __init__(self, bytimes: Bytimes) -> None:
        self._bytimes = bytimes

        self.spectrum_analytics_by_time_get_analytics_by_time = to_raw_response_wrapper(
            bytimes.spectrum_analytics_by_time_get_analytics_by_time,
        )


class AsyncBytimesWithRawResponse:
    def __init__(self, bytimes: AsyncBytimes) -> None:
        self._bytimes = bytimes

        self.spectrum_analytics_by_time_get_analytics_by_time = async_to_raw_response_wrapper(
            bytimes.spectrum_analytics_by_time_get_analytics_by_time,
        )


class BytimesWithStreamingResponse:
    def __init__(self, bytimes: Bytimes) -> None:
        self._bytimes = bytimes

        self.spectrum_analytics_by_time_get_analytics_by_time = to_streamed_response_wrapper(
            bytimes.spectrum_analytics_by_time_get_analytics_by_time,
        )


class AsyncBytimesWithStreamingResponse:
    def __init__(self, bytimes: AsyncBytimes) -> None:
        self._bytimes = bytimes

        self.spectrum_analytics_by_time_get_analytics_by_time = async_to_streamed_response_wrapper(
            bytimes.spectrum_analytics_by_time_get_analytics_by_time,
        )
