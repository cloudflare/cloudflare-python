# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["AuthenticatorCatalogListResponse"]


class AuthenticatorCatalogListResponse(BaseModel):
    """A FIDO2 authenticator device AAGUID entry"""

    aaguid: str
    """
    The Authenticator Attestation GUID (AAGUID) uniquely identifying a FIDO2
    authenticator model
    """

    name: str
    """The human-readable name of the FIDO2 authenticator"""
