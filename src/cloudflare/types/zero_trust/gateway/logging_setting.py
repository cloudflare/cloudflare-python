# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["LoggingSetting", "SettingsByRuleType"]


class SettingsByRuleType(BaseModel):
    dns: Optional[object] = None
    """Logging settings for DNS firewall."""

    http: Optional[object] = None
    """Logging settings for HTTP/HTTPS firewall."""

    l4: Optional[object] = None
    """Logging settings for Network firewall."""


class LoggingSetting(BaseModel):
    redact_pii: Optional[bool] = None
    """
    Redact personally identifiable information from activity logging (PII fields
    are: source IP, user email, user ID, device ID, URL, referrer, user agent).
    """

    settings_by_rule_type: Optional[SettingsByRuleType] = None
    """Logging settings by rule type."""
