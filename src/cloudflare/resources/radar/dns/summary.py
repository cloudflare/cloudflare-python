# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
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
from ....types.radar.dns import (
    summary_dnssec_params,
    summary_protocol_params,
    summary_cache_hit_params,
    summary_dnssec_e2e_params,
    summary_ip_version_params,
    summary_query_type_params,
    summary_dnssec_aware_params,
    summary_response_ttl_params,
    summary_response_code_params,
    summary_matching_answer_params,
)
from ....types.radar.dns.summary_dnssec_response import SummaryDNSSECResponse
from ....types.radar.dns.summary_protocol_response import SummaryProtocolResponse
from ....types.radar.dns.summary_cache_hit_response import SummaryCacheHitResponse
from ....types.radar.dns.summary_dnssec_e2e_response import SummaryDNSSECE2EResponse
from ....types.radar.dns.summary_ip_version_response import SummaryIPVersionResponse
from ....types.radar.dns.summary_query_type_response import SummaryQueryTypeResponse
from ....types.radar.dns.summary_dnssec_aware_response import SummaryDNSSECAwareResponse
from ....types.radar.dns.summary_response_ttl_response import SummaryResponseTTLResponse
from ....types.radar.dns.summary_response_code_response import SummaryResponseCodeResponse
from ....types.radar.dns.summary_matching_answer_response import SummaryMatchingAnswerResponse

__all__ = ["SummaryResource", "AsyncSummaryResource"]


class SummaryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SummaryResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    def cache_hit(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryCacheHitResponse:
        """
        Retrieves the distribution of DNS queries by cache status.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/summary/cache_hit",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_cache_hit_params.SummaryCacheHitParams,
                ),
                post_parser=ResultWrapper[SummaryCacheHitResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryCacheHitResponse], ResultWrapper[SummaryCacheHitResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    def dnssec(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryDNSSECResponse:
        """
        Retrieves the distribution of DNS responses by DNSSEC (DNS Security Extensions)
        support.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/summary/dnssec",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_dnssec_params.SummaryDNSSECParams,
                ),
                post_parser=ResultWrapper[SummaryDNSSECResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryDNSSECResponse], ResultWrapper[SummaryDNSSECResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    def dnssec_aware(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryDNSSECAwareResponse:
        """
        Retrieves the distribution of DNS queries by DNSSEC (DNS Security Extensions)
        client awareness.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/summary/dnssec_aware",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_dnssec_aware_params.SummaryDNSSECAwareParams,
                ),
                post_parser=ResultWrapper[SummaryDNSSECAwareResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryDNSSECAwareResponse], ResultWrapper[SummaryDNSSECAwareResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    def dnssec_e2e(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryDNSSECE2EResponse:
        """
        Retrieves the distribution of DNSSEC-validated answers by end-to-end security
        status.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/summary/dnssec_e2e",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_dnssec_e2e_params.SummaryDNSSECE2EParams,
                ),
                post_parser=ResultWrapper[SummaryDNSSECE2EResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryDNSSECE2EResponse], ResultWrapper[SummaryDNSSECE2EResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    def ip_version(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryIPVersionResponse:
        """
        Retrieves the distribution of DNS queries by IP version.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/summary/ip_version",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_ip_version_params.SummaryIPVersionParams,
                ),
                post_parser=ResultWrapper[SummaryIPVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryIPVersionResponse], ResultWrapper[SummaryIPVersionResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    def matching_answer(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryMatchingAnswerResponse:
        """
        Retrieves the distribution of DNS queries by matching answers.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/summary/matching_answer",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_matching_answer_params.SummaryMatchingAnswerParams,
                ),
                post_parser=ResultWrapper[SummaryMatchingAnswerResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryMatchingAnswerResponse], ResultWrapper[SummaryMatchingAnswerResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    def protocol(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: Iterable[bool] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryProtocolResponse:
        """
        Retrieves the distribution of DNS queries by DNS transport protocol.

        Args:
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

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/summary/protocol",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_protocol_params.SummaryProtocolParams,
                ),
                post_parser=ResultWrapper[SummaryProtocolResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryProtocolResponse], ResultWrapper[SummaryProtocolResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    def query_type(
        self,
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
        nodata: Iterable[bool] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "HTTPS", "TLS"]] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryQueryTypeResponse:
        """
        Retrieves the distribution of DNS queries by type.

        Args:
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

          response_code: Filters results by DNS response code.

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/summary/query_type",
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
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_query_type_params.SummaryQueryTypeParams,
                ),
                post_parser=ResultWrapper[SummaryQueryTypeResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryQueryTypeResponse], ResultWrapper[SummaryQueryTypeResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    def response_code(
        self,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryResponseCodeResponse:
        """
        Retrieves the distribution of DNS queries by response code.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/summary/response_code",
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
                        "tld": tld,
                    },
                    summary_response_code_params.SummaryResponseCodeParams,
                ),
                post_parser=ResultWrapper[SummaryResponseCodeResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryResponseCodeResponse], ResultWrapper[SummaryResponseCodeResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    def response_ttl(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryResponseTTLResponse:
        """
        Retrieves the distribution of DNS queries by minimum response TTL.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/dns/summary/response_ttl",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_response_ttl_params.SummaryResponseTTLParams,
                ),
                post_parser=ResultWrapper[SummaryResponseTTLResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryResponseTTLResponse], ResultWrapper[SummaryResponseTTLResponse]),
        )


class AsyncSummaryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSummaryResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    async def cache_hit(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryCacheHitResponse:
        """
        Retrieves the distribution of DNS queries by cache status.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/summary/cache_hit",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_cache_hit_params.SummaryCacheHitParams,
                ),
                post_parser=ResultWrapper[SummaryCacheHitResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryCacheHitResponse], ResultWrapper[SummaryCacheHitResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    async def dnssec(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryDNSSECResponse:
        """
        Retrieves the distribution of DNS responses by DNSSEC (DNS Security Extensions)
        support.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/summary/dnssec",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_dnssec_params.SummaryDNSSECParams,
                ),
                post_parser=ResultWrapper[SummaryDNSSECResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryDNSSECResponse], ResultWrapper[SummaryDNSSECResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    async def dnssec_aware(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryDNSSECAwareResponse:
        """
        Retrieves the distribution of DNS queries by DNSSEC (DNS Security Extensions)
        client awareness.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/summary/dnssec_aware",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_dnssec_aware_params.SummaryDNSSECAwareParams,
                ),
                post_parser=ResultWrapper[SummaryDNSSECAwareResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryDNSSECAwareResponse], ResultWrapper[SummaryDNSSECAwareResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    async def dnssec_e2e(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryDNSSECE2EResponse:
        """
        Retrieves the distribution of DNSSEC-validated answers by end-to-end security
        status.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/summary/dnssec_e2e",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_dnssec_e2e_params.SummaryDNSSECE2EParams,
                ),
                post_parser=ResultWrapper[SummaryDNSSECE2EResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryDNSSECE2EResponse], ResultWrapper[SummaryDNSSECE2EResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    async def ip_version(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryIPVersionResponse:
        """
        Retrieves the distribution of DNS queries by IP version.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/summary/ip_version",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_ip_version_params.SummaryIPVersionParams,
                ),
                post_parser=ResultWrapper[SummaryIPVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryIPVersionResponse], ResultWrapper[SummaryIPVersionResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    async def matching_answer(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryMatchingAnswerResponse:
        """
        Retrieves the distribution of DNS queries by matching answers.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/summary/matching_answer",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_matching_answer_params.SummaryMatchingAnswerParams,
                ),
                post_parser=ResultWrapper[SummaryMatchingAnswerResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryMatchingAnswerResponse], ResultWrapper[SummaryMatchingAnswerResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    async def protocol(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
        name: SequenceNotStr[str] | Omit = omit,
        nodata: Iterable[bool] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryProtocolResponse:
        """
        Retrieves the distribution of DNS queries by DNS transport protocol.

        Args:
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

          query_type: Filters results by DNS query type.

          response_code: Filters results by DNS response code.

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/summary/protocol",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_protocol_params.SummaryProtocolParams,
                ),
                post_parser=ResultWrapper[SummaryProtocolResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryProtocolResponse], ResultWrapper[SummaryProtocolResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    async def query_type(
        self,
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
        nodata: Iterable[bool] | Omit = omit,
        protocol: List[Literal["UDP", "TCP", "HTTPS", "TLS"]] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryQueryTypeResponse:
        """
        Retrieves the distribution of DNS queries by type.

        Args:
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

          response_code: Filters results by DNS response code.

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/summary/query_type",
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
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_query_type_params.SummaryQueryTypeParams,
                ),
                post_parser=ResultWrapper[SummaryQueryTypeResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryQueryTypeResponse], ResultWrapper[SummaryQueryTypeResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    async def response_code(
        self,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryResponseCodeResponse:
        """
        Retrieves the distribution of DNS queries by response code.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/summary/response_code",
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
                        "tld": tld,
                    },
                    summary_response_code_params.SummaryResponseCodeParams,
                ),
                post_parser=ResultWrapper[SummaryResponseCodeResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryResponseCodeResponse], ResultWrapper[SummaryResponseCodeResponse]),
        )

    @typing_extensions.deprecated(
        "Use [Radar DNS Summary By Dimension](https://developers.cloudflare.com/api/resources/radar/subresources/dns/methods/summary_v2/) instead."
    )
    async def response_ttl(
        self,
        *,
        asn: SequenceNotStr[str] | Omit = omit,
        continent: SequenceNotStr[str] | Omit = omit,
        date_end: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        date_range: SequenceNotStr[str] | Omit = omit,
        date_start: SequenceNotStr[Union[str, datetime]] | Omit = omit,
        format: Literal["JSON", "CSV"] | Omit = omit,
        location: SequenceNotStr[str] | Omit = omit,
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
        tld: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryResponseTTLResponse:
        """
        Retrieves the distribution of DNS queries by minimum response TTL.

        Args:
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

          tld: Filters results by top-level domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/dns/summary/response_ttl",
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
                        "location": location,
                        "name": name,
                        "nodata": nodata,
                        "protocol": protocol,
                        "query_type": query_type,
                        "response_code": response_code,
                        "tld": tld,
                    },
                    summary_response_ttl_params.SummaryResponseTTLParams,
                ),
                post_parser=ResultWrapper[SummaryResponseTTLResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryResponseTTLResponse], ResultWrapper[SummaryResponseTTLResponse]),
        )


class SummaryResourceWithRawResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.cache_hit = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.cache_hit,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.dnssec,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec_aware = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.dnssec_aware,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec_e2e = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.dnssec_e2e,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.matching_answer = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.matching_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.protocol = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.protocol,  # pyright: ignore[reportDeprecated],
            )
        )
        self.query_type = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.query_type,  # pyright: ignore[reportDeprecated],
            )
        )
        self.response_code = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.response_code,  # pyright: ignore[reportDeprecated],
            )
        )
        self.response_ttl = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                summary.response_ttl,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncSummaryResourceWithRawResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.cache_hit = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.cache_hit,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.dnssec,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec_aware = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.dnssec_aware,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec_e2e = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.dnssec_e2e,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.matching_answer = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.matching_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.protocol = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.protocol,  # pyright: ignore[reportDeprecated],
            )
        )
        self.query_type = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.query_type,  # pyright: ignore[reportDeprecated],
            )
        )
        self.response_code = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.response_code,  # pyright: ignore[reportDeprecated],
            )
        )
        self.response_ttl = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                summary.response_ttl,  # pyright: ignore[reportDeprecated],
            )
        )


class SummaryResourceWithStreamingResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.cache_hit = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.cache_hit,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.dnssec,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec_aware = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.dnssec_aware,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec_e2e = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.dnssec_e2e,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.matching_answer = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.matching_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.protocol = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.protocol,  # pyright: ignore[reportDeprecated],
            )
        )
        self.query_type = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.query_type,  # pyright: ignore[reportDeprecated],
            )
        )
        self.response_code = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.response_code,  # pyright: ignore[reportDeprecated],
            )
        )
        self.response_ttl = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                summary.response_ttl,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncSummaryResourceWithStreamingResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.cache_hit = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.cache_hit,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.dnssec,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec_aware = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.dnssec_aware,  # pyright: ignore[reportDeprecated],
            )
        )
        self.dnssec_e2e = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.dnssec_e2e,  # pyright: ignore[reportDeprecated],
            )
        )
        self.ip_version = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.ip_version,  # pyright: ignore[reportDeprecated],
            )
        )
        self.matching_answer = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.matching_answer,  # pyright: ignore[reportDeprecated],
            )
        )
        self.protocol = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.protocol,  # pyright: ignore[reportDeprecated],
            )
        )
        self.query_type = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.query_type,  # pyright: ignore[reportDeprecated],
            )
        )
        self.response_code = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.response_code,  # pyright: ignore[reportDeprecated],
            )
        )
        self.response_ttl = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                summary.response_ttl,  # pyright: ignore[reportDeprecated],
            )
        )
