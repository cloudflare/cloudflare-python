# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = [
    "UnnamedSchemaRef055aaf3918bf29f81c09d394a864182eParam",
    "ActivityLog",
    "Antivirus",
    "AntivirusNotificationSettings",
    "BlockPage",
    "BodyScanning",
    "BrowserIsolation",
    "CustomCertificate",
    "ExtendedEmailMatching",
    "Fips",
    "ProtocolDetection",
    "TLSDecrypt",
]


class ActivityLog(TypedDict, total=False):
    enabled: bool
    """Enable activity logging."""


class AntivirusNotificationSettings(TypedDict, total=False):
    enabled: bool
    """Set notification on"""

    msg: str
    """Customize the message shown in the notification."""

    support_url: str
    """Optional URL to direct users to additional information.

    If not set, the notification will open a block page.
    """


class Antivirus(TypedDict, total=False):
    enabled_download_phase: bool
    """Enable anti-virus scanning on downloads."""

    enabled_upload_phase: bool
    """Enable anti-virus scanning on uploads."""

    fail_closed: bool
    """Block requests for files that cannot be scanned."""

    notification_settings: AntivirusNotificationSettings
    """
    Configure a message to display on the user's device when an antivirus search is
    performed.
    """


class BlockPage(TypedDict, total=False):
    background_color: str
    """Block page background color in #rrggbb format."""

    enabled: bool
    """Enable only cipher suites and TLS versions compliant with FIPS 140-2."""

    footer_text: str
    """Block page footer text."""

    header_text: str
    """Block page header text."""

    logo_path: str
    """Full URL to the logo file."""

    mailto_address: str
    """Admin email for users to contact."""

    mailto_subject: str
    """Subject line for emails created from block page."""

    name: str
    """Block page title."""

    suppress_footer: bool
    """Suppress detailed info at the bottom of the block page."""


class BodyScanning(TypedDict, total=False):
    inspection_mode: str
    """Set the inspection mode to either `deep` or `shallow`."""


class BrowserIsolation(TypedDict, total=False):
    non_identity_enabled: bool
    """Enable non-identity onramp support for Browser Isolation."""

    url_browser_isolation_enabled: bool
    """Enable Clientless Browser Isolation."""


class CustomCertificate(TypedDict, total=False):
    enabled: Required[bool]
    """Enable use of custom certificate authority for signing Gateway traffic."""

    id: str
    """UUID of certificate (ID from MTLS certificate store)."""


class ExtendedEmailMatching(TypedDict, total=False):
    enabled: bool
    """Enable matching all variants of user emails (with + or .

    modifiers) used as criteria in Firewall policies.
    """


class Fips(TypedDict, total=False):
    tls: bool
    """Enable only cipher suites and TLS versions compliant with FIPS 140-2."""


class ProtocolDetection(TypedDict, total=False):
    enabled: bool
    """Enable detecting protocol on initial bytes of client traffic."""


class TLSDecrypt(TypedDict, total=False):
    enabled: bool
    """Enable inspecting encrypted HTTP traffic."""


class UnnamedSchemaRef055aaf3918bf29f81c09d394a864182eParam(TypedDict, total=False):
    activity_log: ActivityLog
    """Activity log settings."""

    antivirus: Antivirus
    """Anti-virus settings."""

    block_page: BlockPage
    """Block page layout settings."""

    body_scanning: BodyScanning
    """DLP body scanning settings."""

    browser_isolation: BrowserIsolation
    """Browser isolation settings."""

    custom_certificate: CustomCertificate
    """Custom certificate settings for BYO-PKI."""

    extended_email_matching: ExtendedEmailMatching
    """Extended e-mail matching settings."""

    fips: Fips
    """FIPS settings."""

    protocol_detection: ProtocolDetection
    """Protocol Detection settings."""

    tls_decrypt: TLSDecrypt
    """TLS interception settings."""
