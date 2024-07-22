# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

from .dns_resolver_settings_v4_param import DNSResolverSettingsV4Param
from .dns_resolver_settings_v6_param import DNSResolverSettingsV6Param

__all__ = [
    "RuleSettingParam",
    "AuditSSH",
    "BISOAdminControls",
    "CheckSession",
    "DNSResolvers",
    "Egress",
    "L4override",
    "NotificationSettings",
    "PayloadLog",
    "UntrustedCERT",
]


class AuditSSH(TypedDict, total=False):
    command_logging: bool
    """Enable to turn on SSH command logging."""


class BISOAdminControls(TypedDict, total=False):
    dcp: bool
    """Set to false to enable copy-pasting."""

    dd: bool
    """Set to false to enable downloading."""

    dk: bool
    """Set to false to enable keyboard usage."""

    dp: bool
    """Set to false to enable printing."""

    du: bool
    """Set to false to enable uploading."""


class CheckSession(TypedDict, total=False):
    duration: str
    """Configure how fresh the session needs to be to be considered valid."""

    enforce: bool
    """Set to true to enable session enforcement."""


class DNSResolvers(TypedDict, total=False):
    ipv4: Iterable[DNSResolverSettingsV4Param]

    ipv6: Iterable[DNSResolverSettingsV6Param]


class Egress(TypedDict, total=False):
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


class L4override(TypedDict, total=False):
    ip: str
    """IPv4 or IPv6 address."""

    port: int
    """A port number to use for TCP/UDP overrides."""


class NotificationSettings(TypedDict, total=False):
    enabled: bool
    """Set notification on"""

    msg: str
    """Customize the message shown in the notification."""

    support_url: str
    """Optional URL to direct users to additional information.

    If not set, the notification will open a block page.
    """


class PayloadLog(TypedDict, total=False):
    enabled: bool
    """Set to true to enable DLP payload logging for this rule."""


class UntrustedCERT(TypedDict, total=False):
    action: Literal["pass_through", "block", "error"]
    """The action performed when an untrusted certificate is seen.

    The default action is an error with HTTP code 526.
    """


class RuleSettingParam(TypedDict, total=False):
    add_headers: object
    """Add custom headers to allowed requests, in the form of key-value pairs.

    Keys are header names, pointing to an array with its header value(s).
    """

    allow_child_bypass: bool
    """Set by parent MSP accounts to enable their children to bypass this rule."""

    audit_ssh: AuditSSH
    """Settings for the Audit SSH action."""

    biso_admin_controls: BISOAdminControls
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

    check_session: CheckSession
    """Configure how session check behaves."""

    dns_resolvers: DNSResolvers
    """Add your own custom resolvers to route queries that match the resolver policy.

    Cannot be used when resolve_dns_through_cloudflare is set. DNS queries will
    route to the address closest to their origin. Only valid when a rule's action is
    set to 'resolve'.
    """

    egress: Egress
    """Configure how Gateway Proxy traffic egresses.

    You can enable this setting for rules with Egress actions and filters, or omit
    it to indicate local egress via WARP IPs.
    """

    ignore_cname_category_matches: bool
    """Set to true, to ignore the category matches at CNAME domains in a response.

    If unchecked, the categories in this rule will be checked against all the CNAME
    domain categories in a response.
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

    l4override: L4override
    """Send matching traffic to the supplied destination IP address and port."""

    notification_settings: NotificationSettings
    """
    Configure a notification to display on the user's device when this rule is
    matched.
    """

    override_host: str
    """Override matching DNS queries with a hostname."""

    override_ips: List[str]
    """Override matching DNS queries with an IP or set of IPs."""

    payload_log: PayloadLog
    """Configure DLP payload logging."""

    resolve_dns_through_cloudflare: bool
    """
    Enable to send queries that match the policy to Cloudflare's default 1.1.1.1 DNS
    resolver. Cannot be set when dns_resolvers are specified. Only valid when a
    rule's action is set to 'resolve'.
    """

    untrusted_cert: UntrustedCERT
    """Configure behavior when an upstream cert is invalid or an SSL error occurs."""
