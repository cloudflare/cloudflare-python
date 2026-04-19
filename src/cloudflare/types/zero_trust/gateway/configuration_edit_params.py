# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .gateway_configuration_settings_param import GatewayConfigurationSettingsParam

__all__ = ["ConfigurationEditParams"]


class ConfigurationEditParams(TypedDict, total=False):
    account_id: str

    settings: GatewayConfigurationSettingsParam
    """Specify account settings."""
