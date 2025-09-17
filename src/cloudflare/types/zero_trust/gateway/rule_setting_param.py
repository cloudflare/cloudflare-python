# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr
from .dns_resolver_settings_v4_param import DNSResolverSettingsV4Param
from .dns_resolver_settings_v6_param import DNSResolverSettingsV6Param

__all__ = [
    "RuleSettingParam",
    "AuditSSH",
    "BISOAdminControls",
    "BlockPage",
    "CheckSession",
    "DNSResolvers",
    "Egress",
    "L4override",
    "NotificationSettings",
    "PayloadLog",
    "Quarantine",
    "Redirect",
    "ResolveDNSInternally",
    "UntrustedCERT",
]


class AuditSSH(TypedDict, total=False):
    command_logging: bool
    """Enable SSH command logging."""


class BISOAdminControls(TypedDict, total=False):
    copy: Literal["enabled", "disabled", "remote_only"]
    """Configure copy behavior.

    If set to remote_only, users cannot copy isolated content from the remote
    browser to the local clipboard. If this field is absent, copying remains
    enabled. Applies only when version == "v2".
    """

    dcp: bool
    """Set to false to enable copy-pasting. Only applies when `version == "v1"`."""

    dd: bool
    """Set to false to enable downloading. Only applies when `version == "v1"`."""

    dk: bool
    """Set to false to enable keyboard usage. Only applies when `version == "v1"`."""

    download: Literal["enabled", "disabled", "remote_only"]
    """Configure download behavior.

    When set to remote_only, users can view downloads but cannot save them. Applies
    only when version == "v2".
    """

    dp: bool
    """Set to false to enable printing. Only applies when `version == "v1"`."""

    du: bool
    """Set to false to enable uploading. Only applies when `version == "v1"`."""

    keyboard: Literal["enabled", "disabled"]
    """Configure keyboard usage behavior.

    If this field is absent, keyboard usage remains enabled. Applies only when
    version == "v2".
    """

    paste: Literal["enabled", "disabled", "remote_only"]
    """Configure paste behavior.

    If set to remote_only, users cannot paste content from the local clipboard into
    isolated pages. If this field is absent, pasting remains enabled. Applies only
    when version == "v2".
    """

    printing: Literal["enabled", "disabled"]
    """Configure print behavior.

    Default, Printing is enabled. Applies only when version == "v2".
    """

    upload: Literal["enabled", "disabled"]
    """Configure upload behavior.

    If this field is absent, uploading remains enabled. Applies only when version ==
    "v2".
    """

    version: Literal["v1", "v2"]
    """Indicate which version of the browser isolation controls should apply."""


class BlockPage(TypedDict, total=False):
    target_uri: Required[str]
    """Specify the URI to which the user is redirected."""

    include_context: bool
    """Specify whether to pass the context information as query parameters."""


class CheckSession(TypedDict, total=False):
    duration: str
    """Sets the required session freshness threshold.

    The API returns a normalized version of this value.
    """

    enforce: bool
    """Enable session enforcement."""


class DNSResolvers(TypedDict, total=False):
    ipv4: Iterable[DNSResolverSettingsV4Param]

    ipv6: Iterable[DNSResolverSettingsV6Param]


class Egress(TypedDict, total=False):
    ipv4: str
    """Specify the IPv4 address to use for egress."""

    ipv4_fallback: str
    """Specify the fallback IPv4 address to use for egress when the primary IPv4 fails.

    Set '0.0.0.0' to indicate local egress via WARP IPs.
    """

    ipv6: str
    """Specify the IPv6 range to use for egress."""


class L4override(TypedDict, total=False):
    ip: str
    """Defines the IPv4 or IPv6 address."""

    port: int
    """Defines a port number to use for TCP/UDP overrides."""


class NotificationSettings(TypedDict, total=False):
    enabled: bool
    """Enable notification."""

    include_context: bool
    """Indicates whether to pass the context information as query parameters."""

    msg: str
    """Customize the message shown in the notification."""

    support_url: str
    """Defines an optional URL to direct users to additional information.

    If unset, the notification opens a block page.
    """


class PayloadLog(TypedDict, total=False):
    enabled: bool
    """Enable DLP payload logging for this rule."""


class Quarantine(TypedDict, total=False):
    file_types: List[
        Literal["exe", "pdf", "doc", "docm", "docx", "rtf", "ppt", "pptx", "xls", "xlsm", "xlsx", "zip", "rar"]
    ]
    """Specify the types of files to sandbox."""


