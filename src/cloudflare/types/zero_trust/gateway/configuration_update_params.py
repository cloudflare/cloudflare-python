# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from .gateway_configuration_settings_param import GatewayConfigurationSettingsParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ConfigurationUpdateParams"]


class ConfigurationUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    settings: GatewayConfigurationSettingsParam
    """account settings."""
