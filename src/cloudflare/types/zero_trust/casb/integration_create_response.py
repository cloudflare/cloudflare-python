# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["IntegrationCreateResponse", "AuthorizationLink"]


class AuthorizationLink(BaseModel):
    """Authorization link for the integration."""

    components: Optional[Dict[str, object]] = None

    link: Optional[str] = None


class IntegrationCreateResponse(BaseModel):
    """Serializer for v2 integration detail response with use cases."""

    id: str
    """Integration ID."""

    application: Dict[str, Optional[str]]

    auth_method: Optional[Dict[str, str]] = None
    """The integration's authentication method."""

    authorization_link: Optional[AuthorizationLink] = None
    """Authorization link for the integration."""

    created: datetime
    """When the integration was created."""

    credentials_expiry: datetime
    """Credentials expiry time."""

    dlp_profiles: List[str]
    """DLP Profiles enabled for the integration."""

    health_details: List[Dict[str, object]]
    """Health details with remediation hints."""

    is_paused: bool
    """Whether the user paused the integration."""

    last_hydrated: datetime
    """Last time the integration was hydrated."""

    name: str
    """Name of the integration."""

    organization_id: int
    """Organization ID."""

    status: str
    """Integration status."""

    updated: datetime
    """When the integration was last updated."""

    use_cases: List[Dict[str, object]]
    """Use cases enabled for the integration."""
