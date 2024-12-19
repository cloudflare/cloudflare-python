# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .tls_settings import TLSSettings
from .fips_settings import FipsSettings
from .protocol_detection import ProtocolDetection
from .anti_virus_settings import AntiVirusSettings
from .block_page_settings import BlockPageSettings
from .activity_log_settings import ActivityLogSettings
from .body_scanning_settings import BodyScanningSettings
from .extended_email_matching import ExtendedEmailMatching
from .browser_isolation_settings import BrowserIsolationSettings
from .custom_certificate_settings import CustomCertificateSettings

__all__ = ["GatewayConfigurationSettings", "Certificate", "Sandbox"]


class Certificate(BaseModel):
    id: str
    """UUID of certificate to be used for interception.

    Certificate must be available (previously called 'active') on the edge. A nil
    UUID will indicate the Cloudflare Root CA should be used.
    """


class Sandbox(BaseModel):
    enabled: Optional[bool] = None
    """Enable sandbox."""

    fallback_action: Optional[Literal["allow", "block"]] = None
    """Action to take when the file cannot be scanned."""


class GatewayConfigurationSettings(BaseModel):
    activity_log: Optional[ActivityLogSettings] = None
    """Activity log settings."""

    antivirus: Optional[AntiVirusSettings] = None
    """Anti-virus settings."""

    block_page: Optional[BlockPageSettings] = None
    """Block page layout settings."""

    body_scanning: Optional[BodyScanningSettings] = None
    """DLP body scanning settings."""

    browser_isolation: Optional[BrowserIsolationSettings] = None
    """Browser isolation settings."""

    certificate: Optional[Certificate] = None
    """Certificate settings for Gateway TLS interception.

    If not specified, the Cloudflare Root CA will be used.
    """

    custom_certificate: Optional[CustomCertificateSettings] = None
    """Custom certificate settings for BYO-PKI.

    (deprecated and replaced by `certificate`)
    """

    extended_email_matching: Optional[ExtendedEmailMatching] = None
    """Extended e-mail matching settings."""

    fips: Optional[FipsSettings] = None
    """FIPS settings."""

    protocol_detection: Optional[ProtocolDetection] = None
    """Protocol Detection settings."""

    sandbox: Optional[Sandbox] = None
    """Sandbox settings."""

    tls_decrypt: Optional[TLSSettings] = None
    """TLS interception settings."""
