# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "TokenConfig",
    "Credentials",
    "CredentialsKey",
    "CredentialsKeyAPIShieldCredentialsJWTKeyEc",
    "CredentialsKeyAPIShieldCredentialsJWTKeyRSA",
]


class CredentialsKeyAPIShieldCredentialsJWTKeyEc(BaseModel):
    alg: Literal["ES256", "ES384"]
    """Algorithm"""

    kid: str
    """Key ID"""

    kty: Literal["EC"]
    """Key Type"""

    x: str
    """X EC coordinate"""

    y: str
    """Y EC coordinate"""


class CredentialsKeyAPIShieldCredentialsJWTKeyRSA(BaseModel):
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


CredentialsKey: TypeAlias = Union[
    CredentialsKeyAPIShieldCredentialsJWTKeyEc, CredentialsKeyAPIShieldCredentialsJWTKeyRSA
]


class Credentials(BaseModel):
    keys: Optional[List[CredentialsKey]] = None


class TokenConfig(BaseModel):
    id: Optional[str] = None
    """UUID."""

    created_at: Optional[datetime] = None

    credentials: Optional[Credentials] = None

    description: Optional[str] = None

    last_updated: Optional[datetime] = None

    title: Optional[str] = None

    token_sources: Optional[List[str]] = None

    token_type: Optional[Literal["JWT"]] = None
