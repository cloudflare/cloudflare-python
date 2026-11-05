# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["IntegrationListResponse", "AuthMethod"]


class AuthMethod(BaseModel):
    """The integration's authentication method."""

    id: str

    display_name: str


class IntegrationListResponse(BaseModel):
    """Serializer for v2 integration list responses."""

    id: str
    """Integration ID."""

    application: Dict[str, Optional[str]]

    auth_method: Optional[AuthMethod] = None
    """The integration's authentication method."""

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

    use_cases: List[str]
    """Use cases enabled for the integration."""
