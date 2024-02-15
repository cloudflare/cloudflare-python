# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DashboardZoneAnalyticsDeprecatedGetDashboardResponse",
    "Timesery",
    "TimeseryBandwidth",
    "TimeseryBandwidthSSL",
    "TimeseryBandwidthSSLProtocols",
    "TimeseryPageviews",
    "TimeseryRequests",
    "TimeseryRequestsSSL",
    "TimeseryRequestsSSLProtocols",
    "TimeseryThreats",
    "TimeseryUniques",
    "Totals",
    "TotalsBandwidth",
    "TotalsBandwidthSSL",
    "TotalsBandwidthSSLProtocols",
    "TotalsPageviews",
    "TotalsRequests",
    "TotalsRequestsSSL",
    "TotalsRequestsSSLProtocols",
    "TotalsThreats",
    "TotalsUniques",
]


class TimeseryBandwidthSSL(BaseModel):
    encrypted: Optional[int] = None
    """The number of bytes served over HTTPS."""

    unencrypted: Optional[int] = None
    """The number of bytes served over HTTP."""


class TimeseryBandwidthSSLProtocols(BaseModel):
    none: Optional[int] = None
    """The number of requests served over HTTP."""

    tl_sv1: Optional[int] = FieldInfo(alias="TLSv1", default=None)
    """The number of requests served over TLS v1.0."""

    tl_sv1_1: Optional[int] = FieldInfo(alias="TLSv1.1", default=None)
    """The number of requests served over TLS v1.1."""

    tl_sv1_2: Optional[int] = FieldInfo(alias="TLSv1.2", default=None)
    """The number of requests served over TLS v1.2."""

    tl_sv1_3: Optional[int] = FieldInfo(alias="TLSv1.3", default=None)
    """The number of requests served over TLS v1.3."""


class TimeseryBandwidth(BaseModel):
    all: Optional[int] = None
    """The total number of bytes served within the time frame."""

    cached: Optional[int] = None
    """The number of bytes that were cached (and served) by Cloudflare."""

    content_type: Optional[object] = None
    """
    A variable list of key/value pairs where the key represents the type of content
    served, and the value is the number in bytes served.
    """

    country: Optional[object] = None
    """
    A variable list of key/value pairs where the key is a two-digit country code and
    the value is the number of bytes served to that country.
    """

    ssl: Optional[TimeseryBandwidthSSL] = None
    """A break down of bytes served over HTTPS."""

    ssl_protocols: Optional[TimeseryBandwidthSSLProtocols] = None
    """A breakdown of requests by their SSL protocol."""

    uncached: Optional[int] = None
    """The number of bytes that were fetched and served from the origin server."""


class TimeseryPageviews(BaseModel):
    all: Optional[int] = None
    """The total number of pageviews served within the time range."""

    search_engine: Optional[object] = None
    """
    A variable list of key/value pairs representing the search engine and number of
    hits.
    """


class TimeseryRequestsSSL(BaseModel):
    encrypted: Optional[int] = None
    """The number of requests served over HTTPS."""

    unencrypted: Optional[int] = None
    """The number of requests served over HTTP."""


class TimeseryRequestsSSLProtocols(BaseModel):
    none: Optional[int] = None
    """The number of requests served over HTTP."""

    tl_sv1: Optional[int] = FieldInfo(alias="TLSv1", default=None)
    """The number of requests served over TLS v1.0."""

    tl_sv1_1: Optional[int] = FieldInfo(alias="TLSv1.1", default=None)
    """The number of requests served over TLS v1.1."""

    tl_sv1_2: Optional[int] = FieldInfo(alias="TLSv1.2", default=None)
    """The number of requests served over TLS v1.2."""

    tl_sv1_3: Optional[int] = FieldInfo(alias="TLSv1.3", default=None)
    """The number of requests served over TLS v1.3."""


class TimeseryRequests(BaseModel):
    all: Optional[int] = None
    """Total number of requests served."""

    cached: Optional[int] = None
    """Total number of cached requests served."""

    content_type: Optional[object] = None
    """
    A variable list of key/value pairs where the key represents the type of content
    served, and the value is the number of requests.
    """

    country: Optional[object] = None
    """
    A variable list of key/value pairs where the key is a two-digit country code and
    the value is the number of requests served to that country.
    """

    http_status: Optional[Dict[str, object]] = None
    """
    Key/value pairs where the key is a HTTP status code and the value is the number
    of requests served with that code.
    """

    ssl: Optional[TimeseryRequestsSSL] = None
    """A break down of requests served over HTTPS."""

    ssl_protocols: Optional[TimeseryRequestsSSLProtocols] = None
    """A breakdown of requests by their SSL protocol."""

    uncached: Optional[int] = None
    """Total number of requests served from the origin."""


