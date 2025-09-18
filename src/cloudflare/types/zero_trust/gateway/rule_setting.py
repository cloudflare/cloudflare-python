# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .dns_resolver_settings_v4 import DNSResolverSettingsV4
from .dns_resolver_settings_v6 import DNSResolverSettingsV6

__all__ = [
    "RuleSetting",
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


class AuditSSH(BaseModel):
    command_logging: Optional[bool] = None
    """Enable SSH command logging."""


class BISOAdminControls(BaseModel):
    copy_: Optional[Literal["enabled", "disabled", "remote_only"]] = FieldInfo(alias="copy", default=None)
    """Configure copy behavior.

    If set to remote_only, users cannot copy isolated content from the remote
    browser to the local clipboard. If this field is absent, copying remains
    enabled. Applies only when version == "v2".
    """

    dcp: Optional[bool] = None
    """Set to false to enable copy-pasting. Only applies when `version == "v1"`."""

    dd: Optional[bool] = None
    """Set to false to enable downloading. Only applies when `version == "v1"`."""

    dk: Optional[bool] = None
    """Set to false to enable keyboard usage. Only applies when `version == "v1"`."""

    download: Optional[Literal["enabled", "disabled", "remote_only"]] = None
    """Configure download behavior.

    When set to remote_only, users can view downloads but cannot save them. Applies
    only when version == "v2".
    """

    dp: Optional[bool] = None
    """Set to false to enable printing. Only applies when `version == "v1"`."""

    du: Optional[bool] = None
    """Set to false to enable uploading. Only applies when `version == "v1"`."""

    keyboard: Optional[Literal["enabled", "disabled"]] = None
    """Configure keyboard usage behavior.

    If this field is absent, keyboard usage remains enabled. Applies only when
    version == "v2".
    """

    paste: Optional[Literal["enabled", "disabled", "remote_only"]] = None
    """Configure paste behavior.

    If set to remote_only, users cannot paste content from the local clipboard into
    isolated pages. If this field is absent, pasting remains enabled. Applies only
    when version == "v2".
    """

    printing: Optional[Literal["enabled", "disabled"]] = None
    """Configure print behavior.

    Default, Printing is enabled. Applies only when version == "v2".
    """

    upload: Optional[Literal["enabled", "disabled"]] = None
    """Configure upload behavior.

    If this field is absent, uploading remains enabled. Applies only when version ==
    "v2".
    """

    version: Optional[Literal["v1", "v2"]] = None
    """Indicate which version of the browser isolation controls should apply."""


class BlockPage(BaseModel):
    target_uri: str
    """Specify the URI to which the user is redirected."""

    include_context: Optional[bool] = None
    """Specify whether to pass the context information as query parameters."""


class CheckSession(BaseModel):
    duration: Optional[str] = None
    """Sets the required session freshness threshold.

    The API returns a normalized version of this value.
    """

    enforce: Optional[bool] = None
    """Enable session enforcement."""


class DNSResolvers(BaseModel):
    ipv4: Optional[List[DNSResolverSettingsV4]] = None

    ipv6: Optional[List[DNSResolverSettingsV6]] = None


class Egress(BaseModel):
    ipv4: Optional[str] = None
    """Specify the IPv4 address to use for egress."""

    ipv4_fallback: Optional[str] = None
    """Specify the fallback IPv4 address to use for egress when the primary IPv4 fails.

    Set '0.0.0.0' to indicate local egress via WARP IPs.
    """

    ipv6: Optional[str] = None
    """Specify the IPv6 range to use for egress."""


class L4override(BaseModel):
    ip: Optional[str] = None
    """Defines the IPv4 or IPv6 address."""

    port: Optional[int] = None
    """Defines a port number to use for TCP/UDP overrides."""


class NotificationSettings(BaseModel):
    enabled: Optional[bool] = None
    """Enable notification."""

    include_context: Optional[bool] = None
    """Indicates whether to pass the context information as query parameters."""

    msg: Optional[str] = None
    """Customize the message shown in the notification."""

    support_url: Optional[str] = None
    """Defines an optional URL to direct users to additional information.

    If unset, the notification opens a block page.
    """


class PayloadLog(BaseModel):
    enabled: Optional[bool] = None
    """Enable DLP payload logging for this rule."""


class Quarantine(BaseModel):
    file_types: Optional[
        List[Literal["exe", "pdf", "doc", "docm", "docx", "rtf", "ppt", "pptx", "xls", "xlsm", "xlsx", "zip", "rar"]]
    ] = None
    """Specify the types of files to sandbox."""


class Redirect(BaseModel):
    target_uri: str
    """Specify the URI to which the user is redirected."""

    include_context: Optional[bool] = None
    """Specify whether to pass the context information as query parameters."""

    preserve_path_and_query: Optional[bool] = None
    """
    Specify whether to append the path and query parameters from the original
    request to target_uri.
    """


class ResolveDNSInternally(BaseModel):
    fallback: Optional[Literal["none", "public_dns"]] = None
    """
    Specify the fallback behavior to apply when the internal DNS response code
    differs from 'NOERROR' or when the response data contains only CNAME records for
    'A' or 'AAAA' queries.
    """

    view_id: Optional[str] = None
    """Specify the internal DNS view identifier to pass to the internal DNS service."""


class UntrustedCERT(BaseModel):
    action: Optional[Literal["pass_through", "block", "error"]] = None
    """Defines the action performed when an untrusted certificate seen.

    The default action an error with HTTP code 526.
    """


class RuleSetting(BaseModel):
    add_headers: Optional[Dict[str, List[str]]] = None
    """Add custom headers to allowed requests as key-value pairs.

    Use header names as keys that map to arrays of header values.
    """

    allow_child_bypass: Optional[bool] = None
    """Set to enable MSP children to bypass this rule.

    Only parent MSP accounts can set this. this rule.
    """

    audit_ssh: Optional[AuditSSH] = None
    """Define the settings for the Audit SSH action."""

    biso_admin_controls: Optional[BISOAdminControls] = None
    """Configure browser isolation behavior."""

    block_page: Optional[BlockPage] = None
    """Configure custom block page settings.

    If missing or null, use the account settings.
    """

    block_page_enabled: Optional[bool] = None
    """Enable the custom block page."""

    block_reason: Optional[str] = None
    """Explain why the rule blocks the request.

    The custom block page shows this text (if enabled).
    """

    bypass_parent_rule: Optional[bool] = None
    """Set to enable MSP accounts to bypass their parent's rules.

    Only MSP child accounts can set this.
    """

    check_session: Optional[CheckSession] = None
    """Configure session check behavior."""

    dns_resolvers: Optional[DNSResolvers] = None
    """Configure custom resolvers to route queries that match the resolver policy.

    Unused with 'resolve_dns_through_cloudflare' or 'resolve_dns_internally'
    settings. DNS queries get routed to the address closest to their origin. Only
    valid when a rule's action is set to 'resolve'.
    """

    egress: Optional[Egress] = None
    """Configure how Gateway Proxy traffic egresses.

    You can enable this setting for rules with Egress actions and filters, or omit
    it to indicate local egress via WARP IPs.
    """

    ignore_cname_category_matches: Optional[bool] = None
    """Ignore category matches at CNAME domains in a response.

    When off, evaluate categories in this rule against all CNAME domain categories
    in the response.
    """

    insecure_disable_dnssec_validation: Optional[bool] = None
    """Specify whether to disable DNSSEC validation (for Allow actions) [INSECURE]."""

    ip_categories: Optional[bool] = None
    """Enable IPs in DNS resolver category blocks.

    The system blocks only domain name categories unless you enable this setting.
    """

    ip_indicator_feeds: Optional[bool] = None
    """Indicates whether to include IPs in DNS resolver indicator feed blocks.

    Default, indicator feeds block only domain names.
    """

    l4override: Optional[L4override] = None
    """Send matching traffic to the supplied destination IP address. and port."""

    notification_settings: Optional[NotificationSettings] = None
    """
    Configure a notification to display on the user's device when this rule matched.
    """

    override_host: Optional[str] = None
    """Defines a hostname for override, for the matching DNS queries."""

    override_ips: Optional[List[str]] = None
    """Defines a an IP or set of IPs for overriding matched DNS queries."""

    payload_log: Optional[PayloadLog] = None
    """Configure DLP payload logging."""

    quarantine: Optional[Quarantine] = None
    """Configure settings that apply to quarantine rules."""

    redirect: Optional[Redirect] = None
    """Apply settings to redirect rules."""

    resolve_dns_internally: Optional[ResolveDNSInternally] = None
    """
    Configure to forward the query to the internal DNS service, passing the
    specified 'view_id' as input. Not used when 'dns_resolvers' is specified or
    'resolve_dns_through_cloudflare' is set. Only valid when a rule's action is set
    to 'resolve'.
    """

    resolve_dns_through_cloudflare: Optional[bool] = None
    """
    Enable to send queries that match the policy to Cloudflare's default 1.1.1.1 DNS
    resolver. Cannot set when 'dns_resolvers' specified or 'resolve_dns_internally'
    is set. Only valid when a rule's action set to 'resolve'.
    """

    untrusted_cert: Optional[UntrustedCERT] = None
    """
    Configure behavior when an upstream certificate is invalid or an SSL error
    occurs.
    """
