# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "ConfigurationCreateParams",
    "Credentials",
    "CredentialsKey",
    "CredentialsKeyAPIShieldCredentialsJWTKeyRSA",
    "CredentialsKeyAPIShieldCredentialsJWTKeyEcEs256",
    "CredentialsKeyAPIShieldCredentialsJWTKeyEcEs384",
]


class ConfigurationCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    credentials: Required[Credentials]

    description: Required[str]

    title: Required[str]

    token_sources: Required[SequenceNotStr[str]]

    token_type: Required[Literal["JWT"]]


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


class CredentialsKeyAPIShieldCredentialsJWTKeyEcEs256(TypedDict, total=False):
    alg: Required[Literal["ES256"]]
    """Algorithm"""

    crv: Required[Literal["P-256"]]
    """Curve"""

    kid: Required[str]
    """Key ID"""

    kty: Required[Literal["EC"]]
    """Key Type"""

    x: Required[str]
    """X EC coordinate"""

    y: Required[str]
    """Y EC coordinate"""


class CredentialsKeyAPIShieldCredentialsJWTKeyEcEs384(TypedDict, total=False):
    alg: Required[Literal["ES384"]]
    """Algorithm"""

    crv: Required[Literal["P-384"]]
    """Curve"""

    kid: Required[str]
    """Key ID"""

    kty: Required[Literal["EC"]]
    """Key Type"""

    x: Required[str]
    """X EC coordinate"""

    y: Required[str]
    """Y EC coordinate"""


CredentialsKey: TypeAlias = Union[
    CredentialsKeyAPIShieldCredentialsJWTKeyRSA,
    CredentialsKeyAPIShieldCredentialsJWTKeyEcEs256,
    CredentialsKeyAPIShieldCredentialsJWTKeyEcEs384,
]


class Credentials(TypedDict, total=False):
    keys: Required[Iterable[CredentialsKey]]
