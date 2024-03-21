# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "ZeroTrustGatewayRules",
    "RuleSettings",
    "RuleSettingsAuditSSH",
    "RuleSettingsBisoAdminControls",
    "RuleSettingsCheckSession",
    "RuleSettingsDNSResolvers",
    "RuleSettingsDNSResolversIPV4",
    "RuleSettingsDNSResolversIPV6",
    "RuleSettingsEgress",
    "RuleSettingsL4override",
    "RuleSettingsNotificationSettings",
    "RuleSettingsPayloadLog",
    "RuleSettingsUntrustedCERT",
    "Schedule",
]


class RuleSettingsAuditSSH(BaseModel):
    command_logging: Optional[bool] = None
    """Enable to turn on SSH command logging."""


class RuleSettingsBisoAdminControls(BaseModel):
    dcp: Optional[bool] = None
    """Set to true to enable copy-pasting."""

    dd: Optional[bool] = None
    """Set to true to enable downloading."""

    dk: Optional[bool] = None
    """Set to true to enable keyboard usage."""

    dp: Optional[bool] = None
    """Set to true to enable printing."""

    du: Optional[bool] = None
    """Set to true to enable uploading."""


class RuleSettingsCheckSession(BaseModel):
    duration: Optional[str] = None
    """Configure how fresh the session needs to be to be considered valid."""

    enforce: Optional[bool] = None
    """Set to true to enable session enforcement."""


class RuleSettingsDNSResolversIPV4(BaseModel):
    ip: str
    """IP address of upstream resolver."""

    port: Optional[int] = None
    """A port number to use for upstream resolver."""

    route_through_private_network: Optional[bool] = None
    """Whether to connect to this resolver over a private network.

    Must be set when vnet_id is set.
    """

    vnet_id: Optional[str] = None
    """Optionally specify a virtual network for this resolver.

    Uses default virtual network id if omitted.
    """


class RuleSettingsDNSResolversIPV6(BaseModel):
    ip: str
    """IP address of upstream resolver."""

    port: Optional[int] = None
    """A port number to use for upstream resolver."""

    route_through_private_network: Optional[bool] = None
    """Whether to connect to this resolver over a private network.

    Must be set when vnet_id is set.
    """

    vnet_id: Optional[str] = None
    """Optionally specify a virtual network for this resolver.

    Uses default virtual network id if omitted.
    """


class RuleSettingsDNSResolvers(BaseModel):
    ipv4: Optional[List[RuleSettingsDNSResolversIPV4]] = None

    ipv6: Optional[List[RuleSettingsDNSResolversIPV6]] = None


class RuleSettingsEgress(BaseModel):
    ipv4: Optional[str] = None
    """The IPv4 address to be used for egress."""

    ipv4_fallback: Optional[str] = None
    """
    The fallback IPv4 address to be used for egress in the event of an error
    egressing with the primary IPv4. Can be '0.0.0.0' to indicate local egress via
    WARP IPs.
    """

    ipv6: Optional[str] = None
    """The IPv6 range to be used for egress."""


class RuleSettingsL4override(BaseModel):
    ip: Optional[str] = None
    """IPv4 or IPv6 address."""

    port: Optional[int] = None
    """A port number to use for TCP/UDP overrides."""


class RuleSettingsNotificationSettings(BaseModel):
    enabled: Optional[bool] = None
    """Set notification on"""

    msg: Optional[str] = None
    """Customize the message shown in the notification."""

    support_url: Optional[str] = None
    """Optional URL to direct users to additional information.

    If not set, the notification will open a block page.
    """


class RuleSettingsPayloadLog(BaseModel):
    enabled: Optional[bool] = None
    """Set to true to enable DLP payload logging for this rule."""


class RuleSettingsUntrustedCERT(BaseModel):
    action: Optional[Literal["pass_through", "block", "error"]] = None
    """The action performed when an untrusted certificate is seen.

    The default action is an error with HTTP code 526.
    """


