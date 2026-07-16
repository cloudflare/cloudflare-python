# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["DNSTimeseriesGroupsV2Params"]


class DNSTimeseriesGroupsV2Params(TypedDict, total=False):
    agg_interval: Annotated[Literal["15m", "1h", "1d", "1w"], PropertyInfo(alias="aggInterval")]
    """Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).

    Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    When omitted, the interval is auto-selected from the requested date range; finer
    intervals are only available for shorter ranges. If the requested interval is
    too granular for the date range, the request is rejected.
    """

    asn: SequenceNotStr[str]
    """Filters results by Autonomous System.

    Specify one or more Autonomous System Numbers (ASNs) as a comma-separated list.
    Prefix with `-` to exclude ASNs from results. For example, `-174, 3356` excludes
    results from AS174, but includes results from AS3356.
    """

    cache_hit: Annotated[Iterable[bool], PropertyInfo(alias="cacheHit")]
    """Filters results based on cache status."""

    continent: SequenceNotStr[str]
    """Filters results by continent.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    continents from results. For example, `-EU,NA` excludes results from EU, but
    includes results from NA.
    """

    date_end: Annotated[SequenceNotStr[Union[str, datetime]], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateStart`. When requesting
    comparison series, every series must resolve to the same duration as the main
    series. Each `dateStart`/`dateEnd` is floored to the nearest 15 minutes before
    evaluation, so windows whose durations match only before alignment may be
    rejected.
    """

    date_range: Annotated[SequenceNotStr[str], PropertyInfo(alias="dateRange")]
    """
    Filters results by relative date range ending at the current time, with each
    value producing a separate series. Use `<n>d` for days (up to `364d`) or `<n>w`
    for weeks (up to `52w`). Append `control` to request the equivalent previous
    period for comparison: the comparison window is shifted back by the current
    window's length rounded up to a whole number of weeks, so it keeps the same
    weekday alignment and does not overlap the current window (e.g. `7dcontrol`
    covers days -14 to -7, `10dcontrol` covers days -24 to -14). For example, pass
    `7d` and `7dcontrol` to compare this week with the previous week. All series
    must resolve to the same duration as the main series; relative ranges (including
    `control`) satisfy this automatically. Use this parameter or set specific start
    and end dates (`dateStart` and `dateEnd` parameters).
    """

    date_start: Annotated[SequenceNotStr[Union[str, datetime]], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range.

    Alternative to `dateRange`; provide together with `dateEnd`. When requesting
    comparison series, every series must resolve to the same duration as the main
    series. Each `dateStart`/`dateEnd` is floored to the nearest 15 minutes before
    evaluation, so windows whose durations match only before alignment may be
    rejected.
    """

    dnssec: List[Literal["INVALID", "INSECURE", "SECURE", "OTHER"]]
    """Filters results based on DNSSEC (DNS Security Extensions) support."""

    dnssec_aware: Annotated[List[Literal["SUPPORTED", "NOT_SUPPORTED"]], PropertyInfo(alias="dnssecAware")]
    """Filters results based on DNSSEC (DNS Security Extensions) client awareness."""

    dnssec_e2e: Annotated[Iterable[bool], PropertyInfo(alias="dnssecE2e")]
    """
    Filters results based on DNSSEC-validated answers by end-to-end security status.
    """

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    ip_version: Annotated[List[Literal["IPv4", "IPv6"]], PropertyInfo(alias="ipVersion")]
    """Filters results by IP version (Ipv4 vs. IPv6)."""

    limit_per_group: Annotated[int, PropertyInfo(alias="limitPerGroup")]
    """
    Limits the number of objects per group to the top items within the specified
    time range. When item count exceeds the limit, extra items appear grouped under
    an "other" category. Only supported on high-cardinality dimensions; otherwise
    the request is rejected. Minimum value is 2.
    """

    location: SequenceNotStr[str]
    """Filters results by location.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    locations from results. For example, `-US,PT` excludes results from the US, but
    includes results from PT.
    """

    matching_answer: Annotated[Iterable[bool], PropertyInfo(alias="matchingAnswer")]
    """Filters results based on whether the queries have a matching answer."""

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""

    nodata: Iterable[bool]
    """Specifies whether the response includes empty DNS responses (NODATA)."""

    normalization: Literal["PERCENTAGE", "MIN0_MAX", "RANK"]
    """Normalization method applied to the results.

    Refer to
    [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
    `RANK` is only meaningful with the `TLD_DNS_MAGNITUDE` dimension, where it ranks
    TLDs by DNS query magnitude at each timestamp; for other dimensions it has no
    effect.
    """

    protocol: List[Literal["UDP", "TCP", "HTTPS", "TLS"]]
    """Filters results by DNS transport protocol."""

    query_type: Annotated[
        List[
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
        ],
        PropertyInfo(alias="queryType"),
    ]
    """Filters results by DNS query type."""

    response_code: Annotated[
        List[
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
        ],
        PropertyInfo(alias="responseCode"),
    ]
    """Filters results by DNS response code."""

    response_ttl: Annotated[
        List[
            Literal["LTE_1M", "GT_1M_LTE_5M", "GT_5M_LTE_15M", "GT_15M_LTE_1H", "GT_1H_LTE_1D", "GT_1D_LTE_1W", "GT_1W"]
        ],
        PropertyInfo(alias="responseTtl"),
    ]
    """Filters results by DNS response TTL."""

    tld: SequenceNotStr[str]
    """Filters results by top-level domain.

    Incompatible with the `ipVersion`, `protocol`, `dnssecE2e`, `dnssecAware`,
    `responseTtl`, and `cacheHit` filters/dimensions; this restriction does not
    apply to country-code TLDs (2-letter, e.g. `uk`).
    """
