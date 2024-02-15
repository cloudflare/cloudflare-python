# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional

from ..._models import BaseModel

__all__ = [
    "ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse",
    "ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItem",
    "ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimesery",
    "ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimeseryBandwidth",
    "ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimeseryRequests",
    "ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimeseryThreats",
    "ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotals",
    "ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotalsBandwidth",
    "ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotalsRequests",
    "ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotalsThreats",
]


class ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimeseryBandwidth(BaseModel):
    all: Optional[int] = None
    """The total number of bytes served within the time frame."""

    cached: Optional[int] = None
    """The number of bytes that were cached (and served) by Cloudflare."""

    uncached: Optional[int] = None
    """The number of bytes that were fetched and served from the origin server."""


class ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimeseryRequests(BaseModel):
    all: Optional[int] = None
    """Total number of requests served."""

    cached: Optional[int] = None
    """Total number of cached requests served."""

    country: Optional[Dict[str, object]] = None
    """
    Key/value pairs where the key is a two-digit country code and the value is the
    number of requests served to that country.
    """

    http_status: Optional[object] = None
    """
    A variable list of key/value pairs where the key is a HTTP status code and the
    value is the number of requests with that code served.
    """

    uncached: Optional[int] = None
    """Total number of requests served from the origin."""


class ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimeseryThreats(BaseModel):
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


class ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimesery(BaseModel):
    bandwidth: Optional[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimeseryBandwidth] = None
    """Breakdown of totals for bandwidth in the form of bytes."""

    requests: Optional[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimeseryRequests] = None
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

    threats: Optional[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimeseryThreats] = None
    """Breakdown of totals for threats."""

    until: Union[str, int, None] = None
    """The (exclusive) end of the requested time frame.

    This value can be a negative integer representing the number of minutes in the
    past relative to time the request is made, or can be an absolute timestamp that
    conforms to RFC 3339. If omitted, the time of the request is used.
    """


class ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotalsBandwidth(BaseModel):
    all: Optional[int] = None
    """The total number of bytes served within the time frame."""

    cached: Optional[int] = None
    """The number of bytes that were cached (and served) by Cloudflare."""

    uncached: Optional[int] = None
    """The number of bytes that were fetched and served from the origin server."""


class ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotalsRequests(BaseModel):
    all: Optional[int] = None
    """Total number of requests served."""

    cached: Optional[int] = None
    """Total number of cached requests served."""

    country: Optional[Dict[str, object]] = None
    """
    Key/value pairs where the key is a two-digit country code and the value is the
    number of requests served to that country.
    """

    http_status: Optional[object] = None
    """
    A variable list of key/value pairs where the key is a HTTP status code and the
    value is the number of requests with that code served.
    """

    uncached: Optional[int] = None
    """Total number of requests served from the origin."""


class ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotalsThreats(BaseModel):
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


class ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotals(BaseModel):
    bandwidth: Optional[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotalsBandwidth] = None
    """Breakdown of totals for bandwidth in the form of bytes."""

    requests: Optional[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotalsRequests] = None
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

    threats: Optional[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotalsThreats] = None
    """Breakdown of totals for threats."""

    until: Union[str, int, None] = None
    """The (exclusive) end of the requested time frame.

    This value can be a negative integer representing the number of minutes in the
    past relative to time the request is made, or can be an absolute timestamp that
    conforms to RFC 3339. If omitted, the time of the request is used.
    """


class ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItem(BaseModel):
    colo_id: Optional[str] = None
    """The airport code identifer for the co-location."""

    timeseries: Optional[List[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTimesery]] = None
    """Time deltas containing metadata about each bucket of time.

    The number of buckets (resolution) is determined by the amount of time between
    the since and until parameters.
    """

    totals: Optional[ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItemTotals] = None
    """Breakdown of totals by data type."""


ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse = List[
    ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponseItem
]
