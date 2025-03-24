# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["RouteRealtimeResponse", "Meta", "MetaCollector", "Route"]


class MetaCollector(BaseModel):
    collector: str
    """public route collector ID"""

    latest_realtime_ts: str
    """latest realtime stream timestamp for this collector"""

    latest_rib_ts: str
    """latest RIB dump MRT file timestamp for this collector"""

    latest_updates_ts: str
    """latest BGP updates MRT file timestamp for this collector"""


class Meta(BaseModel):
    collectors: List[MetaCollector]


class Route(BaseModel):
    as_path: List[int]
    """AS-level path for this route, from collector to origin"""

    collector: str
    """public collector ID for this route"""

    communities: List[str]
    """BGP community values"""

    prefix: str
    """IP prefix of this query"""

    timestamp: str
    """latest timestamp of change for this route"""


class RouteRealtimeResponse(BaseModel):
    meta: Meta

    routes: List[Route]
