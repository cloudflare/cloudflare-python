# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["AppConfigurationCreateParams", "AccountApp", "ManagedApp"]


class AccountApp(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    account_app_id: Required[str]
    """Magic account app ID."""


class ManagedApp(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    managed_app_id: Required[str]
    """Managed app ID."""


AppConfigurationCreateParams = Union[AccountApp, ManagedApp]
