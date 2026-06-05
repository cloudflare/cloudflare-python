# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["IdPFederationGrant"]


class IdPFederationGrant(BaseModel):
    id: str
    """UID of the IdP federation grant."""

    created_at: datetime
    """When the grant was created."""

    idp_id: str
    """UID of the identity provider being federated."""
