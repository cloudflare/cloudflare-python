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
    log_all: Optional[bool] = None
    """Log all requests to this service."""

    log_blocks: Optional[bool] = None
    """Log only blocking requests to this service."""


class SettingsByRuleTypeHTTP(BaseModel):
    log_all: Optional[bool] = None
    """Log all requests to this service."""

    log_blocks: Optional[bool] = None
    """Log only blocking requests to this service."""


class SettingsByRuleTypeL4(BaseModel):
    log_all: Optional[bool] = None
    """Log all requests to this service."""

    log_blocks: Optional[bool] = None
    """Log only blocking requests to this service."""


class SettingsByRuleType(BaseModel):
    dns: Optional[SettingsByRuleTypeDNS] = None

    http: Optional[SettingsByRuleTypeHTTP] = None

    l4: Optional[SettingsByRuleTypeL4] = None


class LoggingSetting(BaseModel):
    redact_pii: Optional[bool] = None
    """
    Redact personally identifiable information from activity logging (PII fields
    are: source IP, user email, user ID, device ID, URL, referrer, user agent).
    """

    settings_by_rule_type: Optional[SettingsByRuleType] = None
    """Logging settings by rule type."""
