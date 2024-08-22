# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScheduleParam"]


class ScheduleParam(TypedDict, total=False):
    fri: str
    """
    The time intervals when the rule will be active on Fridays, in increasing order
    from 00:00-24:00. If this parameter is omitted, the rule will be deactivated on
    Fridays.
    """

    mon: str
    """
    The time intervals when the rule will be active on Mondays, in increasing order
    from 00:00-24:00. If this parameter is omitted, the rule will be deactivated on
    Mondays.
    """

    sat: str
    """
    The time intervals when the rule will be active on Saturdays, in increasing
    order from 00:00-24:00. If this parameter is omitted, the rule will be
    deactivated on Saturdays.
    """

    sun: str
    """
    The time intervals when the rule will be active on Sundays, in increasing order
    from 00:00-24:00. If this parameter is omitted, the rule will be deactivated on
    Sundays.
    """

    thu: str
    """
    The time intervals when the rule will be active on Thursdays, in increasing
    order from 00:00-24:00. If this parameter is omitted, the rule will be
    deactivated on Thursdays.
    """

    time_zone: str
    """The time zone the rule will be evaluated against.

    If a
    [valid time zone city name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)
    is provided, Gateway will always use the current time at that time zone. If this
    parameter is omitted, then Gateway will use the time zone inferred from the
    user's source IP to evaluate the rule. If Gateway cannot determine the time zone
    from the IP, we will fall back to the time zone of the user's connected data
    center.
    """

    tue: str
    """
    The time intervals when the rule will be active on Tuesdays, in increasing order
    from 00:00-24:00. If this parameter is omitted, the rule will be deactivated on
    Tuesdays.
    """

    wed: str
    """
    The time intervals when the rule will be active on Wednesdays, in increasing
    order from 00:00-24:00. If this parameter is omitted, the rule will be
    deactivated on Wednesdays.
    """
