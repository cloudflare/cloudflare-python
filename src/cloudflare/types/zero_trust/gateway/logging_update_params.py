# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = [
    "LoggingUpdateParams",
    "SettingsByRuleType",
    "SettingsByRuleTypeDNS",
    "SettingsByRuleTypeHTTP",
    "SettingsByRuleTypeL4",
]


class LoggingUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    redact_pii: bool
    """
    Indicate whether to redact personally identifiable information from activity
    logging (PII fields include source IP, user email, user ID, device ID, URL,
    referrer, and user agent).
    """

    settings_by_rule_type: SettingsByRuleType
    """Configure logging settings for each rule type."""


class SettingsByRuleTypeDNS(TypedDict, total=False):
    """Configure logging settings for DNS firewall."""

    log_all: bool
    """Specify whether to log all requests to this service."""

    log_blocks: bool
    """Specify whether to log only blocking requests to this service."""


class SettingsByRuleTypeHTTP(TypedDict, total=False):
    """Configure logging settings for HTTP/HTTPS firewall."""

    log_all: bool
    """Specify whether to log all requests to this service."""

    log_blocks: bool
    """Specify whether to log only blocking requests to this service."""


class SettingsByRuleTypeL4(TypedDict, total=False):
    """Configure logging settings for Network firewall."""

    log_all: bool
    """Specify whether to log all requests to this service."""

    log_blocks: bool
    """Specify whether to log only blocking requests to this service."""


class SettingsByRuleType(TypedDict, total=False):
    """Configure logging settings for each rule type."""

    dns: SettingsByRuleTypeDNS
    """Configure logging settings for DNS firewall."""

    http: SettingsByRuleTypeHTTP
    """Configure logging settings for HTTP/HTTPS firewall."""

    l4: SettingsByRuleTypeL4
    """Configure logging settings for Network firewall."""
