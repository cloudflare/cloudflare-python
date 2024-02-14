# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "TracerouteDiagnosticsTracerouteResponse",
    "TracerouteDiagnosticsTracerouteResponseItem",
    "TracerouteDiagnosticsTracerouteResponseItemColo",
    "TracerouteDiagnosticsTracerouteResponseItemColoColo",
    "TracerouteDiagnosticsTracerouteResponseItemColoHop",
    "TracerouteDiagnosticsTracerouteResponseItemColoHopNode",
]


class TracerouteDiagnosticsTracerouteResponseItemColoColo(BaseModel):
    city: Optional[str] = None
    """Source colo city."""

    name: Optional[str] = None
    """Source colo name."""


class TracerouteDiagnosticsTracerouteResponseItemColoHopNode(BaseModel):
    asn: Optional[str] = None
    """AS number associated with the node object."""

    ip: Optional[str] = None
    """IP address of the node."""

    labels: Optional[List[str]] = None
    """
    Field appears if there is an additional annotation printed when the probe
    returns. Field also appears when running a GRE+ICMP traceroute to denote which
    traceroute a node comes from.
    """

    max_rtt_ms: Optional[float] = None
    """Maximum RTT in ms."""

    mean_rtt_ms: Optional[float] = None
    """Mean RTT in ms."""

    min_rtt_ms: Optional[float] = None
    """Minimum RTT in ms."""

    name: Optional[str] = None
    """Host name of the address, this may be the same as the IP address."""

    packet_count: Optional[int] = None
    """Number of packets with a response from this node."""

    std_dev_rtt_ms: Optional[float] = None
    """Standard deviation of the RTTs in ms."""


class TracerouteDiagnosticsTracerouteResponseItemColoHop(BaseModel):
    nodes: Optional[List[TracerouteDiagnosticsTracerouteResponseItemColoHopNode]] = None
    """An array of node objects."""

    packets_lost: Optional[int] = None
    """Number of packets where no response was received."""

    packets_sent: Optional[int] = None
    """Number of packets sent with specified TTL."""

    packets_ttl: Optional[int] = None
    """The time to live (TTL)."""


class TracerouteDiagnosticsTracerouteResponseItemColo(BaseModel):
    colo: Optional[TracerouteDiagnosticsTracerouteResponseItemColoColo] = None

    error: Optional[
        Literal[
            "",
            "Could not gather traceroute data: Code 1",
            "Could not gather traceroute data: Code 2",
            "Could not gather traceroute data: Code 3",
            "Could not gather traceroute data: Code 4",
        ]
    ] = None
    """Errors resulting from collecting traceroute from colo to target."""

    hops: Optional[List[TracerouteDiagnosticsTracerouteResponseItemColoHop]] = None

    target_summary: Optional[object] = None
    """Aggregated statistics from all hops about the target."""

    traceroute_time_ms: Optional[int] = None
    """Total time of traceroute in ms."""


class TracerouteDiagnosticsTracerouteResponseItem(BaseModel):
    colos: Optional[List[TracerouteDiagnosticsTracerouteResponseItemColo]] = None

    target: Optional[str] = None
    """The target hostname, IPv6, or IPv6 address."""


TracerouteDiagnosticsTracerouteResponse = List[TracerouteDiagnosticsTracerouteResponseItem]
