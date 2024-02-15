# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesParams"]


class ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesParams(TypedDict, total=False):
    properties: List[Literal["auth_id_characteristics"]]
    """Requests information about certain properties."""
