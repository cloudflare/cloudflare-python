# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

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

__all__ = ["UnnamedSchemaRef055aaf3918bf29f81c09d394a864182e"]


class UnnamedSchemaRef055aaf3918bf29f81c09d394a864182e(BaseModel):
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

    custom_certificate: Optional[CustomCertificateSettings] = None
    """Custom certificate settings for BYO-PKI."""

    extended_email_matching: Optional[ExtendedEmailMatching] = None
    """Extended e-mail matching settings."""

    fips: Optional[FipsSettings] = None
    """FIPS settings."""

    protocol_detection: Optional[ProtocolDetection] = None
    """Protocol Detection settings."""

    tls_decrypt: Optional[TLSSettings] = None
    """TLS interception settings."""
