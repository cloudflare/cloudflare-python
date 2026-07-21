# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from ....._models import BaseModel

__all__ = ["AuthMethodListResponse", "AuthMethodListResponseItem", "AuthMethodListResponseItemInstructions"]


class AuthMethodListResponseItemInstructions(BaseModel):
    """Step-by-step instructions for obtaining credentials."""

    markdown: str
    """Detailed instructions in markdown format."""


class AuthMethodListResponseItem(BaseModel):
    """Detailed auth method info including credentials schema and instructions."""

    id: str
    """Auth method identifier."""

    display_name: str
    """Human-readable auth method name."""

    human_interaction_required: bool
    """
    Whether setup requires human interaction or integration can be created purely
    using API (e.g., For OAuth can not be created without user interaction).
    """

    instructions: AuthMethodListResponseItemInstructions
    """Step-by-step instructions for obtaining credentials."""

    payload_example: Optional[Dict[str, object]] = None
    """Example credentials payload with placeholder values."""

    payload_schema: Optional[Dict[str, object]] = None
    """JSON Schema for the credentials object in POST /v2/integrations request."""

    redirect_url: Optional[str] = None
    """OAuth redirect URL for vendors requiring human interaction."""


AuthMethodListResponse: TypeAlias = List[AuthMethodListResponseItem]
