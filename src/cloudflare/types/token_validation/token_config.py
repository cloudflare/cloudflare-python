# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "TokenConfig",
    "Credentials",
    "CredentialsKey",
    "CredentialsKeyAPIShieldCredentialsJWTKeyRSA",
    "CredentialsKeyAPIShieldCredentialsJWTKeyEcEs256",
    "CredentialsKeyAPIShieldCredentialsJWTKeyEcEs384",
]


class CredentialsKeyAPIShieldCredentialsJWTKeyRSA(BaseModel):
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


class CredentialsKeyAPIShieldCredentialsJWTKeyEcEs256(BaseModel):
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


class CredentialsKeyAPIShieldCredentialsJWTKeyEcEs384(BaseModel):
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


CredentialsKey: TypeAlias = Union[
    CredentialsKeyAPIShieldCredentialsJWTKeyRSA,
    CredentialsKeyAPIShieldCredentialsJWTKeyEcEs256,
    CredentialsKeyAPIShieldCredentialsJWTKeyEcEs384,
]


class Credentials(BaseModel):
    keys: List[CredentialsKey]


class TokenConfig(BaseModel):
    id: str
    """UUID."""

    created_at: datetime

    credentials: Credentials

    description: str

    last_updated: datetime

    title: str

    token_sources: List[str]

    token_type: Literal["JWT"]
