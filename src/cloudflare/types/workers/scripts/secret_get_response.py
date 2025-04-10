# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = ["SecretGetResponse", "WorkersBindingKindSecretText", "WorkersBindingKindSecretKey"]


class WorkersBindingKindSecretText(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["secret_text"]
    """The kind of resource that the binding provides."""


class WorkersBindingKindSecretKey(BaseModel):
    algorithm: object
    """
    Algorithm-specific key parameters
    ([learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm)).
    """

    format: Literal["raw", "pkcs8", "spki", "jwk"]
    """
    Data format of the key
    ([learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format)).
    """

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["secret_key"]
    """The kind of resource that the binding provides."""

    usages: List[Literal["encrypt", "decrypt", "sign", "verify", "deriveKey", "deriveBits", "wrapKey", "unwrapKey"]]
    """
    Allowed operations with the key
    ([learn more](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages)).
    """


SecretGetResponse: TypeAlias = Annotated[
    Union[WorkersBindingKindSecretText, WorkersBindingKindSecretKey], PropertyInfo(discriminator="type")
]
