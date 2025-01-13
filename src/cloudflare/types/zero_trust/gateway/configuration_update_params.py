# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .gateway_configuration_settings_param import GatewayConfigurationSettingsParam

__all__ = ["ConfigurationUpdateParams"]


class ConfigurationUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    settings: GatewayConfigurationSettingsParam
    """Account settings"""
