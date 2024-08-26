# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal, TypeAlias

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Configuration", "AuthIDCharacteristic", "AuthIDCharacteristicAPIShieldAuthIDCharacteristic", "AuthIDCharacteristicAPIShieldAuthIDCharacteristicJwtClaim"]

class AuthIDCharacteristicAPIShieldAuthIDCharacteristic(BaseModel):
    name: str
    """The name of the characteristic field, i.e., the header or cookie name."""

    type: Literal["header", "cookie"]
    """The type of characteristic."""

class AuthIDCharacteristicAPIShieldAuthIDCharacteristicJwtClaim(BaseModel):
    name: str
    """
    Claim location expressed as `$(token_config_id):$(json_path)`, where
    `token_config_id` is the ID of the token configuration used in validating the
    JWT, and `json_path` is a RFC 9535 JSONPath
    (https://goessner.net/articles/JsonPath/,
    https://www.rfc-editor.org/rfc/rfc9535.html). The JSONPath expression may be in
    dot or bracket notation, may only specify literal keys or array indexes, and
    must return a singleton value, which will be interpreted as a string.
    """

    type: Literal["jwt"]
    """The type of characteristic."""

AuthIDCharacteristic: TypeAlias = Union[AuthIDCharacteristicAPIShieldAuthIDCharacteristic, AuthIDCharacteristicAPIShieldAuthIDCharacteristicJwtClaim]

class Configuration(BaseModel):
    auth_id_characteristics: List[AuthIDCharacteristic]