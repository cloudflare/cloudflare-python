# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["IdPFederationGrantDeleteResponse"]


class IdPFederationGrantDeleteResponse(BaseModel):
    id: Optional[str] = None
    """UID of the deleted IdP federation grant."""
