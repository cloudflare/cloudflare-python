# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = [
    "LoggingSetting",
    "SettingsByRuleType",
    "SettingsByRuleTypeDNS",
    "SettingsByRuleTypeHTTP",
    "SettingsByRuleTypeL4",
]


class SettingsByRuleTypeDNS(BaseModel):
    """Configure logging settings for DNS firewall."""

    log_all: Optional[bool] = None
    """Specify whether to log all requests to this service."""

    log_blocks: Optional[bool] = None
    """Specify whether to log only blocking requests to this service."""


class SettingsByRuleTypeHTTP(BaseModel):
    """Configure logging settings for HTTP/HTTPS firewall."""

    log_all: Optional[bool] = None
    """Specify whether to log all requests to this service."""

    log_blocks: Optional[bool] = None
    """Specify whether to log only blocking requests to this service."""


class SettingsByRuleTypeL4(BaseModel):
    """Configure logging settings for Network firewall."""

    log_all: Optional[bool] = None
    """Specify whether to log all requests to this service."""

    log_blocks: Optional[bool] = None
    """Specify whether to log only blocking requests to this service."""


class SettingsByRuleType(BaseModel):
    """Configure logging settings for each rule type."""

    dns: Optional[SettingsByRuleTypeDNS] = None
    """Configure logging settings for DNS firewall."""

    http: Optional[SettingsByRuleTypeHTTP] = None
    """Configure logging settings for HTTP/HTTPS firewall."""

    l4: Optional[SettingsByRuleTypeL4] = None
    """Configure logging settings for Network firewall."""


class LoggingSetting(BaseModel):
    redact_pii: Optional[bool] = None
    """
    Indicate whether to redact personally identifiable information from activity
    logging (PII fields include source IP, user email, user ID, device ID, URL,
    referrer, and user agent).
    """

    settings_by_rule_type: Optional[SettingsByRuleType] = None
    """Configure logging settings for each rule type."""
