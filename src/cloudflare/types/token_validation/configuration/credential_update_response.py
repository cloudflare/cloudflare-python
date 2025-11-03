# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from ...api_gateway.message import Message

__all__ = ["CredentialUpdateResponse", "Key", "KeyAPIShieldCredentialsJWTKeyEc", "KeyAPIShieldCredentialsJWTKeyRSA"]


class KeyAPIShieldCredentialsJWTKeyEc(BaseModel):
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


class KeyAPIShieldCredentialsJWTKeyRSA(BaseModel):
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


Key: TypeAlias = Union[KeyAPIShieldCredentialsJWTKeyEc, KeyAPIShieldCredentialsJWTKeyRSA]


class CredentialUpdateResponse(BaseModel):
    errors: Message

    messages: Message

    success: Literal[True]
    """Whether the API call was successful."""

    keys: Optional[List[Key]] = None
