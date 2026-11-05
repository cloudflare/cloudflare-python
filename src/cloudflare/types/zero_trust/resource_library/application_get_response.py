# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ApplicationGetResponse"]


class ApplicationGetResponse(BaseModel):
    id: int
    """Numeric identifier for the application."""

    application_confidence_score: float
    """Confidence score for the application. Returns -1 when no score is available."""

    application_source: str
    """Returns the application source."""

    application_type: str
    """Returns the application type."""

    application_type_description: str
    """Returns the application type description."""

    category_id: int
    """Numeric identifier for an application category."""

    created_at: str
    """Returns the application creation time."""

    gen_ai_score: float
    """GenAI score for the application. Returns -1 when no score is available."""

    hostnames: List[str]
    """Hostnames matched by the application."""

    human_id: str
    """Human-readable identifier for the application."""

    ip_subnets: List[str]
    """IP subnets for this application.

    Custom application create and update requests accept IPv4 prefix lengths /8
    through /32 and IPv6 prefix lengths /32 through /128.
    """

    name: str
    """Application name."""

    port_protocols: List[str]
    """
    Ports matched by the application, in `protocol/port` or inclusive
    `protocol/start-end` format (for example, `tcp/443` or `udp/10000-20000`). TCP
    and UDP ports must be between 0 and 65535.
    """

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
