# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ApplicationUpdateResponse"]


class ApplicationUpdateResponse(BaseModel):
    id: int
    """Returns the application ID."""

    application_confidence_score: float
    """Confidence score for the application. Returns -1 when no score is available."""

    application_source: str
    """Returns the application source."""

    application_type: str
    """Returns the application type."""

    application_type_description: str
    """Returns the application type description."""

    category_id: int
    """Returns the category ID."""

    created_at: str
    """Returns the application creation time."""

    gen_ai_score: float
    """GenAI score for the application. Returns -1 when no score is available."""

    hostnames: List[str]
    """Hostnames matched by the application."""

    human_id: str
    """Returns the human readable ID."""

    ip_subnets: List[str]
    """IP subnets matched by the application."""

    name: str
    """Returns the application name."""

    port_protocols: List[str]
    """Port and protocol pairs matched by the application."""

    support_domains: List[str]
    """Support domains matched by the application."""

    supported: List[Literal["GATEWAY", "ACCESS", "CASB"]]
    """Cloudflare products that support this application."""

    updated_at: str
    """Returns the application update time."""

    version: str
    """Returns the application version."""

    application_score_composition: Optional[object] = None
    """Returns the score composition breakdown for the application."""