class Redirect(TypedDict, total=False):
    target_uri: Required[str]
    """Specify the URI to which the user is redirected."""

    include_context: bool
    """Specify whether to pass the context information as query parameters."""

    preserve_path_and_query: bool
    """
    Specify whether to append the path and query parameters from the original
    request to target_uri.
    """


class ResolveDNSInternally(TypedDict, total=False):
    fallback: Literal["none", "public_dns"]
    """
    Specify the fallback behavior to apply when the internal DNS response code
    differs from 'NOERROR' or when the response data contains only CNAME records for
    'A' or 'AAAA' queries.
    """

    view_id: str
    """Specify the internal DNS view identifier to pass to the internal DNS service."""


class UntrustedCERT(TypedDict, total=False):
    action: Literal["pass_through", "block", "error"]
    """Defines the action performed when an untrusted certificate seen.

    The default action an error with HTTP code 526.
    """


class RuleSettingParam(TypedDict, total=False):
    add_headers: Optional[Dict[str, SequenceNotStr[str]]]
    """Add custom headers to allowed requests as key-value pairs.

    Use header names as keys that map to arrays of header values.
    """

    allow_child_bypass: Optional[bool]
    """Set to enable MSP children to bypass this rule.

    Only parent MSP accounts can set this. this rule.
    """

    audit_ssh: Optional[AuditSSH]
    """Define the settings for the Audit SSH action."""

    biso_admin_controls: BISOAdminControls
    """Configure browser isolation behavior."""

    block_page: Optional[BlockPage]
    """Configure custom block page settings.

    If missing or null, use the account settings.
    """

    block_page_enabled: bool
    """Enable the custom block page."""

    block_reason: Optional[str]
    """Explain why the rule blocks the request.

    The custom block page shows this text (if enabled).
    """

    bypass_parent_rule: Optional[bool]
    """Set to enable MSP accounts to bypass their parent's rules.

    Only MSP child accounts can set this.
    """

    check_session: Optional[CheckSession]
    """Configure session check behavior."""

    dns_resolvers: Optional[DNSResolvers]
    """Configure custom resolvers to route queries that match the resolver policy.

    Unused with 'resolve_dns_through_cloudflare' or 'resolve_dns_internally'
    settings. DNS queries get routed to the address closest to their origin. Only
    valid when a rule's action is set to 'resolve'.
    """

    egress: Optional[Egress]
    """Configure how Gateway Proxy traffic egresses.

    You can enable this setting for rules with Egress actions and filters, or omit
    it to indicate local egress via WARP IPs.
    """

    ignore_cname_category_matches: bool
    """Ignore category matches at CNAME domains in a response.

    When off, evaluate categories in this rule against all CNAME domain categories
    in the response.
    """

    insecure_disable_dnssec_validation: bool
    """Specify whether to disable DNSSEC validation (for Allow actions) [INSECURE]."""

    ip_categories: bool
    """Enable IPs in DNS resolver category blocks.

    The system blocks only domain name categories unless you enable this setting.
    """

    ip_indicator_feeds: bool
    """Indicates whether to include IPs in DNS resolver indicator feed blocks.

    Default, indicator feeds block only domain names.
    """

    l4override: Optional[L4override]
    """Send matching traffic to the supplied destination IP address. and port."""

    notification_settings: Optional[NotificationSettings]
    """
    Configure a notification to display on the user's device when this rule matched.
    """

    override_host: str
    """Defines a hostname for override, for the matching DNS queries."""

    override_ips: Optional[SequenceNotStr[str]]
    """Defines a an IP or set of IPs for overriding matched DNS queries."""

    payload_log: Optional[PayloadLog]
    """Configure DLP payload logging."""

    quarantine: Optional[Quarantine]
    """Configure settings that apply to quarantine rules."""

    redirect: Optional[Redirect]
    """Apply settings to redirect rules."""

    resolve_dns_internally: Optional[ResolveDNSInternally]
    """
    Configure to forward the query to the internal DNS service, passing the
    specified 'view_id' as input. Not used when 'dns_resolvers' is specified or
    'resolve_dns_through_cloudflare' is set. Only valid when a rule's action is set
    to 'resolve'.
    """

    resolve_dns_through_cloudflare: Optional[bool]
    """
    Enable to send queries that match the policy to Cloudflare's default 1.1.1.1 DNS
    resolver. Cannot set when 'dns_resolvers' specified or 'resolve_dns_internally'
    is set. Only valid when a rule's action set to 'resolve'.
    """

    untrusted_cert: Optional[UntrustedCERT]
    """
    Configure behavior when an upstream certificate is invalid or an SSL error
    occurs.
    """
