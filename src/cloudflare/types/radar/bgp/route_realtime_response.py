# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["RouteRealtimeResponse", "Meta", "MetaASNInfo", "MetaCollector", "MetaRPKI", "MetaVisibility", "Route"]


class MetaASNInfo(BaseModel):
    as_name: str
    """Name of the autonomous system."""

    asn: int
    """AS number."""

    country_code: str
    """Alpha-2 code for the AS's registration country."""

    org_id: str
    """Organization ID."""

    org_name: str
    """Organization name."""


class MetaCollector(BaseModel):
    collector: str
    """Public route collector ID."""

    latest_realtime_ts: str
    """Latest realtime stream timestamp for this collector."""

    latest_rib_ts: str
    """Latest RIB dump MRT file timestamp for this collector."""

    latest_updates_ts: str
    """Latest BGP updates MRT file timestamp for this collector."""

    peers_count: int
    """Total number of collector peers used from this collector."""

    peers_v4_count: int
    """Total number of collector peers used from this collector for IPv4 prefixes."""

    peers_v6_count: int
    """Total number of collector peers used from this collector for IPv6 prefixes."""


class MetaRPKI(BaseModel):
    origin: int
    """Origin ASN."""

    rpki_validation: str
    """Validation status: valid, invalid, or unknown."""


class MetaVisibility(BaseModel):
    total_peers: int
    """Total number of peers."""

    total_visible: int
    """Total number of peers seeing this prefix."""

    visibility: float
    """Ratio of peers seeing this prefix to total number of peers."""


class Meta(BaseModel):
    asn_info: List[MetaASNInfo]

    collectors: List[MetaCollector]

    rpki: List[MetaRPKI]

    visibility: MetaVisibility


class Route(BaseModel):
    as_path: List[int]
    """AS-level path for this route, from collector to origin."""

    collector: str
    """Public collector ID for this route."""

    communities: List[str]
    """BGP community values."""

    prefix: str
    """IP prefix of this query."""

    timestamp: str
    """Latest timestamp of change for this route."""


class RouteRealtimeResponse(BaseModel):
    meta: Meta

    routes: List[Route]
