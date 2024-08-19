# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DiscoveryOperation", "Features", "FeaturesTrafficStats"]


class FeaturesTrafficStats(BaseModel):
    last_updated: datetime

    period_seconds: int
    """The period in seconds these statistics were computed over"""

    requests: float
    """The average number of requests seen during this period"""


class Features(BaseModel):
    traffic_stats: Optional[FeaturesTrafficStats] = None


class DiscoveryOperation(BaseModel):
    id: str
    """UUID"""

    endpoint: str
    """
    The endpoint which can contain path parameter templates in curly braces, each
    will be replaced from left to right with {varN}, starting with {var1}, during
    insertion. This will further be Cloudflare-normalized upon insertion. See:
    https://developers.cloudflare.com/rules/normalization/how-it-works/.
    """

    host: str
    """RFC3986-compliant host."""

    last_updated: datetime

    method: Literal["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "CONNECT", "PATCH", "TRACE"]
    """The HTTP method used to access the endpoint."""

    origin: List[Literal["ML", "SessionIdentifier"]]
    """API discovery engine(s) that discovered this operation"""

    state: Literal["review", "saved", "ignored"]
    """State of operation in API Discovery

    - `review` - Operation is not saved into API Shield Endpoint Management
    - `saved` - Operation is saved into API Shield Endpoint Management
    - `ignored` - Operation is marked as ignored
    """

    features: Optional[Features] = None
