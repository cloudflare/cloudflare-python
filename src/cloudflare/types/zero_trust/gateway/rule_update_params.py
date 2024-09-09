# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .gateway_filter import GatewayFilter
from .schedule_param import ScheduleParam
from .rule_setting_param import RuleSettingParam

__all__ = ["RuleUpdateParams"]


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
            "audit_ssh",
            "resolve",
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
