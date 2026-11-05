# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ApplicationListResponse"]


class ApplicationListResponse(BaseModel):
    """Describes one application in a list response.

    The response returns every property below unless `fields` narrows it. Treat all properties except `id` as optional.
    """

    id: int
    """Numeric identifier for the application."""

    application_confidence_score: Optional[float] = None
    """Confidence score for the application. Returns -1 when no score is available."""

    application_score_composition: Optional[object] = None
    """Returns the score composition breakdown for the application."""

    application_source: Optional[str] = None
    """Returns the application source."""

    application_type: Optional[str] = None
    """Returns the application type."""

    application_type_description: Optional[str] = None
    """Returns the application type description."""

    category_id: Optional[int] = None
    """Numeric identifier for an application category."""

    created_at: Optional[str] = None
    """Returns the application creation time."""

    gen_ai_score: Optional[float] = None
    """GenAI score for the application. Returns -1 when no score is available."""

    hostnames: Optional[List[str]] = None
    """Hostnames matched by the application."""

    human_id: Optional[str] = None
    """Human-readable identifier for the application."""

    ip_subnets: Optional[List[str]] = None
    """IP subnets for this application.

    Custom application create and update requests accept IPv4 prefix lengths /8
    through /32 and IPv6 prefix lengths /32 through /128.
    """

    name: Optional[str] = None
    """Application name."""

    port_protocols: Optional[List[str]] = None
    """
    Ports matched by the application, in `protocol/port` or inclusive
    `protocol/start-end` format (for example, `tcp/443` or `udp/10000-20000`). TCP
    and UDP ports must be between 0 and 65535.
    """

    review_status: Optional[Literal["approved", "unapproved", "in_review", "unreviewed"]] = None
    """The account-specific Gateway review status.

    Applications with no assigned review status are returned as `unreviewed`.
    """

    support_domains: Optional[List[str]] = None
    """Support domains matched by the application."""

    supported: Optional[List[Literal["GATEWAY", "ACCESS", "CASB"]]] = None
    """Cloudflare products that support this application."""

    updated_at: Optional[str] = None
    """Returns the application update time."""

    version: Optional[str] = None
    """Returns the application version."""
