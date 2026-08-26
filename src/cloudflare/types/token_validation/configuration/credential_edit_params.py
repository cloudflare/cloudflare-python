# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CredentialEditParams",
    "Key",
    "KeyAPIShieldCredentialsJWTKeyRSA",
    "KeyAPIShieldCredentialsJWTKeyEcEs256",
    "KeyAPIShieldCredentialsJWTKeyEcEs384",
    "KeyAPIShieldCredentialsJWTKeyOctPatchRequest",
]


class CredentialEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    keys: Required[Iterable[Key]]


class KeyAPIShieldCredentialsJWTKeyRSA(TypedDict, total=False):
    """JSON representation of an RSA key."""

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


class KeyAPIShieldCredentialsJWTKeyEcEs256(TypedDict, total=False):
    """JSON representation of an ES256 key"""

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


class KeyAPIShieldCredentialsJWTKeyEcEs384(TypedDict, total=False):
    """JSON representation of an ES384 key"""

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


class KeyAPIShieldCredentialsJWTKeyOctPatchRequest(TypedDict, total=False):
    """JSON representation of a symmetric key for PATCH requests."""

    alg: Required[Literal["HS256", "HS384", "HS512"]]
    """Algorithm"""

    kid: Required[str]
    """Key ID"""

    kty: Required[Literal["oct"]]
    """Key Type"""

    k: str
    """Symmetric key material.

    Optional for PATCH: omit to preserve existing secret for matching `{alg,kid}`;
    send a string to rotate. `k: null` is invalid.
    """


Key: TypeAlias = Union[
    KeyAPIShieldCredentialsJWTKeyRSA,
    KeyAPIShieldCredentialsJWTKeyEcEs256,
    KeyAPIShieldCredentialsJWTKeyEcEs384,
    KeyAPIShieldCredentialsJWTKeyOctPatchRequest,
]