class TimeseryThreats(BaseModel):
    all: Optional[int] = None
    """The total number of identifiable threats received over the time frame."""

    country: Optional[object] = None
    """
    A list of key/value pairs where the key is a two-digit country code and the
    value is the number of malicious requests received from that country.
    """

    type: Optional[object] = None
    """
    The list of key/value pairs where the key is a threat category and the value is
    the number of requests.
    """


class TimeseryUniques(BaseModel):
    all: Optional[int] = None
    """Total number of unique IP addresses within the time range."""


class Timesery(BaseModel):
    bandwidth: Optional[TimeseryBandwidth] = None
    """Breakdown of totals for bandwidth in the form of bytes."""

    pageviews: Optional[TimeseryPageviews] = None
    """Breakdown of totals for pageviews."""

    requests: Optional[TimeseryRequests] = None
    """Breakdown of totals for requests."""

    since: Union[str, int, None] = None
    """The (inclusive) beginning of the requested time frame.

    This value can be a negative integer representing the number of minutes in the
    past relative to time the request is made, or can be an absolute timestamp that
    conforms to RFC 3339. At this point in time, it cannot exceed a time in the past
    greater than one year.

    Ranges that the Cloudflare web application provides will provide the following
    period length for each point:

    - Last 60 minutes (from -59 to -1): 1 minute resolution
    - Last 7 hours (from -419 to -60): 15 minutes resolution
    - Last 15 hours (from -899 to -420): 30 minutes resolution
    - Last 72 hours (from -4320 to -900): 1 hour resolution
    - Older than 3 days (-525600 to -4320): 1 day resolution.
    """

    threats: Optional[TimeseryThreats] = None
    """Breakdown of totals for threats."""

    uniques: Optional[TimeseryUniques] = None

    until: Union[str, int, None] = None
    """The (exclusive) end of the requested time frame.

    This value can be a negative integer representing the number of minutes in the
    past relative to time the request is made, or can be an absolute timestamp that
    conforms to RFC 3339. If omitted, the time of the request is used.
    """


class TotalsBandwidthSSL(BaseModel):
    encrypted: Optional[int] = None
    """The number of bytes served over HTTPS."""

    unencrypted: Optional[int] = None
    """The number of bytes served over HTTP."""


class TotalsBandwidthSSLProtocols(BaseModel):
    none: Optional[int] = None
    """The number of requests served over HTTP."""

    tl_sv1: Optional[int] = FieldInfo(alias="TLSv1", default=None)
    """The number of requests served over TLS v1.0."""

    tl_sv1_1: Optional[int] = FieldInfo(alias="TLSv1.1", default=None)
    """The number of requests served over TLS v1.1."""

    tl_sv1_2: Optional[int] = FieldInfo(alias="TLSv1.2", default=None)
    """The number of requests served over TLS v1.2."""

    tl_sv1_3: Optional[int] = FieldInfo(alias="TLSv1.3", default=None)
    """The number of requests served over TLS v1.3."""


class TotalsBandwidth(BaseModel):
    all: Optional[int] = None
    """The total number of bytes served within the time frame."""

    cached: Optional[int] = None
    """The number of bytes that were cached (and served) by Cloudflare."""

    content_type: Optional[object] = None
    """
    A variable list of key/value pairs where the key represents the type of content
    served, and the value is the number in bytes served.
    """

    country: Optional[object] = None
    """
    A variable list of key/value pairs where the key is a two-digit country code and
    the value is the number of bytes served to that country.
    """

    ssl: Optional[TotalsBandwidthSSL] = None
    """A break down of bytes served over HTTPS."""

    ssl_protocols: Optional[TotalsBandwidthSSLProtocols] = None
    """A breakdown of requests by their SSL protocol."""

    uncached: Optional[int] = None
    """The number of bytes that were fetched and served from the origin server."""


