# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

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
