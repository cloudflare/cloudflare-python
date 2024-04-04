# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = [
    "UnnamedSchemaRef125",
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


class ActivityLog(BaseModel):
    enabled: Optional[bool] = None
    """Enable activity logging."""


class AntivirusNotificationSettings(BaseModel):
    enabled: Optional[bool] = None
    """Set notification on"""

    msg: Optional[str] = None
    """Customize the message shown in the notification."""

    support_url: Optional[str] = None
    """Optional URL to direct users to additional information.

    If not set, the notification will open a block page.
    """


class Antivirus(BaseModel):
    enabled_download_phase: Optional[bool] = None
    """Enable anti-virus scanning on downloads."""

    enabled_upload_phase: Optional[bool] = None
    """Enable anti-virus scanning on uploads."""

    fail_closed: Optional[bool] = None
    """Block requests for files that cannot be scanned."""

    notification_settings: Optional[AntivirusNotificationSettings] = None
    """
    Configure a message to display on the user's device when an antivirus search is
    performed.
    """


class BlockPage(BaseModel):
    background_color: Optional[str] = None
    """Block page background color in #rrggbb format."""

    enabled: Optional[bool] = None
    """Enable only cipher suites and TLS versions compliant with FIPS 140-2."""

    footer_text: Optional[str] = None
    """Block page footer text."""

    header_text: Optional[str] = None
    """Block page header text."""

    logo_path: Optional[str] = None
    """Full URL to the logo file."""

    mailto_address: Optional[str] = None
    """Admin email for users to contact."""

    mailto_subject: Optional[str] = None
    """Subject line for emails created from block page."""

    name: Optional[str] = None
    """Block page title."""

    suppress_footer: Optional[bool] = None
    """Suppress detailed info at the bottom of the block page."""


class BodyScanning(BaseModel):
    inspection_mode: Optional[str] = None
    """Set the inspection mode to either `deep` or `shallow`."""


class BrowserIsolation(BaseModel):
    non_identity_enabled: Optional[bool] = None
    """Enable non-identity onramp support for Browser Isolation."""

    url_browser_isolation_enabled: Optional[bool] = None
    """Enable Clientless Browser Isolation."""


class CustomCertificate(BaseModel):
    enabled: bool
    """Enable use of custom certificate authority for signing Gateway traffic."""

    id: Optional[str] = None
    """UUID of certificate (ID from MTLS certificate store)."""

    binding_status: Optional[str] = None
    """Certificate status (internal)."""

    updated_at: Optional[datetime] = None


class ExtendedEmailMatching(BaseModel):
    enabled: Optional[bool] = None
    """Enable matching all variants of user emails (with + or .

    modifiers) used as criteria in Firewall policies.
    """


class Fips(BaseModel):
    tls: Optional[bool] = None
    """Enable only cipher suites and TLS versions compliant with FIPS 140-2."""


class ProtocolDetection(BaseModel):
    enabled: Optional[bool] = None
    """Enable detecting protocol on initial bytes of client traffic."""


class TLSDecrypt(BaseModel):
    enabled: Optional[bool] = None
    """Enable inspecting encrypted HTTP traffic."""


class UnnamedSchemaRef125(BaseModel):
    activity_log: Optional[ActivityLog] = None
    """Activity log settings."""

    antivirus: Optional[Antivirus] = None
    """Anti-virus settings."""

    block_page: Optional[BlockPage] = None
    """Block page layout settings."""

    body_scanning: Optional[BodyScanning] = None
    """DLP body scanning settings."""

    browser_isolation: Optional[BrowserIsolation] = None
    """Browser isolation settings."""

    custom_certificate: Optional[CustomCertificate] = None
    """Custom certificate settings for BYO-PKI."""

    extended_email_matching: Optional[ExtendedEmailMatching] = None
    """Extended e-mail matching settings."""

    fips: Optional[Fips] = None
    """FIPS settings."""

    protocol_detection: Optional[ProtocolDetection] = None
    """Protocol Detection settings."""

    tls_decrypt: Optional[TLSDecrypt] = None
    """TLS interception settings."""
