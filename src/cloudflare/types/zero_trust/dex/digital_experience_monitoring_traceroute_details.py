# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "DigitalExperienceMonitoringTracerouteDetails",
    "TracerouteStats",
    "TracerouteStatsAvailabilityPct",
    "TracerouteStatsAvailabilityPctSlot",
    "TracerouteStatsHopsCount",
    "TracerouteStatsHopsCountSlot",
    "TracerouteStatsPacketLossPct",
    "TracerouteStatsPacketLossPctSlot",
    "TracerouteStatsRoundTripTimeMs",
    "TracerouteStatsRoundTripTimeMsSlot",
    "TracerouteStatsByColo",
    "TracerouteStatsByColoAvailabilityPct",
    "TracerouteStatsByColoAvailabilityPctSlot",
    "TracerouteStatsByColoHopsCount",
    "TracerouteStatsByColoHopsCountSlot",
    "TracerouteStatsByColoPacketLossPct",
    "TracerouteStatsByColoPacketLossPctSlot",
    "TracerouteStatsByColoRoundTripTimeMs",
    "TracerouteStatsByColoRoundTripTimeMsSlot",
]


class TracerouteStatsAvailabilityPctSlot(BaseModel):
    timestamp: str

    value: float


class TracerouteStatsAvailabilityPct(BaseModel):
    slots: List[TracerouteStatsAvailabilityPctSlot]

    avg: Optional[float] = None
    """average observed in the time period"""

    max: Optional[float] = None
    """highest observed in the time period"""

    min: Optional[float] = None
    """lowest observed in the time period"""


class TracerouteStatsHopsCountSlot(BaseModel):
    timestamp: str

    value: int


class TracerouteStatsHopsCount(BaseModel):
    slots: List[TracerouteStatsHopsCountSlot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""


class TracerouteStatsPacketLossPctSlot(BaseModel):
    timestamp: str

    value: float


class TracerouteStatsPacketLossPct(BaseModel):
    slots: List[TracerouteStatsPacketLossPctSlot]

    avg: Optional[float] = None
    """average observed in the time period"""

    max: Optional[float] = None
    """highest observed in the time period"""

    min: Optional[float] = None
    """lowest observed in the time period"""


class TracerouteStatsRoundTripTimeMsSlot(BaseModel):
    timestamp: str

    value: int


class TracerouteStatsRoundTripTimeMs(BaseModel):
    slots: List[TracerouteStatsRoundTripTimeMsSlot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""


class TracerouteStats(BaseModel):
    availability_pct: TracerouteStatsAvailabilityPct = FieldInfo(alias="availabilityPct")

    hops_count: TracerouteStatsHopsCount = FieldInfo(alias="hopsCount")

    packet_loss_pct: TracerouteStatsPacketLossPct = FieldInfo(alias="packetLossPct")

    round_trip_time_ms: TracerouteStatsRoundTripTimeMs = FieldInfo(alias="roundTripTimeMs")

    unique_devices_total: int = FieldInfo(alias="uniqueDevicesTotal")
    """Count of unique devices that have run this test in the given time period"""


class TracerouteStatsByColoAvailabilityPctSlot(BaseModel):
    timestamp: str

    value: float


class TracerouteStatsByColoAvailabilityPct(BaseModel):
    slots: List[TracerouteStatsByColoAvailabilityPctSlot]

    avg: Optional[float] = None
    """average observed in the time period"""

    max: Optional[float] = None
    """highest observed in the time period"""

    min: Optional[float] = None
    """lowest observed in the time period"""


class TracerouteStatsByColoHopsCountSlot(BaseModel):
    timestamp: str

    value: int


class TracerouteStatsByColoHopsCount(BaseModel):
    slots: List[TracerouteStatsByColoHopsCountSlot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""


class TracerouteStatsByColoPacketLossPctSlot(BaseModel):
    timestamp: str

    value: float


class TracerouteStatsByColoPacketLossPct(BaseModel):
    slots: List[TracerouteStatsByColoPacketLossPctSlot]

    avg: Optional[float] = None
    """average observed in the time period"""

    max: Optional[float] = None
    """highest observed in the time period"""

    min: Optional[float] = None
    """lowest observed in the time period"""


class TracerouteStatsByColoRoundTripTimeMsSlot(BaseModel):
    timestamp: str

    value: int


class TracerouteStatsByColoRoundTripTimeMs(BaseModel):
    slots: List[TracerouteStatsByColoRoundTripTimeMsSlot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""


class TracerouteStatsByColo(BaseModel):
    availability_pct: TracerouteStatsByColoAvailabilityPct = FieldInfo(alias="availabilityPct")

    colo: str

    hops_count: TracerouteStatsByColoHopsCount = FieldInfo(alias="hopsCount")

    packet_loss_pct: TracerouteStatsByColoPacketLossPct = FieldInfo(alias="packetLossPct")

    round_trip_time_ms: TracerouteStatsByColoRoundTripTimeMs = FieldInfo(alias="roundTripTimeMs")

    unique_devices_total: int = FieldInfo(alias="uniqueDevicesTotal")
    """Count of unique devices that have run this test in the given time period"""


class DigitalExperienceMonitoringTracerouteDetails(BaseModel):
    host: str
    """The host of the Traceroute synthetic application test"""

    interval: str
    """The interval at which the Traceroute synthetic application test is set to run."""

    kind: Literal["traceroute"]

    name: str
    """The name of the Traceroute synthetic application test"""

    traceroute_stats: Optional[TracerouteStats] = FieldInfo(alias="tracerouteStats", default=None)

    traceroute_stats_by_colo: Optional[List[TracerouteStatsByColo]] = FieldInfo(
        alias="tracerouteStatsByColo", default=None
    )
