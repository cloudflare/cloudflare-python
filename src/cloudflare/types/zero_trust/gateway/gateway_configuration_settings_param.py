# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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

__all__ = ["GatewayConfigurationSettingsParam", "Certificate", "HostSelector", "Inspection", "Sandbox"]


class Certificate(TypedDict, total=False):
    id: Required[str]
    """Specify the UUID of the certificate used for interception.

    Ensure the certificate is available at the edge(previously called 'active'). A
    nil UUID directs Cloudflare to use the Root CA.
    """


class HostSelector(TypedDict, total=False):
    enabled: Optional[bool]
    """Specify whether to enable filtering via hosts for egress policies."""


class Inspection(TypedDict, total=False):
    mode: Literal["static", "dynamic"]
    """Define the proxy inspection mode.

    1. static: Gateway applies static inspection to HTTP on TCP(80). With TLS
       decryption on, Gateway inspects HTTPS traffic on TCP(443) and UDP(443). 2.
       dynamic: Gateway applies protocol detection to inspect HTTP and HTTPS traffic
       on any port. TLS decryption must remain on to inspect HTTPS traffic.
    """


class Sandbox(TypedDict, total=False):
    enabled: Optional[bool]
    """Specify whether to enable the sandbox."""

    fallback_action: Literal["allow", "block"]
    """Specify the action to take when the system cannot scan the file."""


class GatewayConfigurationSettingsParam(TypedDict, total=False):
    activity_log: Optional[ActivityLogSettingsParam]
    """Specify activity log settings."""

    antivirus: Optional[AntiVirusSettingsParam]
    """Specify anti-virus settings."""

    block_page: Optional[BlockPageSettingsParam]
    """Specify block page layout settings."""

    body_scanning: Optional[BodyScanningSettingsParam]
    """Specify the DLP inspection mode."""

    browser_isolation: Optional[BrowserIsolationSettingsParam]
    """Specify Clientless Browser Isolation settings."""

    certificate: Optional[Certificate]
    """Specify certificate settings for Gateway TLS interception.

    If unset, the Cloudflare Root CA handles interception.
    """

    custom_certificate: Optional[CustomCertificateSettingsParam]
    """Specify custom certificate settings for BYO-PKI.

    This field is deprecated; use `certificate` instead.
    """

    extended_email_matching: Optional[ExtendedEmailMatchingParam]
    """Specify user email settings for the firewall policies.

    When this is enabled, we standardize the email addresses in the identity part of
    the rule, so that they match the extended email variants in the firewall
    policies. When this setting is turned off, the email addresses in the identity
    part of the rule will be matched exactly as provided. If your email has `.` or
    `+` modifiers, you should enable this setting.
    """

    fips: Optional[FipsSettingsParam]
    """Specify FIPS settings."""

    host_selector: Optional[HostSelector]
    """Enable host selection in egress policies."""

    inspection: Optional[Inspection]
    """Define the proxy inspection mode."""

    protocol_detection: Optional[ProtocolDetectionParam]
    """Specify whether to detect protocols from the initial bytes of client traffic."""

    sandbox: Optional[Sandbox]
    """Specify whether to enable the sandbox."""

    tls_decrypt: Optional[TLSSettingsParam]
    """Specify whether to inspect encrypted HTTP traffic."""
