# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MTLSCERTBinding"]


class MTLSCERTBinding(BaseModel):
    certificate_id: str
    """ID of the certificate to bind to"""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["mtls_certificate"]
    """The class of resource that the binding provides."""
