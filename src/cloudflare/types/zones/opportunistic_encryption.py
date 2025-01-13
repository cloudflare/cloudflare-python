# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OpportunisticEncryption"]


class OpportunisticEncryption(BaseModel):
    id: Optional[Literal["opportunistic_encryption"]] = None
    """
    Opportunistic Encryption allows browsers to access HTTP URIs over an encrypted
    TLS channel. It's not a substitute for HTTPS, but provides additional security
    for otherwise vulnerable requests.
    """

    value: Optional[Literal["on", "off"]] = None
    """The status of Opportunistic Encryption."""
