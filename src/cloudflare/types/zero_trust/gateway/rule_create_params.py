# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .gateway_filter import GatewayFilter
from .schedule_param import ScheduleParam
from .rule_setting_param import RuleSettingParam

__all__ = ["RuleCreateParams", "Expiration"]


class RuleCreateParams(TypedDict, total=False):
    account_id: Required[str]

    action: Required[
        Literal[
            "on",
            "off",
            "allow",
            "block",
            "scan",
            "noscan",
            "safesearch",
            "ytrestricted",
            "isolate",
            "noisolate",
            "override",
            "l4_override",
            "egress",
            "resolve",
            "quarantine",
        ]
    ]
    """
    The action to preform when the associated traffic, identity, and device posture
    expressions are either absent or evaluate to `true`.
    """

    name: Required[str]
    """The name of the rule."""

    description: str
    """The description of the rule."""

    device_posture: str
    """The wirefilter expression used for device posture check matching."""

    enabled: bool
    """True if the rule is enabled."""

    expiration: Expiration
    """The expiration time stamp and default duration of a DNS policy.

    Takes precedence over the policy's `schedule` configuration, if any.

    This does not apply to HTTP or network policies.
    """

    filters: List[GatewayFilter]
    """
    The protocol or layer to evaluate the traffic, identity, and device posture
    expressions.
    """

    identity: str
    """The wirefilter expression used for identity matching."""

    precedence: int
    """Precedence sets the order of your rules.

    Lower values indicate higher precedence. At each processing phase, applicable
    rules are evaluated in ascending order of this value.
    """

    rule_settings: RuleSettingParam
    """Additional settings that modify the rule's action."""

    schedule: ScheduleParam
    """The schedule for activating DNS policies.

    This does not apply to HTTP or network policies.
    """

    traffic: str
    """The wirefilter expression used for traffic matching."""


class Expiration(TypedDict, total=False):
    expires_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The time stamp at which the policy will expire and cease to be applied.

    Must adhere to RFC 3339 and include a UTC offset. Non-zero offsets are accepted
    but will be converted to the equivalent value with offset zero (UTC+00:00) and
    will be returned as time stamps with offset zero denoted by a trailing 'Z'.

    Policies with an expiration do not consider the timezone of clients they are
    applied to, and expire "globally" at the point given by their `expires_at`
    value.
    """

    duration: int
    """The default duration a policy will be active in minutes.

    Must be set in order to use the `reset_expiration` endpoint on this rule.
    """

    expired: bool
    """Whether the policy has expired."""
