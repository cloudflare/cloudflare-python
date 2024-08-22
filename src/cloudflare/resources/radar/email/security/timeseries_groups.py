# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
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
from .....types.radar.email.security import (
    timeseries_group_arc_params,
    timeseries_group_spf_params,
    timeseries_group_dkim_params,
    timeseries_group_spam_params,
    timeseries_group_dmarc_params,
    timeseries_group_spoof_params,
    timeseries_group_malicious_params,
    timeseries_group_tls_version_params,
    timeseries_group_threat_category_params,
)
from .....types.radar.email.security.timeseries_group_arc_response import TimeseriesGroupARCResponse
from .....types.radar.email.security.timeseries_group_spf_response import TimeseriesGroupSPFResponse
from .....types.radar.email.security.timeseries_group_dkim_response import TimeseriesGroupDKIMResponse
from .....types.radar.email.security.timeseries_group_spam_response import TimeseriesGroupSpamResponse
from .....types.radar.email.security.timeseries_group_dmarc_response import TimeseriesGroupDMARCResponse
from .....types.radar.email.security.timeseries_group_spoof_response import TimeseriesGroupSpoofResponse
from .....types.radar.email.security.timeseries_group_malicious_response import TimeseriesGroupMaliciousResponse
from .....types.radar.email.security.timeseries_group_tls_version_response import TimeseriesGroupTLSVersionResponse
from .....types.radar.email.security.timeseries_group_threat_category_response import (
    TimeseriesGroupThreatCategoryResponse,
)

__all__ = ["TimeseriesGroupsResource", "AsyncTimeseriesGroupsResource"]


class TimeseriesGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self)

    def arc(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupARCResponse:
        """
        Percentage distribution of emails classified per Arc validation over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/timeseries_groups/arc",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_arc_params.TimeseriesGroupARCParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupARCResponse], ResultWrapper[TimeseriesGroupARCResponse]),
        )

    def dkim(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupDKIMResponse:
        """
        Percentage distribution of emails classified per DKIM validation over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/timeseries_groups/dkim",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_dkim_params.TimeseriesGroupDKIMParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDKIMResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDKIMResponse], ResultWrapper[TimeseriesGroupDKIMResponse]),
        )

    def dmarc(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupDMARCResponse:
        """
        Percentage distribution of emails classified per DMARC validation over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/timeseries_groups/dmarc",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_dmarc_params.TimeseriesGroupDMARCParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDMARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDMARCResponse], ResultWrapper[TimeseriesGroupDMARCResponse]),
        )

    def malicious(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupMaliciousResponse:
        """
        Percentage distribution of emails classified as MALICIOUS over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/timeseries_groups/malicious",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_malicious_params.TimeseriesGroupMaliciousParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupMaliciousResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupMaliciousResponse], ResultWrapper[TimeseriesGroupMaliciousResponse]),
        )

    def spam(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupSpamResponse:
        """
        Percentage distribution of emails classified as SPAM over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/timeseries_groups/spam",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_spam_params.TimeseriesGroupSpamParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupSpamResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupSpamResponse], ResultWrapper[TimeseriesGroupSpamResponse]),
        )

    def spf(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupSPFResponse:
        """
        Percentage distribution of emails classified per SPF validation over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/timeseries_groups/spf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "tls_version": tls_version,
                    },
                    timeseries_group_spf_params.TimeseriesGroupSPFParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupSPFResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupSPFResponse], ResultWrapper[TimeseriesGroupSPFResponse]),
        )

    def spoof(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupSpoofResponse:
        """
        Percentage distribution of emails classified as SPOOF over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/timeseries_groups/spoof",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_spoof_params.TimeseriesGroupSpoofParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupSpoofResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupSpoofResponse], ResultWrapper[TimeseriesGroupSpoofResponse]),
        )

    def threat_category(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupThreatCategoryResponse:
        """
        Percentage distribution of emails classified in Threat Categories over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/timeseries_groups/threat_category",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_threat_category_params.TimeseriesGroupThreatCategoryParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupThreatCategoryResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[TimeseriesGroupThreatCategoryResponse], ResultWrapper[TimeseriesGroupThreatCategoryResponse]
            ),
        )

    def tls_version(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupTLSVersionResponse:
        """
        Percentage distribution of emails classified per TLS Version over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/security/timeseries_groups/tls_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_tls_version_params.TimeseriesGroupTLSVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupTLSVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupTLSVersionResponse], ResultWrapper[TimeseriesGroupTLSVersionResponse]),
        )


class AsyncTimeseriesGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self)

    async def arc(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupARCResponse:
        """
        Percentage distribution of emails classified per Arc validation over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/timeseries_groups/arc",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_arc_params.TimeseriesGroupARCParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupARCResponse], ResultWrapper[TimeseriesGroupARCResponse]),
        )

    async def dkim(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupDKIMResponse:
        """
        Percentage distribution of emails classified per DKIM validation over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/timeseries_groups/dkim",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_dkim_params.TimeseriesGroupDKIMParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDKIMResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDKIMResponse], ResultWrapper[TimeseriesGroupDKIMResponse]),
        )

    async def dmarc(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupDMARCResponse:
        """
        Percentage distribution of emails classified per DMARC validation over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/timeseries_groups/dmarc",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_dmarc_params.TimeseriesGroupDMARCParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDMARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDMARCResponse], ResultWrapper[TimeseriesGroupDMARCResponse]),
        )

    async def malicious(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupMaliciousResponse:
        """
        Percentage distribution of emails classified as MALICIOUS over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/timeseries_groups/malicious",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_malicious_params.TimeseriesGroupMaliciousParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupMaliciousResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupMaliciousResponse], ResultWrapper[TimeseriesGroupMaliciousResponse]),
        )

    async def spam(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupSpamResponse:
        """
        Percentage distribution of emails classified as SPAM over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/timeseries_groups/spam",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_spam_params.TimeseriesGroupSpamParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupSpamResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupSpamResponse], ResultWrapper[TimeseriesGroupSpamResponse]),
        )

    async def spf(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupSPFResponse:
        """
        Percentage distribution of emails classified per SPF validation over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/timeseries_groups/spf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "tls_version": tls_version,
                    },
                    timeseries_group_spf_params.TimeseriesGroupSPFParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupSPFResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupSPFResponse], ResultWrapper[TimeseriesGroupSPFResponse]),
        )

    async def spoof(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupSpoofResponse:
        """
        Percentage distribution of emails classified as SPOOF over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/timeseries_groups/spoof",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_spoof_params.TimeseriesGroupSpoofParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupSpoofResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupSpoofResponse], ResultWrapper[TimeseriesGroupSpoofResponse]),
        )

    async def threat_category(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        tls_version: List[Literal["TLSv1_0", "TLSv1_1", "TLSv1_2", "TLSv1_3"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupThreatCategoryResponse:
        """
        Percentage distribution of emails classified in Threat Categories over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          tls_version: Filter for tls version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/timeseries_groups/threat_category",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                        "tls_version": tls_version,
                    },
                    timeseries_group_threat_category_params.TimeseriesGroupThreatCategoryParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupThreatCategoryResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[TimeseriesGroupThreatCategoryResponse], ResultWrapper[TimeseriesGroupThreatCategoryResponse]
            ),
        )

    async def tls_version(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupTLSVersionResponse:
        """
        Percentage distribution of emails classified per TLS Version over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filter for arc (Authenticated Received Chain).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          dkim: Filter for dkim.

          dmarc: Filter for dmarc.

          format: Format results are returned in.

          name: Array of names that will be used to name the series in responses.

          spf: Filter for spf.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/security/timeseries_groups/tls_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "arc": arc,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dkim": dkim,
                        "dmarc": dmarc,
                        "format": format,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_tls_version_params.TimeseriesGroupTLSVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupTLSVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupTLSVersionResponse], ResultWrapper[TimeseriesGroupTLSVersionResponse]),
        )


class TimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.arc = to_raw_response_wrapper(
            timeseries_groups.arc,
        )
        self.dkim = to_raw_response_wrapper(
            timeseries_groups.dkim,
        )
        self.dmarc = to_raw_response_wrapper(
            timeseries_groups.dmarc,
        )
        self.malicious = to_raw_response_wrapper(
            timeseries_groups.malicious,
        )
        self.spam = to_raw_response_wrapper(
            timeseries_groups.spam,
        )
        self.spf = to_raw_response_wrapper(
            timeseries_groups.spf,
        )
        self.spoof = to_raw_response_wrapper(
            timeseries_groups.spoof,
        )
        self.threat_category = to_raw_response_wrapper(
            timeseries_groups.threat_category,
        )
        self.tls_version = to_raw_response_wrapper(
            timeseries_groups.tls_version,
        )


class AsyncTimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.arc = async_to_raw_response_wrapper(
            timeseries_groups.arc,
        )
        self.dkim = async_to_raw_response_wrapper(
            timeseries_groups.dkim,
        )
        self.dmarc = async_to_raw_response_wrapper(
            timeseries_groups.dmarc,
        )
        self.malicious = async_to_raw_response_wrapper(
            timeseries_groups.malicious,
        )
        self.spam = async_to_raw_response_wrapper(
            timeseries_groups.spam,
        )
        self.spf = async_to_raw_response_wrapper(
            timeseries_groups.spf,
        )
        self.spoof = async_to_raw_response_wrapper(
            timeseries_groups.spoof,
        )
        self.threat_category = async_to_raw_response_wrapper(
            timeseries_groups.threat_category,
        )
        self.tls_version = async_to_raw_response_wrapper(
            timeseries_groups.tls_version,
        )


class TimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.arc = to_streamed_response_wrapper(
            timeseries_groups.arc,
        )
        self.dkim = to_streamed_response_wrapper(
            timeseries_groups.dkim,
        )
        self.dmarc = to_streamed_response_wrapper(
            timeseries_groups.dmarc,
        )
        self.malicious = to_streamed_response_wrapper(
            timeseries_groups.malicious,
        )
        self.spam = to_streamed_response_wrapper(
            timeseries_groups.spam,
        )
        self.spf = to_streamed_response_wrapper(
            timeseries_groups.spf,
        )
        self.spoof = to_streamed_response_wrapper(
            timeseries_groups.spoof,
        )
        self.threat_category = to_streamed_response_wrapper(
            timeseries_groups.threat_category,
        )
        self.tls_version = to_streamed_response_wrapper(
            timeseries_groups.tls_version,
        )


class AsyncTimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.arc = async_to_streamed_response_wrapper(
            timeseries_groups.arc,
        )
        self.dkim = async_to_streamed_response_wrapper(
            timeseries_groups.dkim,
        )
        self.dmarc = async_to_streamed_response_wrapper(
            timeseries_groups.dmarc,
        )
        self.malicious = async_to_streamed_response_wrapper(
            timeseries_groups.malicious,
        )
        self.spam = async_to_streamed_response_wrapper(
            timeseries_groups.spam,
        )
        self.spf = async_to_streamed_response_wrapper(
            timeseries_groups.spf,
        )
        self.spoof = async_to_streamed_response_wrapper(
            timeseries_groups.spoof,
        )
        self.threat_category = async_to_streamed_response_wrapper(
            timeseries_groups.threat_category,
        )
        self.tls_version = async_to_streamed_response_wrapper(
            timeseries_groups.tls_version,
        )
