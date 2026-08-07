# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["IntegrationListResponse"]


class IntegrationListResponse(BaseModel):
    """Serializer for v2 integration list responses."""

    id: str
    """Integration ID."""

    application: Dict[str, Optional[str]]

    created: datetime
    """When the integration was created."""

    is_paused: bool
    """Whether the user paused the integration."""

    name: str
    """Name of the integration."""

    status: str
    """Integration status."""

    updated: datetime
    """When the integration was last updated."""
