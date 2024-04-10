# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .tls_settings_param import TLSSettingsParam
from .fips_settings_param import FipsSettingsParam
from .protocol_detection_param import ProtocolDetectionParam
from .anti_virus_settings_param import AntiVirusSettingsParam
from .block_page_settings_param import BlockPageSettingsParam
from .activity_log_settings_param import ActivityLogSettingsParam
from .body_scanning_settings_param import BodyScanningSettingsParam
from .extended_email_matching_param import ExtendedEmailMatchingParam
from .browser_isolation_settings_param import BrowserIsolationSettingsParam
from .custom_certificate_settings_param import CustomCertificateSettingsParam

__all__ = ["GatewayConfigurationSettingsParam"]


class GatewayConfigurationSettingsParam(TypedDict, total=False):
    activity_log: ActivityLogSettingsParam
    """Activity log settings."""

    antivirus: AntiVirusSettingsParam
    """Anti-virus settings."""

    block_page: BlockPageSettingsParam
    """Block page layout settings."""

    body_scanning: BodyScanningSettingsParam
    """DLP body scanning settings."""

    browser_isolation: BrowserIsolationSettingsParam
    """Browser isolation settings."""

    custom_certificate: CustomCertificateSettingsParam
    """Custom certificate settings for BYO-PKI."""

    extended_email_matching: ExtendedEmailMatchingParam
    """Extended e-mail matching settings."""

    fips: FipsSettingsParam
    """FIPS settings."""

    protocol_detection: ProtocolDetectionParam
    """Protocol Detection settings."""

    tls_decrypt: TLSSettingsParam
    """TLS interception settings."""
