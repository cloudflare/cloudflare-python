# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["IdPFederationGrant"]


class IdPFederationGrant(BaseModel):
    id: str
    """UID of the IdP federation grant."""

    idp_id: str
    """UID of the identity provider being federated."""
