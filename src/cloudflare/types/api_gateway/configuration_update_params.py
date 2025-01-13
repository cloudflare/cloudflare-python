# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ConfigurationUpdateParams",
    "AuthIDCharacteristic",
    "AuthIDCharacteristicAPIShieldAuthIDCharacteristic",
    "AuthIDCharacteristicAPIShieldAuthIDCharacteristicJWTClaim",
]


class ConfigurationUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    auth_id_characteristics: Required[Iterable[AuthIDCharacteristic]]


class AuthIDCharacteristicAPIShieldAuthIDCharacteristic(TypedDict, total=False):
    name: Required[str]
    """The name of the characteristic field, i.e., the header or cookie name."""

    type: Required[Literal["header", "cookie"]]
    """The type of characteristic."""


class AuthIDCharacteristicAPIShieldAuthIDCharacteristicJWTClaim(TypedDict, total=False):
    name: Required[str]
    """
    Claim location expressed as `$(token_config_id):$(json_path)`, where
    `token_config_id` is the ID of the token configuration used in validating the
    JWT, and `json_path` is a RFC 9535 JSONPath
    (https://goessner.net/articles/JsonPath/,
    https://www.rfc-editor.org/rfc/rfc9535.html). The JSONPath expression may be in
    dot or bracket notation, may only specify literal keys or array indexes, and
    must return a singleton value, which will be interpreted as a string.
    """

    type: Required[Literal["jwt"]]
    """The type of characteristic."""


AuthIDCharacteristic: TypeAlias = Union[
    AuthIDCharacteristicAPIShieldAuthIDCharacteristic, AuthIDCharacteristicAPIShieldAuthIDCharacteristicJWTClaim
]
