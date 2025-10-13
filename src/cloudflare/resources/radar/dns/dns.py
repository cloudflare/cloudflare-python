# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .top import (
    TopResource,
    AsyncTopResource,
    TopResourceWithRawResponse,
    AsyncTopResourceWithRawResponse,
    TopResourceWithStreamingResponse,
    AsyncTopResourceWithStreamingResponse,
)
from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....types.radar import dns_summary_v2_params, dns_timeseries_params, dns_timeseries_groups_v2_params
from ...._base_client import make_request_options
from .timeseries_groups import (
    TimeseriesGroupsResource,
    AsyncTimeseriesGroupsResource,
    TimeseriesGroupsResourceWithRawResponse,
    AsyncTimeseriesGroupsResourceWithRawResponse,
    TimeseriesGroupsResourceWithStreamingResponse,
    AsyncTimeseriesGroupsResourceWithStreamingResponse,
)
from ....types.radar.dns_summary_v2_response import DNSSummaryV2Response
from ....types.radar.dns_timeseries_response import DNSTimeseriesResponse
from ....types.radar.dns_timeseries_groups_v2_response import DNSTimeseriesGroupsV2Response

__all__ = ["DNSResource", "AsyncDNSResource"]


class DNSResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        return SummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResource:
        return TimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DNSResourceWithStreamingResponse(self)

    def summary_v2(
        self,
        dimension: Literal[
            "IP_VERSION",
            "CACHE_HIT",
            "DNSSEC",
            "DNSSEC_AWARE",
            "DNSSEC_E2E",
            "MATCHING_ANSWER",
            "PROTOCOL",
            "QUERY_TYPE",
            "RESPONSE_CODE",
            "RESPONSE_TTL",
        ],
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: bool | Omit = omit,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | Omit = omit,
        query_type: Optional[
            Literal[
                "A",
                "AAAA",
                "A6",
                "AFSDB",
                "ANY",
                "APL",
                "ATMA",
                "AXFR",
                "CAA",
                "CDNSKEY",
                "CDS",
                "CERT",
                "CNAME",
                "CSYNC",
                "DHCID",
                "DLV",
                "DNAME",
                "DNSKEY",
                "DOA",
                "DS",
                "EID",
                "EUI48",
                "EUI64",
                "GPOS",
                "GID",
                "HINFO",
                "HIP",
                "HTTPS",
                "IPSECKEY",
                "ISDN",
                "IXFR",
                "KEY",
                "KX",
                "L32",
                "L64",
                "LOC",
                "LP",
                "MAILA",
                "MAILB",
                "MB",
                "MD",
                "MF",
                "MG",
                "MINFO",
                "MR",
                "MX",
                "NAPTR",
                "NB",
                "NBSTAT",
                "NID",
                "NIMLOC",
                "NINFO",
                "NS",
                "NSAP",
                "NSEC",
                "NSEC3",
                "NSEC3PARAM",
                "NULL",
                "NXT",
                "OPENPGPKEY",
                "OPT",
                "PTR",
                "PX",
                "RKEY",
                "RP",
                "RRSIG",
                "RT",
                "SIG",
                "SINK",
                "SMIMEA",
                "SOA",
                "SPF",
                "SRV",
                "SSHFP",
                "SVCB",
                "TA",
                "TALINK",
                "TKEY",
                "TLSA",
                "TSIG",
                "TXT",
                "UINFO",
                "UID",
                "UNSPEC",
                "URI",
                "WKS",
                "X25",
                "ZONEMD",
            ]
        ]
        | Omit = omit,
        response_code: Literal[
            "NOERROR",
            "FORMERR",
            "SERVFAIL",
            "NXDOMAIN",
            "NOTIMP",
            "REFUSED",
            "YXDOMAIN",
            "YXRRSET",
            "NXRRSET",
            "NOTAUTH",
            "NOTZONE",
            "BADSIG",
            "BADKEY",
            "BADTIME",
            "BADMODE",
            "BADNAME",
            "BADALG",
            "BADTRUNC",
            "BADCOOKIE",
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSSummaryV2Response:
        """
        Retrieves the distribution of DNS queries by the specified dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Specifies whether the response includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/dns/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    dns_summary_v2_params.DNSSummaryV2Params,
                ),
                post_parser=ResultWrapper[DNSSummaryV2Response]._unwrapper,
            ),
            cast_to=cast(Type[DNSSummaryV2Response], ResultWrapper[DNSSummaryV2Response]),
        )

    def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: bool | Omit = omit,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | Omit = omit,
        query_type: Optional[
            Literal[
                "A",
                "AAAA",
                "A6",
                "AFSDB",
                "ANY",
                "APL",
                "ATMA",
                "AXFR",
                "CAA",
                "CDNSKEY",
                "CDS",
                "CERT",
                "CNAME",
                "CSYNC",
                "DHCID",
                "DLV",
                "DNAME",
                "DNSKEY",
                "DOA",
                "DS",
                "EID",
                "EUI48",
                "EUI64",
                "GPOS",
                "GID",
                "HINFO",
                "HIP",
                "HTTPS",
                "IPSECKEY",
                "ISDN",
                "IXFR",
                "KEY",
                "KX",
                "L32",
                "L64",
                "LOC",
                "LP",
                "MAILA",
                "MAILB",
                "MB",
                "MD",
                "MF",
                "MG",
                "MINFO",
                "MR",
                "MX",
                "NAPTR",
                "NB",
                "NBSTAT",
                "NID",
                "NIMLOC",
                "NINFO",
                "NS",
                "NSAP",
                "NSEC",
                "NSEC3",
                "NSEC3PARAM",
                "NULL",
                "NXT",
                "OPENPGPKEY",
                "OPT",
                "PTR",
                "PX",
                "RKEY",
                "RP",
                "RRSIG",
                "RT",
                "SIG",
                "SINK",
                "SMIMEA",
                "SOA",
                "SPF",
                "SRV",
                "SSHFP",
                "SVCB",
                "TA",
                "TALINK",
                "TKEY",
                "TLSA",
                "TSIG",
                "TXT",
                "UINFO",
                "UID",
                "UNSPEC",
                "URI",
                "WKS",
                "X25",
                "ZONEMD",
            ]
        ]
        | Omit = omit,
        response_code: Literal[
            "NOERROR",
            "FORMERR",
            "SERVFAIL",
            "NXDOMAIN",
            "NOTIMP",
            "REFUSED",
            "YXDOMAIN",
            "YXRRSET",
            "NXRRSET",
            "NOTAUTH",
            "NOTZONE",
            "BADSIG",
            "BADKEY",
            "BADTIME",
            "BADMODE",
            "BADNAME",
            "BADALG",
            "BADTRUNC",
            "BADCOOKIE",
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSTimeseriesResponse:
        """
        Retrieves normalized query volume to the 1.1.1.1 DNS resolver over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Specifies whether the response includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    dns_timeseries_params.DNSTimeseriesParams,
                ),
                post_parser=ResultWrapper[DNSTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[DNSTimeseriesResponse], ResultWrapper[DNSTimeseriesResponse]),
        )

    def timeseries_groups_v2(
        self,
        dimension: Literal[
            "IP_VERSION",
            "CACHE_HIT",
            "DNSSEC",
            "DNSSEC_AWARE",
            "DNSSEC_E2E",
            "MATCHING_ANSWER",
            "PROTOCOL",
            "QUERY_TYPE",
            "RESPONSE_CODE",
            "RESPONSE_TTL",
        ],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: bool | Omit = omit,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | Omit = omit,
        query_type: Optional[
            Literal[
                "A",
                "AAAA",
                "A6",
                "AFSDB",
                "ANY",
                "APL",
                "ATMA",
                "AXFR",
                "CAA",
                "CDNSKEY",
                "CDS",
                "CERT",
                "CNAME",
                "CSYNC",
                "DHCID",
                "DLV",
                "DNAME",
                "DNSKEY",
                "DOA",
                "DS",
                "EID",
                "EUI48",
                "EUI64",
                "GPOS",
                "GID",
                "HINFO",
                "HIP",
                "HTTPS",
                "IPSECKEY",
                "ISDN",
                "IXFR",
                "KEY",
                "KX",
                "L32",
                "L64",
                "LOC",
                "LP",
                "MAILA",
                "MAILB",
                "MB",
                "MD",
                "MF",
                "MG",
                "MINFO",
                "MR",
                "MX",
                "NAPTR",
                "NB",
                "NBSTAT",
                "NID",
                "NIMLOC",
                "NINFO",
                "NS",
                "NSAP",
                "NSEC",
                "NSEC3",
                "NSEC3PARAM",
                "NULL",
                "NXT",
                "OPENPGPKEY",
                "OPT",
                "PTR",
                "PX",
                "RKEY",
                "RP",
                "RRSIG",
                "RT",
                "SIG",
                "SINK",
                "SMIMEA",
                "SOA",
                "SPF",
                "SRV",
                "SSHFP",
                "SVCB",
                "TA",
                "TALINK",
                "TKEY",
                "TLSA",
                "TSIG",
                "TXT",
                "UINFO",
                "UID",
                "UNSPEC",
                "URI",
                "WKS",
                "X25",
                "ZONEMD",
            ]
        ]
        | Omit = omit,
        response_code: Literal[
            "NOERROR",
            "FORMERR",
            "SERVFAIL",
            "NXDOMAIN",
            "NOTIMP",
            "REFUSED",
            "YXDOMAIN",
            "YXRRSET",
            "NXRRSET",
            "NOTAUTH",
            "NOTZONE",
            "BADSIG",
            "BADKEY",
            "BADTIME",
            "BADMODE",
            "BADNAME",
            "BADALG",
            "BADTRUNC",
            "BADCOOKIE",
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSTimeseriesGroupsV2Response:
        """
        Retrieves the distribution of DNS queries grouped by dimension over time.

        Args:
          dimension: Specifies the attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Specifies whether the response includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            f"/radar/dns/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    dns_timeseries_groups_v2_params.DNSTimeseriesGroupsV2Params,
                ),
                post_parser=ResultWrapper[DNSTimeseriesGroupsV2Response]._unwrapper,
            ),
            cast_to=cast(Type[DNSTimeseriesGroupsV2Response], ResultWrapper[DNSTimeseriesGroupsV2Response]),
        )


class AsyncDNSResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        return AsyncSummaryResource(self._client)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResource:
        return AsyncTimeseriesGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDNSResourceWithStreamingResponse(self)

    async def summary_v2(
        self,
        dimension: Literal[
            "IP_VERSION",
            "CACHE_HIT",
            "DNSSEC",
            "DNSSEC_AWARE",
            "DNSSEC_E2E",
            "MATCHING_ANSWER",
            "PROTOCOL",
            "QUERY_TYPE",
            "RESPONSE_CODE",
            "RESPONSE_TTL",
        ],
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: bool | Omit = omit,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | Omit = omit,
        query_type: Optional[
            Literal[
                "A",
                "AAAA",
                "A6",
                "AFSDB",
                "ANY",
                "APL",
                "ATMA",
                "AXFR",
                "CAA",
                "CDNSKEY",
                "CDS",
                "CERT",
                "CNAME",
                "CSYNC",
                "DHCID",
                "DLV",
                "DNAME",
                "DNSKEY",
                "DOA",
                "DS",
                "EID",
                "EUI48",
                "EUI64",
                "GPOS",
                "GID",
                "HINFO",
                "HIP",
                "HTTPS",
                "IPSECKEY",
                "ISDN",
                "IXFR",
                "KEY",
                "KX",
                "L32",
                "L64",
                "LOC",
                "LP",
                "MAILA",
                "MAILB",
                "MB",
                "MD",
                "MF",
                "MG",
                "MINFO",
                "MR",
                "MX",
                "NAPTR",
                "NB",
                "NBSTAT",
                "NID",
                "NIMLOC",
                "NINFO",
                "NS",
                "NSAP",
                "NSEC",
                "NSEC3",
                "NSEC3PARAM",
                "NULL",
                "NXT",
                "OPENPGPKEY",
                "OPT",
                "PTR",
                "PX",
                "RKEY",
                "RP",
                "RRSIG",
                "RT",
                "SIG",
                "SINK",
                "SMIMEA",
                "SOA",
                "SPF",
                "SRV",
                "SSHFP",
                "SVCB",
                "TA",
                "TALINK",
                "TKEY",
                "TLSA",
                "TSIG",
                "TXT",
                "UINFO",
                "UID",
                "UNSPEC",
                "URI",
                "WKS",
                "X25",
                "ZONEMD",
            ]
        ]
        | Omit = omit,
        response_code: Literal[
            "NOERROR",
            "FORMERR",
            "SERVFAIL",
            "NXDOMAIN",
            "NOTIMP",
            "REFUSED",
            "YXDOMAIN",
            "YXRRSET",
            "NXRRSET",
            "NOTAUTH",
            "NOTZONE",
            "BADSIG",
            "BADKEY",
            "BADTIME",
            "BADMODE",
            "BADNAME",
            "BADALG",
            "BADTRUNC",
            "BADCOOKIE",
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSSummaryV2Response:
        """
        Retrieves the distribution of DNS queries by the specified dimension.

        Args:
          dimension: Specifies the attribute by which to group the results.

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Specifies whether the response includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/dns/summary/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    dns_summary_v2_params.DNSSummaryV2Params,
                ),
                post_parser=ResultWrapper[DNSSummaryV2Response]._unwrapper,
            ),
            cast_to=cast(Type[DNSSummaryV2Response], ResultWrapper[DNSSummaryV2Response]),
        )

    async def timeseries(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: bool | Omit = omit,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | Omit = omit,
        query_type: Optional[
            Literal[
                "A",
                "AAAA",
                "A6",
                "AFSDB",
                "ANY",
                "APL",
                "ATMA",
                "AXFR",
                "CAA",
                "CDNSKEY",
                "CDS",
                "CERT",
                "CNAME",
                "CSYNC",
                "DHCID",
                "DLV",
                "DNAME",
                "DNSKEY",
                "DOA",
                "DS",
                "EID",
                "EUI48",
                "EUI64",
                "GPOS",
                "GID",
                "HINFO",
                "HIP",
                "HTTPS",
                "IPSECKEY",
                "ISDN",
                "IXFR",
                "KEY",
                "KX",
                "L32",
                "L64",
                "LOC",
                "LP",
                "MAILA",
                "MAILB",
                "MB",
                "MD",
                "MF",
                "MG",
                "MINFO",
                "MR",
                "MX",
                "NAPTR",
                "NB",
                "NBSTAT",
                "NID",
                "NIMLOC",
                "NINFO",
                "NS",
                "NSAP",
                "NSEC",
                "NSEC3",
                "NSEC3PARAM",
                "NULL",
                "NXT",
                "OPENPGPKEY",
                "OPT",
                "PTR",
                "PX",
                "RKEY",
                "RP",
                "RRSIG",
                "RT",
                "SIG",
                "SINK",
                "SMIMEA",
                "SOA",
                "SPF",
                "SRV",
                "SSHFP",
                "SVCB",
                "TA",
                "TALINK",
                "TKEY",
                "TLSA",
                "TSIG",
                "TXT",
                "UINFO",
                "UID",
                "UNSPEC",
                "URI",
                "WKS",
                "X25",
                "ZONEMD",
            ]
        ]
        | Omit = omit,
        response_code: Literal[
            "NOERROR",
            "FORMERR",
            "SERVFAIL",
            "NXDOMAIN",
            "NOTIMP",
            "REFUSED",
            "YXDOMAIN",
            "YXRRSET",
            "NXRRSET",
            "NOTAUTH",
            "NOTZONE",
            "BADSIG",
            "BADKEY",
            "BADTIME",
            "BADMODE",
            "BADNAME",
            "BADALG",
            "BADTRUNC",
            "BADCOOKIE",
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSTimeseriesResponse:
        """
        Retrieves normalized query volume to the 1.1.1.1 DNS resolver over time.

        Args:
          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Specifies whether the response includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    dns_timeseries_params.DNSTimeseriesParams,
                ),
                post_parser=ResultWrapper[DNSTimeseriesResponse]._unwrapper,
            ),
            cast_to=cast(Type[DNSTimeseriesResponse], ResultWrapper[DNSTimeseriesResponse]),
        )

    async def timeseries_groups_v2(
        self,
        dimension: Literal[
            "IP_VERSION",
            "CACHE_HIT",
            "DNSSEC",
            "DNSSEC_AWARE",
            "DNSSEC_E2E",
            "MATCHING_ANSWER",
            "PROTOCOL",
            "QUERY_TYPE",
            "RESPONSE_CODE",
            "RESPONSE_TTL",
        ],
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | Omit = omit,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        limit_per_group: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: bool | Omit = omit,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | Omit = omit,
        query_type: Optional[
            Literal[
                "A",
                "AAAA",
                "A6",
                "AFSDB",
                "ANY",
                "APL",
                "ATMA",
                "AXFR",
                "CAA",
                "CDNSKEY",
                "CDS",
                "CERT",
                "CNAME",
                "CSYNC",
                "DHCID",
                "DLV",
                "DNAME",
                "DNSKEY",
                "DOA",
                "DS",
                "EID",
                "EUI48",
                "EUI64",
                "GPOS",
                "GID",
                "HINFO",
                "HIP",
                "HTTPS",
                "IPSECKEY",
                "ISDN",
                "IXFR",
                "KEY",
                "KX",
                "L32",
                "L64",
                "LOC",
                "LP",
                "MAILA",
                "MAILB",
                "MB",
                "MD",
                "MF",
                "MG",
                "MINFO",
                "MR",
                "MX",
                "NAPTR",
                "NB",
                "NBSTAT",
                "NID",
                "NIMLOC",
                "NINFO",
                "NS",
                "NSAP",
                "NSEC",
                "NSEC3",
                "NSEC3PARAM",
                "NULL",
                "NXT",
                "OPENPGPKEY",
                "OPT",
                "PTR",
                "PX",
                "RKEY",
                "RP",
                "RRSIG",
                "RT",
                "SIG",
                "SINK",
                "SMIMEA",
                "SOA",
                "SPF",
                "SRV",
                "SSHFP",
                "SVCB",
                "TA",
                "TALINK",
                "TKEY",
                "TLSA",
                "TSIG",
                "TXT",
                "UINFO",
                "UID",
                "UNSPEC",
                "URI",
                "WKS",
                "X25",
                "ZONEMD",
            ]
        ]
        | Omit = omit,
        response_code: Literal[
            "NOERROR",
            "FORMERR",
            "SERVFAIL",
            "NXDOMAIN",
            "NOTIMP",
            "REFUSED",
            "YXDOMAIN",
            "YXRRSET",
            "NXRRSET",
            "NOTAUTH",
            "NOTZONE",
            "BADSIG",
            "BADKEY",
            "BADTIME",
            "BADMODE",
            "BADNAME",
            "BADALG",
            "BADTRUNC",
            "BADCOOKIE",
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSTimeseriesGroupsV2Response:
        """
        Retrieves the distribution of DNS queries grouped by dimension over time.

        Args:
          dimension: Specifies the attribute by which to group the results.

          agg_interval: Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).
              Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. When item count exceeds the limit, extra items appear grouped under
              an "other" category.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Specifies whether the response includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            f"/radar/dns/timeseries_groups/{dimension}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "asn": asn,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    dns_timeseries_groups_v2_params.DNSTimeseriesGroupsV2Params,
                ),
                post_parser=ResultWrapper[DNSTimeseriesGroupsV2Response]._unwrapper,
            ),
            cast_to=cast(Type[DNSTimeseriesGroupsV2Response], ResultWrapper[DNSTimeseriesGroupsV2Response]),
        )


class DNSResourceWithRawResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.summary_v2 = to_raw_response_wrapper(
            dns.summary_v2,
        )
        self.timeseries = to_raw_response_wrapper(
            dns.timeseries,
        )
        self.timeseries_groups_v2 = to_raw_response_wrapper(
            dns.timeseries_groups_v2,
        )

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._dns.top)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self._dns.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithRawResponse:
        return TimeseriesGroupsResourceWithRawResponse(self._dns.timeseries_groups)


class AsyncDNSResourceWithRawResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.summary_v2 = async_to_raw_response_wrapper(
            dns.summary_v2,
        )
        self.timeseries = async_to_raw_response_wrapper(
            dns.timeseries,
        )
        self.timeseries_groups_v2 = async_to_raw_response_wrapper(
            dns.timeseries_groups_v2,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._dns.top)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self._dns.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithRawResponse:
        return AsyncTimeseriesGroupsResourceWithRawResponse(self._dns.timeseries_groups)


class DNSResourceWithStreamingResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.summary_v2 = to_streamed_response_wrapper(
            dns.summary_v2,
        )
        self.timeseries = to_streamed_response_wrapper(
            dns.timeseries,
        )
        self.timeseries_groups_v2 = to_streamed_response_wrapper(
            dns.timeseries_groups_v2,
        )

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._dns.top)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self._dns.summary)

    @cached_property
    def timeseries_groups(self) -> TimeseriesGroupsResourceWithStreamingResponse:
        return TimeseriesGroupsResourceWithStreamingResponse(self._dns.timeseries_groups)


class AsyncDNSResourceWithStreamingResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.summary_v2 = async_to_streamed_response_wrapper(
            dns.summary_v2,
        )
        self.timeseries = async_to_streamed_response_wrapper(
            dns.timeseries,
        )
        self.timeseries_groups_v2 = async_to_streamed_response_wrapper(
            dns.timeseries_groups_v2,
        )

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._dns.top)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self._dns.summary)

    @cached_property
    def timeseries_groups(self) -> AsyncTimeseriesGroupsResourceWithStreamingResponse:
        return AsyncTimeseriesGroupsResourceWithStreamingResponse(self._dns.timeseries_groups)
