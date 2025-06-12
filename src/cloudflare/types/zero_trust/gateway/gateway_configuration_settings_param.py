# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
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

__all__ = ["GatewayConfigurationSettingsParam", "AppControlSettings", "Certificate", "HostSelector", "Sandbox"]


class AppControlSettings(TypedDict, total=False):
    enabled: bool
    """Enable App Control"""


class Certificate(TypedDict, total=False):
    id: Required[str]
    """UUID of certificate to be used for interception.

    Certificate must be available (previously called 'active') on the edge. A nil
    UUID will indicate the Cloudflare Root CA should be used.
    """


class HostSelector(TypedDict, total=False):
    enabled: bool
    """Enable filtering via hosts for egress policies."""


class Sandbox(TypedDict, total=False):
    enabled: bool
    """Enable sandbox."""

    fallback_action: Literal["allow", "block"]
    """Action to take when the file cannot be scanned."""


class GatewayConfigurationSettingsParam(TypedDict, total=False):
    activity_log: Optional[ActivityLogSettingsParam]
    """Activity log settings."""

    antivirus: Optional[AntiVirusSettingsParam]
    """Anti-virus settings."""

    app_control_settings: Annotated[Optional[AppControlSettings], PropertyInfo(alias="app-control-settings")]
    """Setting to enable App Control"""

    block_page: Optional[BlockPageSettingsParam]
    """Block page layout settings."""

    body_scanning: Optional[BodyScanningSettingsParam]
    """DLP body scanning settings."""

    browser_isolation: Optional[BrowserIsolationSettingsParam]
    """Browser isolation settings."""

    certificate: Optional[Certificate]
    """Certificate settings for Gateway TLS interception.

    If not specified, the Cloudflare Root CA will be used.
    """

    custom_certificate: Optional[CustomCertificateSettingsParam]
    """Custom certificate settings for BYO-PKI.

    (deprecated and replaced by `certificate`)
    """

    extended_email_matching: Optional[ExtendedEmailMatchingParam]
    """Extended e-mail matching settings."""

    fips: Optional[FipsSettingsParam]
    """FIPS settings."""

    host_selector: Optional[HostSelector]
    """Setting to enable host selector in egress policies."""

    protocol_detection: Optional[ProtocolDetectionParam]
    """Protocol Detection settings."""

    sandbox: Optional[Sandbox]
    """Sandbox settings."""

    tls_decrypt: Optional[TLSSettingsParam]
    """TLS interception settings."""
