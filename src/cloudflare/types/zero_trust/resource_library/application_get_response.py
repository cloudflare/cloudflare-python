# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ApplicationGetResponse"]


class ApplicationGetResponse(BaseModel):
    id: str
    """Returns the application ID."""

    application_confidence_score: float
    """Confidence score for the application. Returns -1 when no score is available."""

    application_source: str
    """Returns the application source."""

    application_type: str
    """Returns the application type."""

    application_type_description: str
    """Returns the application type description."""

    created_at: str
    """Returns the application creation time."""

    gen_ai_score: float
    """GenAI score for the application. Returns -1 when no score is available."""

    hostnames: List[str]
    """Returns the list of hostnames for the application."""

    human_id: str
    """Returns the human readable ID."""

    ip_subnets: List[str]
    """Returns the list of IP subnets for the application."""

    name: str
    """Returns the application name."""

    port_protocols: List[str]
    """Returns the list of port protocols for the application."""

    support_domains: List[str]
    """Returns the list of support domains for the application."""

    supported: List[Literal["GATEWAY", "ACCESS", "CASB"]]
    """Cloudflare products that support this application."""

    updated_at: str
    """Returns the application update time."""

    version: str
    """Returns the application version."""

    application_score_composition: Optional[object] = None
    """Returns the score composition breakdown for the application."""

    intel_id: Optional[int] = None
    """Returns the Intel API ID for the application."""
