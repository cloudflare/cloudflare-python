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

__all__ = ["GatewayConfigurationSettings", "Certificate", "HostSelector", "Inspection", "Sandbox"]


class Certificate(BaseModel):
    id: str
    """Specify the UUID of the certificate used for interception.

    Ensure the certificate is available at the edge(previously called 'active'). A
    nil UUID directs Cloudflare to use the Root CA.
    """


class HostSelector(BaseModel):
    enabled: Optional[bool] = None
    """Specify whether to enable filtering via hosts for egress policies."""


class Inspection(BaseModel):
    mode: Optional[Literal["static", "dynamic"]] = None
    """Define the proxy inspection mode.

    1. static: Gateway applies static inspection to HTTP on TCP(80). With TLS
       decryption on, Gateway inspects HTTPS traffic on TCP(443) and UDP(443). 2.
       dynamic: Gateway applies protocol detection to inspect HTTP and HTTPS traffic
       on any port. TLS decryption must remain on to inspect HTTPS traffic.
    """


class Sandbox(BaseModel):
    enabled: Optional[bool] = None
    """Specify whether to enable the sandbox."""

    fallback_action: Optional[Literal["allow", "block"]] = None
    """Specify the action to take when the system cannot scan the file."""


class GatewayConfigurationSettings(BaseModel):
    activity_log: Optional[ActivityLogSettings] = None
    """Specify activity log settings."""

    antivirus: Optional[AntiVirusSettings] = None
    """Specify anti-virus settings."""

    block_page: Optional[BlockPageSettings] = None
    """Specify block page layout settings."""

    body_scanning: Optional[BodyScanningSettings] = None
    """Specify the DLP inspection mode."""

    browser_isolation: Optional[BrowserIsolationSettings] = None
    """Specify Clientless Browser Isolation settings."""

    certificate: Optional[Certificate] = None
    """Specify certificate settings for Gateway TLS interception.

    If unset, the Cloudflare Root CA handles interception.
    """

    custom_certificate: Optional[CustomCertificateSettings] = None
    """Specify custom certificate settings for BYO-PKI.

    This field is deprecated; use `certificate` instead.
    """

    extended_email_matching: Optional[ExtendedEmailMatching] = None
    """Configures user email settings for firewall policies.

    When you enable this, the system standardizes email addresses in the identity
    portion of the rule to match extended email variants in firewall policies. When
    you disable this setting, the system matches email addresses exactly as you
    provide them. Enable this setting if your email uses `.` or `+` modifiers.
    """

    fips: Optional[FipsSettings] = None
    """Specify FIPS settings."""

    host_selector: Optional[HostSelector] = None
    """Enable host selection in egress policies."""

    inspection: Optional[Inspection] = None
    """Define the proxy inspection mode."""

    protocol_detection: Optional[ProtocolDetection] = None
    """Specify whether to detect protocols from the initial bytes of client traffic."""

    sandbox: Optional[Sandbox] = None
    """Specify whether to enable the sandbox."""

    tls_decrypt: Optional[TLSSettings] = None
    """Specify whether to inspect encrypted HTTP traffic."""
