# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .access_settings_param import AccessSettingsParam

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    settings: Required[Iterable[AccessSettingsParam]]

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""
