# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConfigurationAPIShieldSettingsSetConfigurationPropertiesParams", "AuthIDCharacteristic"]


class ConfigurationAPIShieldSettingsSetConfigurationPropertiesParams(TypedDict, total=False):
    auth_id_characteristics: Iterable[AuthIDCharacteristic]


class AuthIDCharacteristic(TypedDict, total=False):
    name: Required[str]
    """The name of the characteristic field, i.e., the header or cookie name."""

    type: Required[Literal["header", "cookie"]]
    """The type of characteristic."""
