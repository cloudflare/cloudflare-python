# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LoggingUpdateParams", "SettingsByRuleType"]


class LoggingUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    redact_pii: bool
    """
    Redact personally identifiable information from activity logging (PII fields
    are: source IP, user email, user ID, device ID, URL, referrer, user agent).
    """

    settings_by_rule_type: SettingsByRuleType
    """Logging settings by rule type."""


class SettingsByRuleType(TypedDict, total=False):
    dns: object
    """Logging settings for DNS firewall."""

    http: object
    """Logging settings for HTTP/HTTPS firewall."""

    l4: object
    """Logging settings for Network firewall."""
