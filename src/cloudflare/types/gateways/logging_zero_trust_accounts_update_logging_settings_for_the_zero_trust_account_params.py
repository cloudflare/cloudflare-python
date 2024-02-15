# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountParams", "SettingsByRuleType"]


class LoggingZeroTrustAccountsUpdateLoggingSettingsForTheZeroTrustAccountParams(TypedDict, total=False):
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
