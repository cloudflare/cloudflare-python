# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse",
    "AuthIDCharacteristic",
]


class AuthIDCharacteristic(BaseModel):
    name: str
    """The name of the characteristic field, i.e., the header or cookie name."""

    type: Literal["header", "cookie"]
    """The type of characteristic."""


class ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse(BaseModel):
    auth_id_characteristics: Optional[List[AuthIDCharacteristic]] = None
