# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SummaryDNSSECParams"]


class SummaryDNSSECParams(TypedDict, total=False):
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

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    location: SequenceNotStr[str]
    """Filters results by location.

    Specify a comma-separated list of alpha-2 codes. Prefix with `-` to exclude
    locations from results. For example, `-US,PT` excludes results from the US, but
    includes results from PT.
    """

    name: SequenceNotStr[str]
    """Array of names used to label the series in the response."""

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
