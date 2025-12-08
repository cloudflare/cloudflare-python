# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .gateway_filter import GatewayFilter
from .schedule_param import ScheduleParam
from .rule_setting_param import RuleSettingParam

__all__ = ["RuleUpdateParams", "Expiration"]


class RuleUpdateParams(TypedDict, total=False):
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
            "redirect",
        ]
    ]
    """
    Specify the action to perform when the associated traffic, identity, and device
    posture expressions either absent or evaluate to `true`.
    """

    name: Required[str]
    """Specify the rule name."""

    description: str
    """Specify the rule description."""

    device_posture: str
    """Specify the wirefilter expression used for device posture check.

    The API automatically formats and sanitizes expressions before storing them. To
    prevent Terraform state drift, use the formatted expression returned in the API
    response.
    """

    enabled: bool
    """Specify whether the rule is enabled."""

    expiration: Optional[Expiration]
    """Defines the expiration time stamp and default duration of a DNS policy.

    Takes precedence over the policy's `schedule` configuration, if any. This does
    not apply to HTTP or network policies. Settable only for `dns` rules.
    """

    filters: List[GatewayFilter]
    """
    Specify the protocol or layer to evaluate the traffic, identity, and device
    posture expressions. Can only contain a single value.
    """

    identity: str
    """Specify the wirefilter expression used for identity matching.

    The API automatically formats and sanitizes expressions before storing them. To
    prevent Terraform state drift, use the formatted expression returned in the API
    response.
    """

    precedence: int
    """Set the order of your rules.

    Lower values indicate higher precedence. At each processing phase, evaluate
    applicable rules in ascending order of this value. Refer to
    [Order of enforcement](http://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/#manage-precedence-with-terraform)
    to manage precedence via Terraform.
    """

    rule_settings: RuleSettingParam
    """Defines settings for this rule.

    Settings apply only to specific rule types and must use compatible selectors. If
    Terraform detects drift, confirm the setting supports your rule type and check
    whether the API modifies the value. Use API-returned values in your
    configuration to prevent drift.
    """

    schedule: Optional[ScheduleParam]
    """Defines the schedule for activating DNS policies.

    Settable only for `dns` and `dns_resolver` rules.
    """

    traffic: str
    """Specify the wirefilter expression used for traffic matching.

    The API automatically formats and sanitizes expressions before storing them. To
    prevent Terraform state drift, use the formatted expression returned in the API
    response.
    """


class Expiration(TypedDict, total=False):
    """Defines the expiration time stamp and default duration of a DNS policy.

    Takes precedence over the policy's `schedule` configuration, if any. This  does not apply to HTTP or network policies. Settable only for `dns` rules.
    """

    expires_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Show the timestamp when the policy expires and stops applying.

    The value must follow RFC 3339 and include a UTC offset. The system accepts
    non-zero offsets but converts them to the equivalent UTC+00:00 value and returns
    timestamps with a trailing Z. Expiration policies ignore client timezones and
    expire globally at the specified expires_at time.
    """

    duration: int
    """Defines the default duration a policy active in minutes.

    Must set in order to use the `reset_expiration` endpoint on this rule.
    """
