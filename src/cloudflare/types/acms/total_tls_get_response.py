# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TotalTLSGetResponse"]


class TotalTLSGetResponse(BaseModel):
    certificate_authority: Optional[Literal["google", "lets_encrypt"]] = None
    """The Certificate Authority that Total TLS certificates will be issued through."""

    enabled: Optional[bool] = None
    """
    If enabled, Total TLS will order a hostname specific TLS certificate for any
    proxied A, AAAA, or CNAME record in your zone.
    """

    validity_days: Optional[Literal[90]] = None
    """The validity period in days for the certificates ordered via Total TLS."""
