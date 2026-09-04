# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AnnotationListParams"]


class AnnotationListParams(TypedDict, total=False):
    asn: int
    """Filters results by Autonomous System.

    Specify a single Autonomous System Number (ASN) as integer.
    """

    bot: str
    """Filters results by bot."""

    ca: str
    """Filters results by certificate authority."""

    data_source: Annotated[
        Literal[
            "ALL",
            "AI_BOTS",
            "AI_GATEWAY",
            "BGP",
            "BOTS",
            "CONNECTION_ANOMALY",
            "CT",
            "DNS",
            "DNS_MAGNITUDE",
            "DNS_AS112",
            "DOS",
            "EMAIL_ROUTING",
            "EMAIL_SECURITY",
            "FW",
            "FW_PG",
            "HTTP",
            "HTTP_CONTROL",
            "HTTP_CRAWLER_REFERER",
            "HTTP_ORIGINS",
            "IQI",
            "LEAKED_CREDENTIALS",
            "NET",
            "ROBOTS_TXT",
            "SPEED",
            "WORKERS_AI",
        ],
        PropertyInfo(alias="dataSource"),
    ]
    """Filters results by data source."""

    date_end: Annotated[Union[str, datetime], PropertyInfo(alias="dateEnd", format="iso8601")]
    """End of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateStart`.
    """

    date_range: Annotated[str, PropertyInfo(alias="dateRange")]
    """Filters results by a relative date range ending at the current time.

    Use `<n>d` for days (up to `364d`) or `<n>w` for weeks (up to `52w`), e.g. `7d`.
    Append `control` to request the equivalent previous period for comparison: the
    comparison window is shifted back by the current window's length rounded up to a
    whole number of weeks, so it keeps the same weekday alignment and does not
    overlap the current window (e.g. `3dcontrol` covers days -10 to -7, `7dcontrol`
    covers days -14 to -7, `28dcontrol` covers days -56 to -28, and `10dcontrol`
    covers days -24 to -14). Mutually exclusive with `dateStart`/`dateEnd`.
    """

    date_start: Annotated[Union[str, datetime], PropertyInfo(alias="dateStart", format="iso8601")]
    """Start of the date range (inclusive).

    Alternative to `dateRange`; provide together with `dateEnd`.
    """

    event_type: Annotated[
        Literal["EVENT", "GENERAL", "OUTAGE", "PARTIAL_PROJECTION", "PIPELINE", "TRAFFIC_ANOMALY"],
        PropertyInfo(alias="eventType"),
    ]
    """Filters results by event type. EVENT is a legacy alias for GENERAL."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    geo_id: Annotated[str, PropertyInfo(alias="geoId")]
    """Filters results by geolocation.

    Refer to [GeoNames](https://download.geonames.org/export/dump/readme.txt).
    """

    limit: int
    """Limits the number of objects returned in the response."""

    location: str
    """Filters results by location. Specify an alpha-2 location code."""

    log: str
    """Filters results by certificate log."""

    offset: int
    """Skips the specified number of objects before fetching the results."""

    origin: str
    """Filters results by origin."""

    outage_cause: Annotated[
        Literal[
            "BLOCKING",
            "CABLE_CUT",
            "CYBERATTACK",
            "DNS",
            "FIRE",
            "GOVERNMENT_DIRECTED",
            "MAINTENANCE",
            "MECHANICAL",
            "MILITARY_ACTION",
            "MISCONFIGURATION",
            "NATURAL_DISASTER",
            "NETWORK_PROBLEM",
            "POWER_OUTAGE",
            "SOFTWARE",
            "TECHNICAL_PROBLEM",
            "UNKNOWN",
            "WEATHER",
        ],
        PropertyInfo(alias="outageCause"),
    ]
    """Filters results by outage cause."""

    outage_type: Annotated[Literal["NATIONWIDE", "REGIONAL", "NETWORK", "PLATFORM"], PropertyInfo(alias="outageType")]
    """Filters results by outage type."""

    query: str
    """
    Filters results by a free-text match on the annotation description, id, or
    linked entities (location, ASN, origin).
    """

    tags: List[
        Literal[
            "ADM1",
            "ADM2",
            "API_TRAFFIC",
            "ARC",
            "AS",
            "ASN",
            "ATTACKS",
            "AUTHOR",
            "BANDWIDTH",
            "BITRATE",
            "BOT",
            "BOT_CATEGORY",
            "BOT_CLASS",
            "BOT_KIND",
            "BOT_OPERATOR",
            "BROWSER",
            "BROWSER_FAMILY",
            "BYTES",
            "CA",
            "CACHE_HIT",
            "CA_OWNER",
            "CHECK_RESULT",
            "CLIENT_TYPE",
            "COMPROMISED",
            "CONTENT_TYPE",
            "CRAWL_PURPOSE",
            "CRAWL_REFER_RATIO",
            "DEVICE_TYPE",
            "DKIM",
            "DMARC",
            "DNS",
            "DNSSEC",
            "DNSSEC_AWARE",
            "DNSSEC_E2E",
            "DOMAIN_CATEGORY",
            "DURATION",
            "EDNS",
            "ENCRYPTED",
            "ENTRY_TYPE",
            "EXPIRATION_STATUS",
            "HAS_IPS",
            "HAS_MATCHING_ANSWER",
            "HAS_WILDCARDS",
            "HTTP_METHOD",
            "HTTP_PROTOCOL",
            "HTTP_VERSION",
            "INDUSTRY",
            "IP_VERSION",
            "JITTER",
            "KEY_AGREEMENT",
            "LATENCY",
            "LOCATION",
            "LOCATION_LATENCY",
            "LOG",
            "LOG_API",
            "LOG_OPERATOR",
            "MALICIOUS",
            "MANAGED_RULES",
            "MITIGATION_PRODUCT",
            "MODEL",
            "NAMESERVER_LATENCY",
            "ORIGIN",
            "ORIGIN_AS",
            "ORIGIN_LOCATION",
            "ORIGIN_TARGET_LOCATION_PAIR",
            "OS",
            "PERCENTILE",
            "POST_QUANTUM",
            "PREFIX",
            "PRODUCT",
            "PROTOCOL",
            "PROVIDER",
            "PUBLIC_KEY_ALGORITHM",
            "QUERY_TYPE",
            "REFERER",
            "REGION",
            "RESPONSE_CODE",
            "RESPONSE_STATUS",
            "RESPONSE_STATUS_CATEGORY",
            "RESPONSE_TTL",
            "SIGNATURE_ALGORITHM",
            "SPAM",
            "SPF",
            "SPOOF",
            "SUCCESS_RATE",
            "TARGET_LOCATION",
            "TASK",
            "THREAT_CATEGORY",
            "TLD",
            "TLD_DNS_MAGNITUDE",
            "TLS_VERSION",
            "UPDATE_TYPE",
            "USER_AGENT",
            "VALIDATION_LEVEL",
            "VECTOR",
            "VERTICAL",
        ]
    ]
    """Filters results by annotation tag.

    Matches annotations carrying at least one of the given tags.
    """

    tld: str
    """Filters results by top-level domain."""
