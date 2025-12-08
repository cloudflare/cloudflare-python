# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from ...api_gateway.message import Message

__all__ = [
    "CredentialUpdateResponse",
    "Key",
    "KeyAPIShieldCredentialsJWTKeyRSA",
    "KeyAPIShieldCredentialsJWTKeyEcEs256",
    "KeyAPIShieldCredentialsJWTKeyEcEs384",
]


class KeyAPIShieldCredentialsJWTKeyRSA(BaseModel):
    """JSON representation of an RSA key."""

    alg: Literal["RS256", "RS384", "RS512", "PS256", "PS384", "PS512"]
    """Algorithm"""

    e: str
    """RSA exponent"""

    kid: str
    """Key ID"""

    kty: Literal["RSA"]
    """Key Type"""

    n: str
    """RSA modulus"""


class KeyAPIShieldCredentialsJWTKeyEcEs256(BaseModel):
    """JSON representation of an ES256 key"""

    alg: Literal["ES256"]
    """Algorithm"""

    crv: Literal["P-256"]
    """Curve"""

    kid: str
    """Key ID"""

    kty: Literal["EC"]
    """Key Type"""

    x: str
    """X EC coordinate"""

    y: str
    """Y EC coordinate"""


class KeyAPIShieldCredentialsJWTKeyEcEs384(BaseModel):
    """JSON representation of an ES384 key"""

    alg: Literal["ES384"]
    """Algorithm"""

    crv: Literal["P-384"]
    """Curve"""

    kid: str
    """Key ID"""

    kty: Literal["EC"]
    """Key Type"""

    x: str
    """X EC coordinate"""

    y: str
    """Y EC coordinate"""


Key: TypeAlias = Union[
    KeyAPIShieldCredentialsJWTKeyRSA, KeyAPIShieldCredentialsJWTKeyEcEs256, KeyAPIShieldCredentialsJWTKeyEcEs384
]


class CredentialUpdateResponse(BaseModel):
    errors: Message

    keys: List[Key]

    messages: Message

    success: Literal[True]
    """Whether the API call was successful."""
