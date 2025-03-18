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
    "CheckSession",
    "DNSResolvers",
    "Egress",
    "L4override",
    "NotificationSettings",
    "PayloadLog",
    "Quarantine",
    "ResolveDNSInternally",
    "UntrustedCERT",
]


class AuditSSH(BaseModel):
    command_logging: Optional[bool] = None
    """Enable to turn on SSH command logging."""


class BISOAdminControls(BaseModel):
    copy_: Optional[Literal["enabled", "disabled", "remote_only"]] = FieldInfo(alias="copy", default=None)
    """Configure whether copy is enabled or not.

    When set with "remote_only", copying isolated content from the remote browser to
    the user's local clipboard is disabled. When absent, copy is enabled. Only
    applies when `version == "v2"`.
    """

    dcp: Optional[bool] = None
    """Set to false to enable copy-pasting. Only applies when `version == "v1"`."""

    dd: Optional[bool] = None
    """Set to false to enable downloading. Only applies when `version == "v1"`."""

    dk: Optional[bool] = None
    """Set to false to enable keyboard usage. Only applies when `version == "v1"`."""

    download: Optional[Literal["enabled", "disabled"]] = None
    """Configure whether downloading enabled or not.

    When absent, downloading is enabled. Only applies when `version == "v2"`.
    """

    dp: Optional[bool] = None
    """Set to false to enable printing. Only applies when `version == "v1"`."""

    du: Optional[bool] = None
    """Set to false to enable uploading. Only applies when `version == "v1"`."""

    keyboard: Optional[Literal["enabled", "disabled"]] = None
    """Configure whether keyboard usage is enabled or not.

    When absent, keyboard usage is enabled. Only applies when `version == "v2"`.
    """

    paste: Optional[Literal["enabled", "disabled", "remote_only"]] = None
    """Configure whether pasting is enabled or not.

    When set with "remote_only", pasting content from the user's local clipboard
    into isolated pages is disabled. When absent, paste is enabled. Only applies
    when `version == "v2"`.
    """

    printing: Optional[Literal["enabled", "disabled"]] = None
    """Configure whether printing is enabled or not.

    When absent, printing is enabled. Only applies when `version == "v2"`.
    """

    upload: Optional[Literal["enabled", "disabled"]] = None
    """Configure whether uploading is enabled or not.

    When absent, uploading is enabled. Only applies when `version == "v2"`.
    """

    version: Optional[Literal["v1", "v2"]] = None
    """Indicates which version of the browser isolation controls should apply."""


class CheckSession(BaseModel):
    duration: Optional[str] = None
    """Configure how fresh the session needs to be to be considered valid."""

    enforce: Optional[bool] = None
    """Set to true to enable session enforcement."""


class DNSResolvers(BaseModel):
    ipv4: Optional[List[DNSResolverSettingsV4]] = None

    ipv6: Optional[List[DNSResolverSettingsV6]] = None


class Egress(BaseModel):
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


class L4override(BaseModel):
    ip: Optional[str] = None
    """IPv4 or IPv6 address."""

    port: Optional[int] = None
    """A port number to use for TCP/UDP overrides."""


class NotificationSettings(BaseModel):
    enabled: Optional[bool] = None
    """Set notification on"""

    msg: Optional[str] = None
    """Customize the message shown in the notification."""

    support_url: Optional[str] = None
    """Optional URL to direct users to additional information.

    If not set, the notification will open a block page.
    """


class PayloadLog(BaseModel):
    enabled: Optional[bool] = None
    """Set to true to enable DLP payload logging for this rule."""


class Quarantine(BaseModel):
    file_types: Optional[
        List[Literal["exe", "pdf", "doc", "docm", "docx", "rtf", "ppt", "pptx", "xls", "xlsm", "xlsx", "zip", "rar"]]
    ] = None
    """Types of files to sandbox."""


class ResolveDNSInternally(BaseModel):
    fallback: Optional[Literal["none", "public_dns"]] = None
    """
    The fallback behavior to apply when the internal DNS response code is different
    from 'NOERROR' or when the response data only contains CNAME records for 'A' or
    'AAAA' queries.
    """

    view_id: Optional[str] = None
    """The internal DNS view identifier that's passed to the internal DNS service."""


class UntrustedCERT(BaseModel):
    action: Optional[Literal["pass_through", "block", "error"]] = None
    """The action performed when an untrusted certificate is seen.

    The default action is an error with HTTP code 526.
    """


class RuleSetting(BaseModel):
    add_headers: Optional[Dict[str, str]] = None
    """Add custom headers to allowed requests, in the form of key-value pairs.

    Keys are header names, pointing to an array with its header value(s).
    """

    allow_child_bypass: Optional[bool] = None
    """Set by parent MSP accounts to enable their children to bypass this rule."""

    audit_ssh: Optional[AuditSSH] = None
    """Settings for the Audit SSH action."""

    biso_admin_controls: Optional[BISOAdminControls] = None
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

    check_session: Optional[CheckSession] = None
    """Configure how session check behaves."""

    dns_resolvers: Optional[DNSResolvers] = None
    """Add your own custom resolvers to route queries that match the resolver policy.

    Cannot be used when 'resolve_dns_through_cloudflare' or 'resolve_dns_internally'
    are set. DNS queries will route to the address closest to their origin. Only
    valid when a rule's action is set to 'resolve'.
    """

    egress: Optional[Egress] = None
    """Configure how Gateway Proxy traffic egresses.

    You can enable this setting for rules with Egress actions and filters, or omit
    it to indicate local egress via WARP IPs.
    """

    ignore_cname_category_matches: Optional[bool] = None
    """Set to true, to ignore the category matches at CNAME domains in a response.

    If unchecked, the categories in this rule will be checked against all the CNAME
    domain categories in a response.
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

    l4override: Optional[L4override] = None
    """Send matching traffic to the supplied destination IP address and port."""

    notification_settings: Optional[NotificationSettings] = None
    """
    Configure a notification to display on the user's device when this rule is
    matched.
    """

    override_host: Optional[str] = None
    """Override matching DNS queries with a hostname."""

    override_ips: Optional[List[str]] = None
    """Override matching DNS queries with an IP or set of IPs."""

    payload_log: Optional[PayloadLog] = None
    """Configure DLP payload logging."""

    quarantine: Optional[Quarantine] = None
    """Settings that apply to quarantine rules"""

    resolve_dns_internally: Optional[ResolveDNSInternally] = None
    """
    Configure to forward the query to the internal DNS service, passing the
    specified 'view_id' as input. Cannot be set when 'dns_resolvers' are specified
    or 'resolve_dns_through_cloudflare' is set. Only valid when a rule's action is
    set to 'resolve'.
    """

    resolve_dns_through_cloudflare: Optional[bool] = None
    """
    Enable to send queries that match the policy to Cloudflare's default 1.1.1.1 DNS
    resolver. Cannot be set when 'dns_resolvers' are specified or
    'resolve_dns_internally' is set. Only valid when a rule's action is set to
    'resolve'.
    """

    untrusted_cert: Optional[UntrustedCERT] = None
    """Configure behavior when an upstream cert is invalid or an SSL error occurs."""
