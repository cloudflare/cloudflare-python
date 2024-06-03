# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypedDict

__all__ = [
    "AppConfigurationUpdateParams",
    "ChangeBreakoutBehavior",
    "ChangePriority",
    "UpdateAccountAppID",
    "UpdateManagedAppID",
    "AccountAppManagedApp",
    "ManagedAppAccountApp",
]


class ChangeBreakoutBehavior(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    body: Required[object]


class ChangePriority(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    body: Required[object]


class UpdateAccountAppID(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    account_app_id: Required[str]
    """Magic account app ID."""


class UpdateManagedAppID(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    managed_app_id: Required[str]
    """Managed app ID."""


class AccountAppManagedApp(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    account_app_id: Required[str]
    """Magic account app ID."""

    managed_app_id: Required[Optional[str]]
    """**Must be set to null**"""


class ManagedAppAccountApp(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    account_app_id: Required[Optional[str]]
    """**Must be set to null**"""

    managed_app_id: Required[str]
    """Managed app ID."""


AppConfigurationUpdateParams = Union[
    ChangeBreakoutBehavior,
    ChangePriority,
    UpdateAccountAppID,
    UpdateManagedAppID,
    AccountAppManagedApp,
    ManagedAppAccountApp,
]
