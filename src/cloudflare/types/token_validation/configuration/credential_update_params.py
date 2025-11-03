# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["CredentialUpdateParams", "Key", "KeyAPIShieldCredentialsJWTKeyEc", "KeyAPIShieldCredentialsJWTKeyRSA"]


class CredentialUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    keys: Iterable[Key]


class KeyAPIShieldCredentialsJWTKeyEc(TypedDict, total=False):
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


class KeyAPIShieldCredentialsJWTKeyRSA(TypedDict, total=False):
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


Key: TypeAlias = Union[KeyAPIShieldCredentialsJWTKeyEc, KeyAPIShieldCredentialsJWTKeyRSA]
