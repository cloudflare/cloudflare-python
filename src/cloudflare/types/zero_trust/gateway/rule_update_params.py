# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "RuleUpdateParams",
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

    filters: List[Literal["http", "dns", "l4", "egress"]]
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

    rule_settings: RuleSettings
    """Additional settings that modify the rule's action."""

    schedule: Schedule
    """The schedule for activating DNS policies.

    This does not apply to HTTP or network policies.
    """

    traffic: str
    """The wirefilter expression used for traffic matching."""


class RuleSettingsAuditSSH(TypedDict, total=False):
    command_logging: bool
    """Enable to turn on SSH command logging."""


class RuleSettingsBisoAdminControls(TypedDict, total=False):
    dcp: bool
    """Set to true to enable copy-pasting."""

    dd: bool
    """Set to true to enable downloading."""

    dk: bool
    """Set to true to enable keyboard usage."""

    dp: bool
    """Set to true to enable printing."""

    du: bool
    """Set to true to enable uploading."""


class RuleSettingsCheckSession(TypedDict, total=False):
    duration: str
    """Configure how fresh the session needs to be to be considered valid."""

    enforce: bool
    """Set to true to enable session enforcement."""


class RuleSettingsDNSResolversIPV4(TypedDict, total=False):
    ip: Required[str]
    """IP address of upstream resolver."""

    port: int
    """A port number to use for upstream resolver."""

    route_through_private_network: bool
    """Whether to connect to this resolver over a private network.

    Must be set when vnet_id is set.
    """

    vnet_id: str
    """Optionally specify a virtual network for this resolver.

    Uses default virtual network id if omitted.
    """


class RuleSettingsDNSResolversIPV6(TypedDict, total=False):
    ip: Required[str]
    """IP address of upstream resolver."""

    port: int
    """A port number to use for upstream resolver."""

    route_through_private_network: bool
    """Whether to connect to this resolver over a private network.

    Must be set when vnet_id is set.
    """

    vnet_id: str
    """Optionally specify a virtual network for this resolver.

    Uses default virtual network id if omitted.
    """


class RuleSettingsDNSResolvers(TypedDict, total=False):
    ipv4: Iterable[RuleSettingsDNSResolversIPV4]

    ipv6: Iterable[RuleSettingsDNSResolversIPV6]


class RuleSettingsEgress(TypedDict, total=False):
    ipv4: str
    """The IPv4 address to be used for egress."""

    ipv4_fallback: str
    """
    The fallback IPv4 address to be used for egress in the event of an error
    egressing with the primary IPv4. Can be '0.0.0.0' to indicate local egress via
    WARP IPs.
    """

    ipv6: str
    """The IPv6 range to be used for egress."""


class RuleSettingsL4override(TypedDict, total=False):
    ip: str
    """IPv4 or IPv6 address."""

    port: int
    """A port number to use for TCP/UDP overrides."""


class RuleSettingsNotificationSettings(TypedDict, total=False):
    enabled: bool
    """Set notification on"""

    msg: str
    """Customize the message shown in the notification."""

    support_url: str
    """Optional URL to direct users to additional information.

    If not set, the notification will open a block page.
    """


class RuleSettingsPayloadLog(TypedDict, total=False):
    enabled: bool
    """Set to true to enable DLP payload logging for this rule."""


class RuleSettingsUntrustedCERT(TypedDict, total=False):
    action: Literal["pass_through", "block", "error"]
    """The action performed when an untrusted certificate is seen.

    The default action is an error with HTTP code 526.
    """


class RuleSettings(TypedDict, total=False):
    add_headers: object
    """Add custom headers to allowed requests, in the form of key-value pairs.

    Keys are header names, pointing to an array with its header value(s).
    """

    allow_child_bypass: bool
    """Set by parent MSP accounts to enable their children to bypass this rule."""

    audit_ssh: RuleSettingsAuditSSH
    """Settings for the Audit SSH action."""

    biso_admin_controls: RuleSettingsBisoAdminControls
    """Configure how browser isolation behaves."""

    block_page_enabled: bool
    """Enable the custom block page."""

    block_reason: str
    """
    The text describing why this block occurred, displayed on the custom block page
    (if enabled).
    """

    bypass_parent_rule: bool
    """Set by children MSP accounts to bypass their parent's rules."""

    check_session: RuleSettingsCheckSession
    """Configure how session check behaves."""

    dns_resolvers: RuleSettingsDNSResolvers
    """Add your own custom resolvers to route queries that match the resolver policy.

    Cannot be used when resolve_dns_through_cloudflare is set. DNS queries will
    route to the address closest to their origin.
    """

    egress: RuleSettingsEgress
    """Configure how Gateway Proxy traffic egresses.

    You can enable this setting for rules with Egress actions and filters, or omit
    it to indicate local egress via WARP IPs.
    """

    insecure_disable_dnssec_validation: bool
    """INSECURE - disable DNSSEC validation (for Allow actions)."""

    ip_categories: bool
    """Set to true to enable IPs in DNS resolver category blocks.

    By default categories only block based on domain names.
    """

    ip_indicator_feeds: bool
    """Set to true to include IPs in DNS resolver indicator feed blocks.

    By default indicator feeds only block based on domain names.
    """

    l4override: RuleSettingsL4override
    """Send matching traffic to the supplied destination IP address and port."""

    notification_settings: RuleSettingsNotificationSettings
    """
    Configure a notification to display on the user's device when this rule is
    matched.
    """

    override_host: str
    """Override matching DNS queries with a hostname."""

    override_ips: List[str]
    """Override matching DNS queries with an IP or set of IPs."""

    payload_log: RuleSettingsPayloadLog
    """Configure DLP payload logging."""

    resolve_dns_through_cloudflare: bool
    """
    Enable to send queries that match the policy to Cloudflare's default 1.1.1.1 DNS
    resolver. Cannot be set when dns_resolvers are specified.
    """

    untrusted_cert: RuleSettingsUntrustedCERT
    """Configure behavior when an upstream cert is invalid or an SSL error occurs."""


class Schedule(TypedDict, total=False):
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
