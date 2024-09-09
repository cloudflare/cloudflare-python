# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .dns_setting_param import DNSSettingParam

__all__ = ["SettingEditParams"]


class SettingEditParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    zone_defaults: DNSSettingParam
