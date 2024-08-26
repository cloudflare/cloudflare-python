# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MTLSCERTBinding"]


class MTLSCERTBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["mtls_certificate"]
    """The class of resource that the binding provides."""

    certificate_id: Optional[str] = None
    """ID of the certificate to bind to"""
