# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from ..dimension import Dimension

__all__ = ["BytimeGetParams"]


class BytimeGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    time_delta: Required[Literal["year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"]]
    """Used to select time series resolution."""

    dimensions: List[Dimension]
    """Can be used to break down the data by given attributes. Options are:

    | Dimension | Name                          | Example                                                    |
    | --------- | ----------------------------- | ---------------------------------------------------------- |
    | event     | Connection Event              | connect, progress, disconnect, originError, clientFiltered |
    | appID     | Application ID                | 40d67c87c6cd4b889a4fd57805225e85                           |
    | coloName  | Colo Name                     | SFO                                                        |
    | ipVersion | IP version used by the client | 4, 6.                                                      |
    """

    filters: str
    """Used to filter rows by one or more dimensions.

    Filters can be combined using OR and AND boolean logic. AND takes precedence
    over OR in all the expressions. The OR operator is defined using a comma (,) or
    OR keyword surrounded by whitespace. The AND operator is defined using a
    semicolon (;) or AND keyword surrounded by whitespace. Note that the semicolon
    is a reserved character in URLs (rfc1738) and needs to be percent-encoded as
    %3B. Comparison options are:

    | Operator | Name                     | URL Encoded |
    | -------- | ------------------------ | ----------- |
    | ==       | Equals                   | %3D%3D      |
    | !=       | Does not equals          | !%3D        |
    | \\>>       | Greater Than             | %3E         |
    | \\<<       | Less Than                | %3C         |
    | \\>>=      | Greater than or equal to | %3E%3D      |
    | \\<<=      | Less than or equal to    | %3C%3D      |
    """

    metrics: List[
        Literal["count", "bytesIngress", "bytesEgress", "durationAvg", "durationMedian", "duration90th", "duration99th"]
    ]
    """One or more metrics to compute. Options are:

    | Metric         | Name                                | Example | Unit                  |
    | -------------- | ----------------------------------- | ------- | --------------------- |
    | count          | Count of total events               | 1000    | Count                 |
    | bytesIngress   | Sum of ingress bytes                | 1000    | Sum                   |
    | bytesEgress    | Sum of egress bytes                 | 1000    | Sum                   |
    | durationAvg    | Average connection duration         | 1.0     | Time in milliseconds  |
    | durationMedian | Median connection duration          | 1.0     | Time in milliseconds  |
    | duration90th   | 90th percentile connection duration | 1.0     | Time in milliseconds  |
    | duration99th   | 99th percentile connection duration | 1.0     | Time in milliseconds. |
    """

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of time interval to query, defaults to `until` - 6 hours.

    Timestamp must be in RFC3339 format and uses UTC unless otherwise specified.
    """

    sort: List[str]
    """
    The sort order for the result set; sort fields must be included in `metrics` or
    `dimensions`.
    """

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of time interval to query, defaults to current time.

    Timestamp must be in RFC3339 format and uses UTC unless otherwise specified.
    """
