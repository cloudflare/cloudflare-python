# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
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
from .....types.radar.email.routing import (
    timeseries_group_arc_params,
    timeseries_group_spf_params,
    timeseries_group_dkim_params,
    timeseries_group_dmarc_params,
    timeseries_group_encrypted_params,
    timeseries_group_ip_version_params,
)
from .....types.radar.email.routing.timeseries_group_arc_response import TimeseriesGroupARCResponse
from .....types.radar.email.routing.timeseries_group_spf_response import TimeseriesGroupSPFResponse
from .....types.radar.email.routing.timeseries_group_dkim_response import TimeseriesGroupDKIMResponse
from .....types.radar.email.routing.timeseries_group_dmarc_response import TimeseriesGroupDMARCResponse
from .....types.radar.email.routing.timeseries_group_encrypted_response import TimeseriesGroupEncryptedResponse
from .....types.radar.email.routing.timeseries_group_ip_version_response import TimeseriesGroupIPVersionResponse

__all__ = ["TimeseriesGroupsResource", "AsyncTimeseriesGroupsResource"]


class TimeseriesGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimeseriesGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TimeseriesGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TimeseriesGroupsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def arc(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupARCResponse:
        """
        Retrieves the distribution of emails by ARC (Authenticated Received Chain)
        validation over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/routing/timeseries_groups/arc",
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
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_arc_params.TimeseriesGroupARCParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupARCResponse], ResultWrapper[TimeseriesGroupARCResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def dkim(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupDKIMResponse:
        """
        Retrieves the distribution of emails by DKIM (DomainKeys Identified Mail)
        validation over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/routing/timeseries_groups/dkim",
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
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_dkim_params.TimeseriesGroupDKIMParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDKIMResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDKIMResponse], ResultWrapper[TimeseriesGroupDKIMResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def dmarc(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupDMARCResponse:
        """
        Retrieves the distribution of emails by DMARC (Domain-based Message
        Authentication, Reporting and Conformance) validation over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/routing/timeseries_groups/dmarc",
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
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_dmarc_params.TimeseriesGroupDMARCParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDMARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDMARCResponse], ResultWrapper[TimeseriesGroupDMARCResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def encrypted(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupEncryptedResponse:
        """
        Retrieves the distribution of emails by encryption status (encrypted vs.
        not-encrypted) over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/routing/timeseries_groups/encrypted",
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
                        "ip_version": ip_version,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_encrypted_params.TimeseriesGroupEncryptedParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupEncryptedResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupEncryptedResponse], ResultWrapper[TimeseriesGroupEncryptedResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def ip_version(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupIPVersionResponse:
        """
        Retrieves the distribution of emails by IP version over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/routing/timeseries_groups/ip_version",
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
                        "encrypted": encrypted,
                        "format": format,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_ip_version_params.TimeseriesGroupIPVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupIPVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupIPVersionResponse], ResultWrapper[TimeseriesGroupIPVersionResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    def spf(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupSPFResponse:
        """
        Retrieves the distribution of emails by SPF (Sender Policy Framework) validation
        over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/email/routing/timeseries_groups/spf",
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
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "name": name,
                    },
                    timeseries_group_spf_params.TimeseriesGroupSPFParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupSPFResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupSPFResponse], ResultWrapper[TimeseriesGroupSPFResponse]),
        )


class AsyncTimeseriesGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimeseriesGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def arc(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupARCResponse:
        """
        Retrieves the distribution of emails by ARC (Authenticated Received Chain)
        validation over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/routing/timeseries_groups/arc",
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
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_arc_params.TimeseriesGroupARCParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupARCResponse], ResultWrapper[TimeseriesGroupARCResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def dkim(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupDKIMResponse:
        """
        Retrieves the distribution of emails by DKIM (DomainKeys Identified Mail)
        validation over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/routing/timeseries_groups/dkim",
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
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_dkim_params.TimeseriesGroupDKIMParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDKIMResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDKIMResponse], ResultWrapper[TimeseriesGroupDKIMResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def dmarc(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupDMARCResponse:
        """
        Retrieves the distribution of emails by DMARC (Domain-based Message
        Authentication, Reporting and Conformance) validation over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/routing/timeseries_groups/dmarc",
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
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_dmarc_params.TimeseriesGroupDMARCParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDMARCResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDMARCResponse], ResultWrapper[TimeseriesGroupDMARCResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def encrypted(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupEncryptedResponse:
        """
        Retrieves the distribution of emails by encryption status (encrypted vs.
        not-encrypted) over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/routing/timeseries_groups/encrypted",
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
                        "ip_version": ip_version,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_encrypted_params.TimeseriesGroupEncryptedParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupEncryptedResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupEncryptedResponse], ResultWrapper[TimeseriesGroupEncryptedResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def ip_version(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        spf: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupIPVersionResponse:
        """
        Retrieves the distribution of emails by IP version over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          name: Array of names used to label the series in the response.

          spf: Filters results by SPF (Sender Policy Framework) validation status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/routing/timeseries_groups/ip_version",
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
                        "encrypted": encrypted,
                        "format": format,
                        "name": name,
                        "spf": spf,
                    },
                    timeseries_group_ip_version_params.TimeseriesGroupIPVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupIPVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupIPVersionResponse], ResultWrapper[TimeseriesGroupIPVersionResponse]),
        )

    @typing_extensions.deprecated("deprecated")
    async def spf(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        arc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dkim: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        dmarc: List[Literal["PASS", "NONE", "FAIL"]] | Omit = omit,
        encrypted: List[Literal["ENCRYPTED", "NOT_ENCRYPTED"]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TimeseriesGroupSPFResponse:
        """
        Retrieves the distribution of emails by SPF (Sender Policy Framework) validation
        over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          arc: Filters results by ARC (Authenticated Received Chain) validation.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dkim: Filters results by DKIM (DomainKeys Identified Mail) validation status.

          dmarc: Filters results by DMARC (Domain-based Message Authentication, Reporting and
              Conformance) validation status.

          encrypted: Filters results by encryption status (encrypted vs. not-encrypted).

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          name: Array of names used to label the series in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/email/routing/timeseries_groups/spf",
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
                        "encrypted": encrypted,
                        "format": format,
                        "ip_version": ip_version,
                        "name": name,
                    },
                    timeseries_group_spf_params.TimeseriesGroupSPFParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupSPFResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupSPFResponse], ResultWrapper[TimeseriesGroupSPFResponse]),
        )


class TimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.arc = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.arc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dkim = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.dkim,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dmarc = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.dmarc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.encrypted = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.encrypted,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spf = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                timeseries_groups.spf,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncTimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.arc = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.arc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dkim = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.dkim,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dmarc = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.dmarc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.encrypted = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.encrypted,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spf = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                timeseries_groups.spf,  # pyright: ignore[reportDeprecated],
            )
        )


class TimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.arc = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.arc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dkim = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.dkim,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dmarc = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.dmarc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.encrypted = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.encrypted,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spf = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                timeseries_groups.spf,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncTimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.arc = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.arc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dkim = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.dkim,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dmarc = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.dmarc,  # pyright: ignore[reportDeprecated],
            )
        )
        self.encrypted = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.encrypted,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.spf = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                timeseries_groups.spf,  # pyright: ignore[reportDeprecated],
            )
        )
