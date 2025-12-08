# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Schedule"]


class Schedule(BaseModel):
    """Defines the schedule for activating DNS policies.

    Settable only for `dns` and `dns_resolver` rules.
    """

    fri: Optional[str] = None
    """
    Specify the time intervals when the rule is active on Fridays, in the increasing
    order from 00:00-24:00. If this parameter omitted, the rule is deactivated on
    Fridays. API returns a formatted version of this string, which may cause
    Terraform drift if a unformatted value is used.
    """

    mon: Optional[str] = None
    """
    Specify the time intervals when the rule is active on Mondays, in the increasing
    order from 00:00-24:00(capped at maximum of 6 time splits). If this parameter
    omitted, the rule is deactivated on Mondays. API returns a formatted version of
    this string, which may cause Terraform drift if a unformatted value is used.
    """

    sat: Optional[str] = None
    """
    Specify the time intervals when the rule is active on Saturdays, in the
    increasing order from 00:00-24:00. If this parameter omitted, the rule is
    deactivated on Saturdays. API returns a formatted version of this string, which
    may cause Terraform drift if a unformatted value is used.
    """

    sun: Optional[str] = None
    """
    Specify the time intervals when the rule is active on Sundays, in the increasing
    order from 00:00-24:00. If this parameter omitted, the rule is deactivated on
    Sundays. API returns a formatted version of this string, which may cause
    Terraform drift if a unformatted value is used.
    """

    thu: Optional[str] = None
    """
    Specify the time intervals when the rule is active on Thursdays, in the
    increasing order from 00:00-24:00. If this parameter omitted, the rule is
    deactivated on Thursdays. API returns a formatted version of this string, which
    may cause Terraform drift if a unformatted value is used.
    """

    time_zone: Optional[str] = None
    """Specify the time zone for rule evaluation.

    When a
    [valid time zone city name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)
    is provided, Gateway always uses the current time for that time zone. When this
    parameter is omitted, Gateway uses the time zone determined from the user's IP
    address. Colo time zone is used when the user's IP address does not resolve to a
    location.
    """

    tue: Optional[str] = None
    """
    Specify the time intervals when the rule is active on Tuesdays, in the
    increasing order from 00:00-24:00. If this parameter omitted, the rule is
    deactivated on Tuesdays. API returns a formatted version of this string, which
    may cause Terraform drift if a unformatted value is used.
    """

    wed: Optional[str] = None
    """
    Specify the time intervals when the rule is active on Wednesdays, in the
    increasing order from 00:00-24:00. If this parameter omitted, the rule is
    deactivated on Wednesdays. API returns a formatted version of this string, which
    may cause Terraform drift if a unformatted value is used.
    """
