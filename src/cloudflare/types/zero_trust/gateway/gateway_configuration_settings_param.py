# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

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

__all__ = ["GatewayConfigurationSettingsParam", "Certificate", "Sandbox"]


class Certificate(TypedDict, total=False):
    id: Required[str]
    """UUID of certificate to be used for interception.

    Certificate must be available (previously called 'active') on the edge. A nil
    UUID will indicate the Cloudflare Root CA should be used.
    """


class Sandbox(TypedDict, total=False):
    enabled: bool
    """Enable sandbox."""

    fallback_action: Literal["allow", "block"]
    """Action to take when the file cannot be scanned."""


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

    certificate: Certificate
    """Certificate settings for Gateway TLS interception.

    If not specified, the Cloudflare Root CA will be used.
    """

    custom_certificate: CustomCertificateSettingsParam
    """Custom certificate settings for BYO-PKI.

    (deprecated and replaced by `certificate`)
    """

    extended_email_matching: ExtendedEmailMatchingParam
    """Extended e-mail matching settings."""

    fips: FipsSettingsParam
    """FIPS settings."""

    protocol_detection: ProtocolDetectionParam
    """Protocol Detection settings."""

    sandbox: Sandbox
    """Sandbox settings."""

    tls_decrypt: TLSSettingsParam
    """TLS interception settings."""