class RuleSettings(BaseModel):
    add_headers: Optional[object] = None
    """Add custom headers to allowed requests, in the form of key-value pairs.

    Keys are header names, pointing to an array with its header value(s).
    """

    allow_child_bypass: Optional[bool] = None
    """Set by parent MSP accounts to enable their children to bypass this rule."""

    audit_ssh: Optional[RuleSettingsAuditSSH] = None
    """Settings for the Audit SSH action."""

    biso_admin_controls: Optional[RuleSettingsBisoAdminControls] = None
    """Configure how browser isolation behaves."""

    block_page_enabled: Optional[bool] = None
    """Enable the custom block page."""

    block_reason: Optional[str] = None
    """
    The text describing why this block occurred, displayed on the custom block page
    (if enabled).
    """

    bypass_parent_rule: Optional[bool] = None
    """Set by children MSP accounts to bypass their parent's rules."""

    check_session: Optional[RuleSettingsCheckSession] = None
    """Configure how session check behaves."""

    dns_resolvers: Optional[RuleSettingsDNSResolvers] = None
    """Add your own custom resolvers to route queries that match the resolver policy.

    Cannot be used when resolve_dns_through_cloudflare is set. DNS queries will
    route to the address closest to their origin.
    """

    egress: Optional[RuleSettingsEgress] = None
    """Configure how Gateway Proxy traffic egresses.

    You can enable this setting for rules with Egress actions and filters, or omit
    it to indicate local egress via WARP IPs.
    """

    insecure_disable_dnssec_validation: Optional[bool] = None
    """INSECURE - disable DNSSEC validation (for Allow actions)."""

    ip_categories: Optional[bool] = None
    """Set to true to enable IPs in DNS resolver category blocks.

    By default categories only block based on domain names.
    """

    ip_indicator_feeds: Optional[bool] = None
    """Set to true to include IPs in DNS resolver indicator feed blocks.

    By default indicator feeds only block based on domain names.
    """

    l4override: Optional[RuleSettingsL4override] = None
    """Send matching traffic to the supplied destination IP address and port."""

    notification_settings: Optional[RuleSettingsNotificationSettings] = None
    """
    Configure a notification to display on the user's device when this rule is
    matched.
    """

    override_host: Optional[str] = None
    """Override matching DNS queries with a hostname."""

    override_ips: Optional[List[str]] = None
    """Override matching DNS queries with an IP or set of IPs."""

    payload_log: Optional[RuleSettingsPayloadLog] = None
    """Configure DLP payload logging."""

    resolve_dns_through_cloudflare: Optional[bool] = None
    """
    Enable to send queries that match the policy to Cloudflare's default 1.1.1.1 DNS
    resolver. Cannot be set when dns_resolvers are specified.
    """

    untrusted_cert: Optional[RuleSettingsUntrustedCERT] = None
    """Configure behavior when an upstream cert is invalid or an SSL error occurs."""


class Schedule(BaseModel):
    fri: Optional[str] = None
    """
    The time intervals when the rule will be active on Fridays, in increasing order
    from 00:00-24:00. If this parameter is omitted, the rule will be deactivated on
    Fridays.
    """

    mon: Optional[str] = None
    """
    The time intervals when the rule will be active on Mondays, in increasing order
    from 00:00-24:00. If this parameter is omitted, the rule will be deactivated on
    Mondays.
    """

    sat: Optional[str] = None
    """
    The time intervals when the rule will be active on Saturdays, in increasing
    order from 00:00-24:00. If this parameter is omitted, the rule will be
    deactivated on Saturdays.
    """

    sun: Optional[str] = None
    """
    The time intervals when the rule will be active on Sundays, in increasing order
    from 00:00-24:00. If this parameter is omitted, the rule will be deactivated on
    Sundays.
    """

    thu: Optional[str] = None
    """
    The time intervals when the rule will be active on Thursdays, in increasing
    order from 00:00-24:00. If this parameter is omitted, the rule will be
    deactivated on Thursdays.
    """

    time_zone: Optional[str] = None
    """The time zone the rule will be evaluated against.

    If a
    [valid time zone city name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)
    is provided, Gateway will always use the current time at that time zone. If this
    parameter is omitted, then Gateway will use the time zone inferred from the
    user's source IP to evaluate the rule. If Gateway cannot determine the time zone
    from the IP, we will fall back to the time zone of the user's connected data
    center.
    """

    tue: Optional[str] = None
    """
    The time intervals when the rule will be active on Tuesdays, in increasing order
    from 00:00-24:00. If this parameter is omitted, the rule will be deactivated on
    Tuesdays.
    """

    wed: Optional[str] = None
    """
    The time intervals when the rule will be active on Wednesdays, in increasing
    order from 00:00-24:00. If this parameter is omitted, the rule will be
    deactivated on Wednesdays.
    """


class ZeroTrustGatewayRules(BaseModel):
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
            "audit_ssh",
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

    filters: Optional[List[Literal["http", "dns", "l4", "egress"]]] = None
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

    rule_settings: Optional[RuleSettings] = None
    """Additional settings that modify the rule's action."""

    schedule: Optional[Schedule] = None
    """The schedule for activating DNS policies.

    This does not apply to HTTP or network policies.
    """

    traffic: Optional[str] = None
    """The wirefilter expression used for traffic matching."""

    updated_at: Optional[datetime] = None
