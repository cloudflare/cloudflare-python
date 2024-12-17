# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["GatewayCAListResponse"]


class GatewayCAListResponse(BaseModel):
    id: Optional[str] = None
    """The key ID of this certificate."""

    public_key: Optional[str] = None
    """The public key of this certificate."""
