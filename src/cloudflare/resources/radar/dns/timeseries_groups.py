# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.radar.dns import (
    timeseries_group_dnssec_params,
    timeseries_group_protocol_params,
    timeseries_group_cache_hit_params,
    timeseries_group_dnssec_e2e_params,
    timeseries_group_ip_version_params,
    timeseries_group_query_type_params,
    timeseries_group_dnssec_aware_params,
    timeseries_group_response_ttl_params,
    timeseries_group_response_code_params,
    timeseries_group_matching_answer_params,
)
from ....types.radar.dns.timeseries_group_dnssec_response import TimeseriesGroupDNSSECResponse
from ....types.radar.dns.timeseries_group_protocol_response import TimeseriesGroupProtocolResponse
from ....types.radar.dns.timeseries_group_cache_hit_response import TimeseriesGroupCacheHitResponse
from ....types.radar.dns.timeseries_group_dnssec_e2e_response import TimeseriesGroupDNSSECE2EResponse
from ....types.radar.dns.timeseries_group_ip_version_response import TimeseriesGroupIPVersionResponse
from ....types.radar.dns.timeseries_group_query_type_response import TimeseriesGroupQueryTypeResponse
from ....types.radar.dns.timeseries_group_dnssec_aware_response import TimeseriesGroupDNSSECAwareResponse
from ....types.radar.dns.timeseries_group_response_ttl_response import TimeseriesGroupResponseTTLResponse
from ....types.radar.dns.timeseries_group_response_code_response import TimeseriesGroupResponseCodeResponse
from ....types.radar.dns.timeseries_group_matching_answer_response import TimeseriesGroupMatchingAnswerResponse

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

    def cache_hit(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupCacheHitResponse:
        """
        Retrieves the distribution of DNS queries by cache status over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/cache_hit",
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
                    timeseries_group_cache_hit_params.TimeseriesGroupCacheHitParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupCacheHitResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupCacheHitResponse], ResultWrapper[TimeseriesGroupCacheHitResponse]),
        )

    def dnssec(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupDNSSECResponse:
        """
        Retrieves the distribution of DNS responses by DNSSEC (DNS Security Extensions)
        support over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/dnssec",
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
                    timeseries_group_dnssec_params.TimeseriesGroupDNSSECParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDNSSECResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDNSSECResponse], ResultWrapper[TimeseriesGroupDNSSECResponse]),
        )

    def dnssec_aware(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupDNSSECAwareResponse:
        """
        Retrieves the distribution of DNS queries by DNSSEC (DNS Security Extensions)
        client awareness over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/dnssec_aware",
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
                    timeseries_group_dnssec_aware_params.TimeseriesGroupDNSSECAwareParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDNSSECAwareResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDNSSECAwareResponse], ResultWrapper[TimeseriesGroupDNSSECAwareResponse]),
        )

    def dnssec_e2e(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupDNSSECE2EResponse:
        """
        Retrieves the distribution of DNSSEC-validated answers by end-to-end security
        status over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/dnssec_e2e",
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
                    timeseries_group_dnssec_e2e_params.TimeseriesGroupDNSSECE2EParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDNSSECE2EResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDNSSECE2EResponse], ResultWrapper[TimeseriesGroupDNSSECE2EResponse]),
        )

    def ip_version(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupIPVersionResponse:
        """
        Retrieves the distribution of DNS queries by IP version over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/ip_version",
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
                    timeseries_group_ip_version_params.TimeseriesGroupIPVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupIPVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupIPVersionResponse], ResultWrapper[TimeseriesGroupIPVersionResponse]),
        )

    def matching_answer(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupMatchingAnswerResponse:
        """
        Retrieves the distribution of DNS queries by matching answers over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/matching_answer",
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
                    timeseries_group_matching_answer_params.TimeseriesGroupMatchingAnswerParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupMatchingAnswerResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[TimeseriesGroupMatchingAnswerResponse], ResultWrapper[TimeseriesGroupMatchingAnswerResponse]
            ),
        )

    def protocol(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupProtocolResponse:
        """
        Retrieves the distribution of DNS queries by DNS transport protocol over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/timeseries_groups/protocol",
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
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    timeseries_group_protocol_params.TimeseriesGroupProtocolParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupProtocolResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupProtocolResponse], ResultWrapper[TimeseriesGroupProtocolResponse]),
        )

    def query_type(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit_per_group: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupQueryTypeResponse:
        """
        Retrieves the distribution of DNS queries by type over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. If there are more items than the limit, the response will include
              the count of items, with any remaining items grouped together under an "other"
              category.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          response_code: Filters results by DNS response code.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/timeseries_groups/query_type",
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
                        "response_code": response_code,
                        "tld": tld,
                    },
                    timeseries_group_query_type_params.TimeseriesGroupQueryTypeParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupQueryTypeResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupQueryTypeResponse], ResultWrapper[TimeseriesGroupQueryTypeResponse]),
        )

    def response_code(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit_per_group: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupResponseCodeResponse:
        """
        Retrieves the distribution of DNS queries by response code over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. If there are more items than the limit, the response will include
              the count of items, with any remaining items grouped together under an "other"
              category.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/timeseries_groups/response_code",
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
                        "tld": tld,
                    },
                    timeseries_group_response_code_params.TimeseriesGroupResponseCodeParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupResponseCodeResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupResponseCodeResponse], ResultWrapper[TimeseriesGroupResponseCodeResponse]),
        )

    def response_ttl(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupResponseTTLResponse:
        """
        Retrieves the distribution of DNS queries by minimum answer TTL over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/response_ttl",
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
                    timeseries_group_response_ttl_params.TimeseriesGroupResponseTTLParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupResponseTTLResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupResponseTTLResponse], ResultWrapper[TimeseriesGroupResponseTTLResponse]),
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

    async def cache_hit(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupCacheHitResponse:
        """
        Retrieves the distribution of DNS queries by cache status over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/cache_hit",
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
                    timeseries_group_cache_hit_params.TimeseriesGroupCacheHitParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupCacheHitResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupCacheHitResponse], ResultWrapper[TimeseriesGroupCacheHitResponse]),
        )

    async def dnssec(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupDNSSECResponse:
        """
        Retrieves the distribution of DNS responses by DNSSEC (DNS Security Extensions)
        support over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/dnssec",
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
                    timeseries_group_dnssec_params.TimeseriesGroupDNSSECParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDNSSECResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDNSSECResponse], ResultWrapper[TimeseriesGroupDNSSECResponse]),
        )

    async def dnssec_aware(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupDNSSECAwareResponse:
        """
        Retrieves the distribution of DNS queries by DNSSEC (DNS Security Extensions)
        client awareness over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/dnssec_aware",
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
                    timeseries_group_dnssec_aware_params.TimeseriesGroupDNSSECAwareParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDNSSECAwareResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDNSSECAwareResponse], ResultWrapper[TimeseriesGroupDNSSECAwareResponse]),
        )

    async def dnssec_e2e(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupDNSSECE2EResponse:
        """
        Retrieves the distribution of DNSSEC-validated answers by end-to-end security
        status over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/dnssec_e2e",
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
                    timeseries_group_dnssec_e2e_params.TimeseriesGroupDNSSECE2EParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupDNSSECE2EResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupDNSSECE2EResponse], ResultWrapper[TimeseriesGroupDNSSECE2EResponse]),
        )

    async def ip_version(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupIPVersionResponse:
        """
        Retrieves the distribution of DNS queries by IP version over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/ip_version",
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
                    timeseries_group_ip_version_params.TimeseriesGroupIPVersionParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupIPVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupIPVersionResponse], ResultWrapper[TimeseriesGroupIPVersionResponse]),
        )

    async def matching_answer(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupMatchingAnswerResponse:
        """
        Retrieves the distribution of DNS queries by matching answers over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/matching_answer",
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
                    timeseries_group_matching_answer_params.TimeseriesGroupMatchingAnswerParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupMatchingAnswerResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[TimeseriesGroupMatchingAnswerResponse], ResultWrapper[TimeseriesGroupMatchingAnswerResponse]
            ),
        )

    async def protocol(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupProtocolResponse:
        """
        Retrieves the distribution of DNS queries by DNS transport protocol over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/timeseries_groups/protocol",
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
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    timeseries_group_protocol_params.TimeseriesGroupProtocolParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupProtocolResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupProtocolResponse], ResultWrapper[TimeseriesGroupProtocolResponse]),
        )

    async def query_type(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit_per_group: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupQueryTypeResponse:
        """
        Retrieves the distribution of DNS queries by type over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. If there are more items than the limit, the response will include
              the count of items, with any remaining items grouped together under an "other"
              category.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          response_code: Filters results by DNS response code.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/timeseries_groups/query_type",
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
                        "response_code": response_code,
                        "tld": tld,
                    },
                    timeseries_group_query_type_params.TimeseriesGroupQueryTypeParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupQueryTypeResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupQueryTypeResponse], ResultWrapper[TimeseriesGroupQueryTypeResponse]),
        )

    async def response_code(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit_per_group: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupResponseCodeResponse:
        """
        Retrieves the distribution of DNS queries by response code over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          limit_per_group: Limits the number of objects per group to the top items within the specified
              time range. If there are more items than the limit, the response will include
              the count of items, with any remaining items grouped together under an "other"
              category.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          tld: Filters results by country code top-level domain (ccTLD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/timeseries_groups/response_code",
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
                        "tld": tld,
                    },
                    timeseries_group_response_code_params.TimeseriesGroupResponseCodeParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupResponseCodeResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupResponseCodeResponse], ResultWrapper[TimeseriesGroupResponseCodeResponse]),
        )

    async def response_ttl(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        asn: List[str] | NotGiven = NOT_GIVEN,
        continent: List[str] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[str] | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        nodata: bool | NotGiven = NOT_GIVEN,
        protocol: Literal["UDP", "TCP", "HTTPS", "TLS"] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        tld: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeseriesGroupResponseTTLResponse:
        """
        Retrieves the distribution of DNS queries by minimum answer TTL over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          asn: Comma-separated list of Autonomous System Numbers (ASNs). Prefix with `-` to
              exclude ASNs from results. For example, `-174, 3356` excludes results from
              AS174, but includes results from AS3356.

          continent: Comma-separated list of continents (alpha-2 continent codes). Prefix with `-` to
              exclude continents from results. For example, `-EU,NA` excludes results from EU,
              but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by the specified date range. For example, use `7d` and
              `7dcontrol` to compare this week with the previous week. Use this parameter or
              set specific start and end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          format: Format in which results will be returned.

          location: Comma-separated list of locations (alpha-2 codes). Prefix with `-` to exclude
              locations from results. For example, `-US,PT` excludes results from the US, but
              includes results from PT.

          name: Array of names used to label the series in the response.

          nodata: Includes empty DNS responses (NODATA).

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
            "/radar/dns/timeseries_groups/response_ttl",
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
                    timeseries_group_response_ttl_params.TimeseriesGroupResponseTTLParams,
                ),
                post_parser=ResultWrapper[TimeseriesGroupResponseTTLResponse]._unwrapper,
            ),
            cast_to=cast(Type[TimeseriesGroupResponseTTLResponse], ResultWrapper[TimeseriesGroupResponseTTLResponse]),
        )


class TimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.cache_hit = to_raw_response_wrapper(
            timeseries_groups.cache_hit,
        )
        self.dnssec = to_raw_response_wrapper(
            timeseries_groups.dnssec,
        )
        self.dnssec_aware = to_raw_response_wrapper(
            timeseries_groups.dnssec_aware,
        )
        self.dnssec_e2e = to_raw_response_wrapper(
            timeseries_groups.dnssec_e2e,
        )
        self.ip_version = to_raw_response_wrapper(
            timeseries_groups.ip_version,
        )
        self.matching_answer = to_raw_response_wrapper(
            timeseries_groups.matching_answer,
        )
        self.protocol = to_raw_response_wrapper(
            timeseries_groups.protocol,
        )
        self.query_type = to_raw_response_wrapper(
            timeseries_groups.query_type,
        )
        self.response_code = to_raw_response_wrapper(
            timeseries_groups.response_code,
        )
        self.response_ttl = to_raw_response_wrapper(
            timeseries_groups.response_ttl,
        )


class AsyncTimeseriesGroupsResourceWithRawResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.cache_hit = async_to_raw_response_wrapper(
            timeseries_groups.cache_hit,
        )
        self.dnssec = async_to_raw_response_wrapper(
            timeseries_groups.dnssec,
        )
        self.dnssec_aware = async_to_raw_response_wrapper(
            timeseries_groups.dnssec_aware,
        )
        self.dnssec_e2e = async_to_raw_response_wrapper(
            timeseries_groups.dnssec_e2e,
        )
        self.ip_version = async_to_raw_response_wrapper(
            timeseries_groups.ip_version,
        )
        self.matching_answer = async_to_raw_response_wrapper(
            timeseries_groups.matching_answer,
        )
        self.protocol = async_to_raw_response_wrapper(
            timeseries_groups.protocol,
        )
        self.query_type = async_to_raw_response_wrapper(
            timeseries_groups.query_type,
        )
        self.response_code = async_to_raw_response_wrapper(
            timeseries_groups.response_code,
        )
        self.response_ttl = async_to_raw_response_wrapper(
            timeseries_groups.response_ttl,
        )


class TimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: TimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.cache_hit = to_streamed_response_wrapper(
            timeseries_groups.cache_hit,
        )
        self.dnssec = to_streamed_response_wrapper(
            timeseries_groups.dnssec,
        )
        self.dnssec_aware = to_streamed_response_wrapper(
            timeseries_groups.dnssec_aware,
        )
        self.dnssec_e2e = to_streamed_response_wrapper(
            timeseries_groups.dnssec_e2e,
        )
        self.ip_version = to_streamed_response_wrapper(
            timeseries_groups.ip_version,
        )
        self.matching_answer = to_streamed_response_wrapper(
            timeseries_groups.matching_answer,
        )
        self.protocol = to_streamed_response_wrapper(
            timeseries_groups.protocol,
        )
        self.query_type = to_streamed_response_wrapper(
            timeseries_groups.query_type,
        )
        self.response_code = to_streamed_response_wrapper(
            timeseries_groups.response_code,
        )
        self.response_ttl = to_streamed_response_wrapper(
            timeseries_groups.response_ttl,
        )


class AsyncTimeseriesGroupsResourceWithStreamingResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroupsResource) -> None:
        self._timeseries_groups = timeseries_groups

        self.cache_hit = async_to_streamed_response_wrapper(
            timeseries_groups.cache_hit,
        )
        self.dnssec = async_to_streamed_response_wrapper(
            timeseries_groups.dnssec,
        )
        self.dnssec_aware = async_to_streamed_response_wrapper(
            timeseries_groups.dnssec_aware,
        )
        self.dnssec_e2e = async_to_streamed_response_wrapper(
            timeseries_groups.dnssec_e2e,
        )
        self.ip_version = async_to_streamed_response_wrapper(
            timeseries_groups.ip_version,
        )
        self.matching_answer = async_to_streamed_response_wrapper(
            timeseries_groups.matching_answer,
        )
        self.protocol = async_to_streamed_response_wrapper(
            timeseries_groups.protocol,
        )
        self.query_type = async_to_streamed_response_wrapper(
            timeseries_groups.query_type,
        )
        self.response_code = async_to_streamed_response_wrapper(
            timeseries_groups.response_code,
        )
        self.response_ttl = async_to_streamed_response_wrapper(
            timeseries_groups.response_ttl,
        )
