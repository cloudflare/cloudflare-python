# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .schedule import Schedule
from ...._models import BaseModel
from .rule_setting import RuleSetting
from .gateway_filter import GatewayFilter

__all__ = ["GatewayRule", "Expiration"]


class Expiration(BaseModel):
    expires_at: datetime
    """The time stamp at which the policy will expire and cease to be applied.

    Must adhere to RFC 3339 and include a UTC offset. Non-zero offsets are accepted
    but will be converted to the equivalent value with offset zero (UTC+00:00) and
    will be returned as time stamps with offset zero denoted by a trailing 'Z'.

    Policies with an expiration do not consider the timezone of clients they are
    applied to, and expire "globally" at the point given by their `expires_at`
    value.
    """

    duration: Optional[int] = None
    """The default duration a policy will be active in minutes.

    Must be set in order to use the `reset_expiration` endpoint on this rule.
    """

    expired: Optional[bool] = None
    """Whether the policy has expired."""


class GatewayRule(BaseModel):
    id: Optional[str] = None
    """The API resource UUID."""

    action: Optional[
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
    ] = None
    """
    The action to preform when the associated traffic, identity, and device posture
    expressions are either absent or evaluate to `true`.
    """

    created_at: Optional[datetime] = None

    deleted_at: Optional[datetime] = None
    """Date of deletion, if any."""

    description: Optional[str] = None
    """The description of the rule."""

    device_posture: Optional[str] = None
    """The wirefilter expression used for device posture check matching."""

    enabled: Optional[bool] = None
    """True if the rule is enabled."""

    expiration: Optional[Expiration] = None
    """The expiration time stamp and default duration of a DNS policy.

    Takes precedence over the policy's `schedule` configuration, if any.

    This does not apply to HTTP or network policies.
    """

    filters: Optional[List[GatewayFilter]] = None
    """
    The protocol or layer to evaluate the traffic, identity, and device posture
    expressions.
    """

    identity: Optional[str] = None
    """The wirefilter expression used for identity matching."""

    name: Optional[str] = None
    """The name of the rule."""

    precedence: Optional[int] = None
    """Precedence sets the order of your rules.

    Lower values indicate higher precedence. At each processing phase, applicable
    rules are evaluated in ascending order of this value.
    """

    rule_settings: Optional[RuleSetting] = None
    """Additional settings that modify the rule's action."""

    schedule: Optional[Schedule] = None
    """The schedule for activating DNS policies.

    This does not apply to HTTP or network policies.
    """

    traffic: Optional[str] = None
    """The wirefilter expression used for traffic matching."""

    updated_at: Optional[datetime] = None

    version: Optional[int] = None
    """version number of the rule"""
