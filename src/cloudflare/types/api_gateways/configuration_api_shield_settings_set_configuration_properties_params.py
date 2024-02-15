# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ConfigurationAPIShieldSettingsSetConfigurationPropertiesParams", "AuthIDCharacteristic"]


class ConfigurationAPIShieldSettingsSetConfigurationPropertiesParams(TypedDict, total=False):
    auth_id_characteristics: Iterable[AuthIDCharacteristic]


class AuthIDCharacteristic(TypedDict, total=False):
    name: Required[str]
    """The name of the characteristic field, i.e., the header or cookie name."""

    type: Required[Literal["header", "cookie"]]
    """The type of characteristic."""
