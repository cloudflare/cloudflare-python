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
    """Show the timestamp when the policy expires and stops applying.

    The value must follow RFC 3339 and include a UTC offset. The system accepts
    non-zero offsets but converts them to the equivalent UTC+00:00 value and returns
    timestamps with a trailing Z. Expiration policies ignore client timezones and
    expire globally at the specified expires_at time.
    """

    duration: Optional[int] = None
    """Defines the default duration a policy active in minutes.

    Must set in order to use the `reset_expiration` endpoint on this rule.
    """

    expired: Optional[bool] = None
    """Indicates whether the policy is expired."""


class GatewayRule(BaseModel):
    action: Literal[
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
    """
    Specify the action to perform when the associated traffic, identity, and device
    posture expressions either absent or evaluate to `true`.
    """

    enabled: bool
    """Specify whether the rule is enabled."""

    filters: List[GatewayFilter]
    """
    Specify the protocol or layer to evaluate the traffic, identity, and device
    posture expressions. Can only contain a single value.
    """

    name: str
    """Specify the rule name."""

    precedence: int
    """Set the order of your rules.

    Lower values indicate higher precedence. At each processing phase, evaluate
    applicable rules in ascending order of this value. Refer to
    [Order of enforcement](http://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/#manage-precedence-with-terraform)
    to manage precedence via Terraform.
    """

    traffic: str
    """Specify the wirefilter expression used for traffic matching.

    The API automatically formats and sanitizes expressions before storing them. To
    prevent Terraform state drift, use the formatted expression returned in the API
    response.
    """

    id: Optional[str] = None
    """Identify the API resource with a UUID."""

    created_at: Optional[datetime] = None

    deleted_at: Optional[datetime] = None
    """Indicate the date of deletion, if any."""

    description: Optional[str] = None
    """Specify the rule description."""

    device_posture: Optional[str] = None
    """Specify the wirefilter expression used for device posture check.

    The API automatically formats and sanitizes expressions before storing them. To
    prevent Terraform state drift, use the formatted expression returned in the API
    response.
    """

    expiration: Optional[Expiration] = None
    """Defines the expiration time stamp and default duration of a DNS policy.

    Takes precedence over the policy's `schedule` configuration, if any. This does
    not apply to HTTP or network policies. Settable only for `dns` rules.
    """

    identity: Optional[str] = None
    """Specify the wirefilter expression used for identity matching.

    The API automatically formats and sanitizes expressions before storing them. To
    prevent Terraform state drift, use the formatted expression returned in the API
    response.
    """

    read_only: Optional[bool] = None
    """Indicate that this rule is shared via the Orgs API and read only."""

    rule_settings: Optional[RuleSetting] = None
    """Defines settings for this rule.

    Settings apply only to specific rule types and must use compatible selectors. If
    Terraform detects drift, confirm the setting supports your rule type and check
    whether the API modifies the value. Use API-returned values in your
    configuration to prevent drift.
    """

    schedule: Optional[Schedule] = None
    """Defines the schedule for activating DNS policies.

    Settable only for `dns` and `dns_resolver` rules.
    """

    sharable: Optional[bool] = None
    """Indicate that this rule is sharable via the Orgs API."""

    source_account: Optional[str] = None
    """Provide the account tag of the account that created the rule."""

    updated_at: Optional[datetime] = None

    version: Optional[int] = None
    """Indicate the version number of the rule(read-only)."""

    warning_status: Optional[str] = None
    """Indicate a warning for a misconfigured rule, if any."""
