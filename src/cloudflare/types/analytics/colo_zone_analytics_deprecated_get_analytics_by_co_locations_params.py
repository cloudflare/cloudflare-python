# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

__all__ = ["ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsParams"]


class ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsParams(TypedDict, total=False):
    continuous: bool
    """
    When set to true, the API will move the requested time window backward, until it
    finds a region with completely aggregated data.

    The API response _may not represent the requested time window_.
    """

    since: Union[str, int]
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

    until: Union[str, int]
    """The (exclusive) end of the requested time frame.

    This value can be a negative integer representing the number of minutes in the
    past relative to time the request is made, or can be an absolute timestamp that
    conforms to RFC 3339. If omitted, the time of the request is used.
    """
