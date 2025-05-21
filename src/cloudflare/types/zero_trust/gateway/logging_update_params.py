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
    Redact personally identifiable information from activity logging (PII fields
    are: source IP, user email, user ID, device ID, URL, referrer, user agent).
    """

    settings_by_rule_type: SettingsByRuleType
    """Logging settings by rule type."""


class SettingsByRuleTypeDNS(TypedDict, total=False):
    log_all: bool
    """Log all requests to this service."""

    log_blocks: bool
    """Log only blocking requests to this service."""


class SettingsByRuleTypeHTTP(TypedDict, total=False):
    log_all: bool
    """Log all requests to this service."""

    log_blocks: bool
    """Log only blocking requests to this service."""


class SettingsByRuleTypeL4(TypedDict, total=False):
    log_all: bool
    """Log all requests to this service."""

    log_blocks: bool
    """Log only blocking requests to this service."""


class SettingsByRuleType(TypedDict, total=False):
    dns: SettingsByRuleTypeDNS

    http: SettingsByRuleTypeHTTP

    l4: SettingsByRuleTypeL4
