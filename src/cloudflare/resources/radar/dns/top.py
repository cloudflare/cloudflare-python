# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from ...._base_client import make_request_options
from ....types.radar.dns import top_ases_params, top_locations_params
from ....types.radar.dns.top_ases_response import TopAsesResponse
from ....types.radar.dns.top_locations_response import TopLocationsResponse

__all__ = ["TopResource", "AsyncTopResource"]


class TopResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TopResourceWithStreamingResponse(self)

    def ases(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        cache_hit: Iterable[bool] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dnssec: List[Literal["INVALID", "INSECURE", "SECURE", "OTHER"]] | Omit = omit,
        dnssec_aware: List[Literal["SUPPORTED", "NOT_SUPPORTED"]] | Omit = omit,
        dnssec_e2e: Iterable[bool] | Omit = omit,
        domain: SequenceNotStr[str] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        matching_answer: Iterable[bool] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: Iterable[bool] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "HTTPS", "TLS"]] | Omit = omit,
        query_type: List[
            Optional[
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
        ]
        | Omit = omit,
        response_code: List[
            Literal[
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
        ]
        | Omit = omit,
        response_ttl: List[
            Literal["LTE_1M", "GT_1M_LTE_5M", "GT_5M_LTE_15M", "GT_15M_LTE_1H", "GT_1H_LTE_1D", "GT_1D_LTE_1W", "GT_1W"]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopAsesResponse:
        """
        Retrieves the top autonomous systems by DNS queries made to 1.1.1.1 DNS
        resolver.

        Args:
          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          cache_hit: Filters results based on cache status.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dnssec: Filters results based on DNSSEC (DNS Security Extensions) support.

          dnssec_aware: Filters results based on DNSSEC (DNS Security Extensions) client awareness.

          dnssec_e2e: Filters results based on DNSSEC-validated answers by end-to-end security status.

          domain: Filters results by domain name.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit: Limits the number of objects returned in the response.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          matching_answer: Filters results based on whether the queries have a matching answer.

          name: Array of names used to label the series in the response.

          nodata: Specifies whether the response includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          response_ttl: Filters results by DNS response TTL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/top/ases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "cache_hit": cache_hit,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dnssec": dnssec,
                        "dnssec_aware": dnssec_aware,
                        "dnssec_e2e": dnssec_e2e,
                        "domain": domain,
                        "format": format,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "matching_answer": matching_answer,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "response_ttl": response_ttl,
                    },
                    top_ases_params.TopAsesParams,
                ),
                post_parser=ResultWrapper[TopAsesResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopAsesResponse], ResultWrapper[TopAsesResponse]),
        )

    def locations(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        cache_hit: Iterable[bool] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dnssec: List[Literal["INVALID", "INSECURE", "SECURE", "OTHER"]] | Omit = omit,
        dnssec_aware: List[Literal["SUPPORTED", "NOT_SUPPORTED"]] | Omit = omit,
        dnssec_e2e: Iterable[bool] | Omit = omit,
        domain: SequenceNotStr[str] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        matching_answer: Iterable[bool] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: Iterable[bool] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "HTTPS", "TLS"]] | Omit = omit,
        query_type: List[
            Optional[
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
        ]
        | Omit = omit,
        response_code: List[
            Literal[
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
        ]
        | Omit = omit,
        response_ttl: List[
            Literal["LTE_1M", "GT_1M_LTE_5M", "GT_5M_LTE_15M", "GT_15M_LTE_1H", "GT_1H_LTE_1D", "GT_1D_LTE_1W", "GT_1W"]
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopLocationsResponse:
        """
        Retrieves the top locations by DNS queries made to 1.1.1.1 DNS resolver.

        Args:
          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          cache_hit: Filters results based on cache status.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dnssec: Filters results based on DNSSEC (DNS Security Extensions) support.

          dnssec_aware: Filters results based on DNSSEC (DNS Security Extensions) client awareness.

          dnssec_e2e: Filters results based on DNSSEC-validated answers by end-to-end security status.

          domain: Filters results by domain name.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit: Limits the number of objects returned in the response.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          matching_answer: Filters results based on whether the queries have a matching answer.

          name: Array of names used to label the series in the response.

          nodata: Specifies whether the response includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          response_ttl: Filters results by DNS response TTL.

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/top/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "cache_hit": cache_hit,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dnssec": dnssec,
                        "dnssec_aware": dnssec_aware,
                        "dnssec_e2e": dnssec_e2e,
                        "domain": domain,
                        "format": format,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "matching_answer": matching_answer,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "response_ttl": response_ttl,
                        "tld": tld,
                    },
                    top_locations_params.TopLocationsParams,
                ),
                post_parser=ResultWrapper[TopLocationsResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopLocationsResponse], ResultWrapper[TopLocationsResponse]),
        )


class AsyncTopResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTopResourceWithStreamingResponse(self)

    async def ases(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        cache_hit: Iterable[bool] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dnssec: List[Literal["INVALID", "INSECURE", "SECURE", "OTHER"]] | Omit = omit,
        dnssec_aware: List[Literal["SUPPORTED", "NOT_SUPPORTED"]] | Omit = omit,
        dnssec_e2e: Iterable[bool] | Omit = omit,
        domain: SequenceNotStr[str] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        matching_answer: Iterable[bool] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: Iterable[bool] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "HTTPS", "TLS"]] | Omit = omit,
        query_type: List[
            Optional[
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
        ]
        | Omit = omit,
        response_code: List[
            Literal[
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
        ]
        | Omit = omit,
        response_ttl: List[
            Literal["LTE_1M", "GT_1M_LTE_5M", "GT_5M_LTE_15M", "GT_15M_LTE_1H", "GT_1H_LTE_1D", "GT_1D_LTE_1W", "GT_1W"]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopAsesResponse:
        """
        Retrieves the top autonomous systems by DNS queries made to 1.1.1.1 DNS
        resolver.

        Args:
          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          cache_hit: Filters results based on cache status.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dnssec: Filters results based on DNSSEC (DNS Security Extensions) support.

          dnssec_aware: Filters results based on DNSSEC (DNS Security Extensions) client awareness.

          dnssec_e2e: Filters results based on DNSSEC-validated answers by end-to-end security status.

          domain: Filters results by domain name.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit: Limits the number of objects returned in the response.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          matching_answer: Filters results based on whether the queries have a matching answer.

          name: Array of names used to label the series in the response.

          nodata: Specifies whether the response includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          response_ttl: Filters results by DNS response TTL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/top/ases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "cache_hit": cache_hit,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dnssec": dnssec,
                        "dnssec_aware": dnssec_aware,
                        "dnssec_e2e": dnssec_e2e,
                        "domain": domain,
                        "format": format,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "matching_answer": matching_answer,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "response_ttl": response_ttl,
                    },
                    top_ases_params.TopAsesParams,
                ),
                post_parser=ResultWrapper[TopAsesResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopAsesResponse], ResultWrapper[TopAsesResponse]),
        )

    async def locations(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        cache_hit: Iterable[bool] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        dnssec: List[Literal["INVALID", "INSECURE", "SECURE", "OTHER"]] | Omit = omit,
        dnssec_aware: List[Literal["SUPPORTED", "NOT_SUPPORTED"]] | Omit = omit,
        dnssec_e2e: Iterable[bool] | Omit = omit,
        domain: SequenceNotStr[str] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        ip_version: List[Literal["IPv4", "IPv6"]] | Omit = omit,
        limit: int | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        matching_answer: Iterable[bool] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: Iterable[bool] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "HTTPS", "TLS"]] | Omit = omit,
        query_type: List[
            Optional[
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
        ]
        | Omit = omit,
        response_code: List[
            Literal[
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
        ]
        | Omit = omit,
        response_ttl: List[
            Literal["LTE_1M", "GT_1M_LTE_5M", "GT_5M_LTE_15M", "GT_15M_LTE_1H", "GT_1H_LTE_1D", "GT_1D_LTE_1W", "GT_1W"]
        ]
        | Omit = omit,
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopLocationsResponse:
        """
        Retrieves the top locations by DNS queries made to 1.1.1.1 DNS resolver.

        Args:
          asn: Filters results by Autonomous System. Specify one or more Autonomous System
              Numbers (ASNs) as a comma-separated list. Prefix with `-` to exclude ASNs from
              results. For example, `-174, 3356` excludes results from AS174, but includes
              results from AS3356.

          cache_hit: Filters results based on cache status.

          continent: Filters results by continent. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude continents from results. For example, `-EU,NA`
              excludes results from EU, but includes results from NA.

          date_end: End of the date range (inclusive).

          date_range: Filters results by date range. For example, use `7d` and `7dcontrol` to compare
              this week with the previous week. Use this parameter or set specific start and
              end dates (`dateStart` and `dateEnd` parameters).

          date_start: Start of the date range.

          dnssec: Filters results based on DNSSEC (DNS Security Extensions) support.

          dnssec_aware: Filters results based on DNSSEC (DNS Security Extensions) client awareness.

          dnssec_e2e: Filters results based on DNSSEC-validated answers by end-to-end security status.

          domain: Filters results by domain name.

          format: Format in which results will be returned.

          ip_version: Filters results by IP version (Ipv4 vs. IPv6).

          limit: Limits the number of objects returned in the response.

          location: Filters results by location. Specify a comma-separated list of alpha-2 codes.
              Prefix with `-` to exclude locations from results. For example, `-US,PT`
              excludes results from the US, but includes results from PT.

          matching_answer: Filters results based on whether the queries have a matching answer.

          name: Array of names used to label the series in the response.

          nodata: Specifies whether the response includes empty DNS responses (NODATA).

          protocol: Filters results by DNS transport protocol.

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          response_ttl: Filters results by DNS response TTL.

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/top/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asn": asn,
                        "cache_hit": cache_hit,
                        "continent": continent,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "dnssec": dnssec,
                        "dnssec_aware": dnssec_aware,
                        "dnssec_e2e": dnssec_e2e,
                        "domain": domain,
                        "format": format,
                        "ip_version": ip_version,
                        "limit": limit,
                        "location": location,
                        "matching_answer": matching_answer,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "response_ttl": response_ttl,
                        "tld": tld,
                    },
                    top_locations_params.TopLocationsParams,
                ),
                post_parser=ResultWrapper[TopLocationsResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopLocationsResponse], ResultWrapper[TopLocationsResponse]),
        )


class TopResourceWithRawResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.ases = to_raw_response_wrapper(
            top.ases,
        )
        self.locations = to_raw_response_wrapper(
            top.locations,
        )


class AsyncTopResourceWithRawResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.ases = async_to_raw_response_wrapper(
            top.ases,
        )
        self.locations = async_to_raw_response_wrapper(
            top.locations,
        )


class TopResourceWithStreamingResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

        self.ases = to_streamed_response_wrapper(
            top.ases,
        )
        self.locations = to_streamed_response_wrapper(
            top.locations,
        )


class AsyncTopResourceWithStreamingResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

        self.ases = async_to_streamed_response_wrapper(
            top.ases,
        )
        self.locations = async_to_streamed_response_wrapper(
            top.locations,
        )
