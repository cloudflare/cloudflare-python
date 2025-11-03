# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "ConfigurationCreateParams",
    "Credentials",
    "CredentialsKey",
    "CredentialsKeyAPIShieldCredentialsJWTKeyEc",
    "CredentialsKeyAPIShieldCredentialsJWTKeyRSA",
]


class ConfigurationCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    credentials: Required[Credentials]

    description: Required[str]

    title: Required[str]

    token_sources: Required[SequenceNotStr[str]]

    token_type: Required[Literal["JWT"]]


class CredentialsKeyAPIShieldCredentialsJWTKeyEc(TypedDict, total=False):
    alg: Required[Literal["ES256", "ES384"]]
    """Algorithm"""

    kid: Required[str]
    """Key ID"""

    kty: Required[Literal["EC"]]
    """Key Type"""

    x: Required[str]
    """X EC coordinate"""

    y: Required[str]
    """Y EC coordinate"""


class CredentialsKeyAPIShieldCredentialsJWTKeyRSA(TypedDict, total=False):
    alg: Required[Literal["RS256", "RS384", "RS512", "PS256", "PS384", "PS512"]]
    """Algorithm"""

    e: Required[str]
    """RSA exponent"""

    kid: Required[str]
    """Key ID"""

    kty: Required[Literal["RSA"]]
    """Key Type"""

    n: Required[str]
    """RSA modulus"""


CredentialsKey: TypeAlias = Union[
    CredentialsKeyAPIShieldCredentialsJWTKeyEc, CredentialsKeyAPIShieldCredentialsJWTKeyRSA
]


class Credentials(TypedDict, total=False):
    keys: Iterable[CredentialsKey]