class TotalsPageviews(BaseModel):
    all: Optional[int] = None
    """The total number of pageviews served within the time range."""

    search_engine: Optional[object] = None
    """
    A variable list of key/value pairs representing the search engine and number of
    hits.
    """


class TotalsRequestsSSL(BaseModel):
    encrypted: Optional[int] = None
    """The number of requests served over HTTPS."""

    unencrypted: Optional[int] = None
    """The number of requests served over HTTP."""


class TotalsRequestsSSLProtocols(BaseModel):
    none: Optional[int] = None
    """The number of requests served over HTTP."""

    tl_sv1: Optional[int] = FieldInfo(alias="TLSv1", default=None)
    """The number of requests served over TLS v1.0."""

    tl_sv1_1: Optional[int] = FieldInfo(alias="TLSv1.1", default=None)
    """The number of requests served over TLS v1.1."""

    tl_sv1_2: Optional[int] = FieldInfo(alias="TLSv1.2", default=None)
    """The number of requests served over TLS v1.2."""

    tl_sv1_3: Optional[int] = FieldInfo(alias="TLSv1.3", default=None)
    """The number of requests served over TLS v1.3."""


class TotalsRequests(BaseModel):
    all: Optional[int] = None
    """Total number of requests served."""

    cached: Optional[int] = None
    """Total number of cached requests served."""

    content_type: Optional[object] = None
    """
    A variable list of key/value pairs where the key represents the type of content
    served, and the value is the number of requests.
    """

    country: Optional[object] = None
    """
    A variable list of key/value pairs where the key is a two-digit country code and
    the value is the number of requests served to that country.
    """

    http_status: Optional[Dict[str, object]] = None
    """
    Key/value pairs where the key is a HTTP status code and the value is the number
    of requests served with that code.
    """

    ssl: Optional[TotalsRequestsSSL] = None
    """A break down of requests served over HTTPS."""

    ssl_protocols: Optional[TotalsRequestsSSLProtocols] = None
    """A breakdown of requests by their SSL protocol."""

    uncached: Optional[int] = None
    """Total number of requests served from the origin."""


class TotalsThreats(BaseModel):
    all: Optional[int] = None
    """The total number of identifiable threats received over the time frame."""

    country: Optional[object] = None
    """
    A list of key/value pairs where the key is a two-digit country code and the
    value is the number of malicious requests received from that country.
    """

    type: Optional[object] = None
    """
    The list of key/value pairs where the key is a threat category and the value is
    the number of requests.
    """


class TotalsUniques(BaseModel):
    all: Optional[int] = None
    """Total number of unique IP addresses within the time range."""


class Totals(BaseModel):
    bandwidth: Optional[TotalsBandwidth] = None
    """Breakdown of totals for bandwidth in the form of bytes."""

    pageviews: Optional[TotalsPageviews] = None
    """Breakdown of totals for pageviews."""

    requests: Optional[TotalsRequests] = None
    """Breakdown of totals for requests."""

    since: Union[str, int, None] = None
    """The (inclusive) beginning of the requested time frame.

    This value can be a negative integer representing the number of minutes in the
    past relative to time the request is made, or can be an absolute timestamp that
    conforms to RFC 3339. At this point in time, it cannot exceed a time in the past
    greater than one year.

    Ranges that the Cloudflare web application provides will provide the following
    period length for each point:

    - Last 60 minutes (from -59 to -1): 1 minute resolution
    - Last 7 hours (from -419 to -60): 15 minutes resolution
    - Last 15 hours (from -899 to -420): 30 minutes resolution
    - Last 72 hours (from -4320 to -900): 1 hour resolution
    - Older than 3 days (-525600 to -4320): 1 day resolution.
    """

    threats: Optional[TotalsThreats] = None
    """Breakdown of totals for threats."""

    uniques: Optional[TotalsUniques] = None

    until: Union[str, int, None] = None
    """The (exclusive) end of the requested time frame.

    This value can be a negative integer representing the number of minutes in the
    past relative to time the request is made, or can be an absolute timestamp that
    conforms to RFC 3339. If omitted, the time of the request is used.
    """


class DashboardZoneAnalyticsDeprecatedGetDashboardResponse(BaseModel):
    timeseries: Optional[List[Timesery]] = None
    """Time deltas containing metadata about each bucket of time.

    The number of buckets (resolution) is determined by the amount of time between
    the since and until parameters.
    """

    totals: Optional[Totals] = None
    """Breakdown of totals by data type."""
