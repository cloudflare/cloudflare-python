# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..digital_experience_monitor import DigitalExperienceMonitor
from .http_tests.test_stat_over_time import TestStatOverTime

__all__ = [
    "Traceroute",
    "TracerouteStats",
    "TracerouteStatsAvailabilityPct",
    "TracerouteStatsAvailabilityPctSlot",
    "TracerouteStatsPacketLossPct",
    "TracerouteStatsPacketLossPctSlot",
    "TracerouteStatsByColo",
    "TracerouteStatsByColoAvailabilityPct",
    "TracerouteStatsByColoAvailabilityPctSlot",
    "TracerouteStatsByColoPacketLossPct",
    "TracerouteStatsByColoPacketLossPctSlot",
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


class TracerouteStats(BaseModel):
    availability_pct: TracerouteStatsAvailabilityPct = FieldInfo(alias="availabilityPct")

    hops_count: TestStatOverTime = FieldInfo(alias="hopsCount")

    packet_loss_pct: TracerouteStatsPacketLossPct = FieldInfo(alias="packetLossPct")

    round_trip_time_ms: TestStatOverTime = FieldInfo(alias="roundTripTimeMs")

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


class TracerouteStatsByColo(BaseModel):
    availability_pct: TracerouteStatsByColoAvailabilityPct = FieldInfo(alias="availabilityPct")

    colo: str

    hops_count: TestStatOverTime = FieldInfo(alias="hopsCount")

    packet_loss_pct: TracerouteStatsByColoPacketLossPct = FieldInfo(alias="packetLossPct")

    round_trip_time_ms: TestStatOverTime = FieldInfo(alias="roundTripTimeMs")

    unique_devices_total: int = FieldInfo(alias="uniqueDevicesTotal")
    """Count of unique devices that have run this test in the given time period"""


class Traceroute(BaseModel):
    host: str
    """The host of the Traceroute synthetic application test"""

    interval: str
    """The interval at which the Traceroute synthetic application test is set to run."""

    kind: Literal["traceroute"]

    name: str
    """The name of the Traceroute synthetic application test"""

    target_policies: Optional[List[DigitalExperienceMonitor]] = None

    targeted: Optional[bool] = None

    traceroute_stats: Optional[TracerouteStats] = FieldInfo(alias="tracerouteStats", default=None)

    traceroute_stats_by_colo: Optional[List[TracerouteStatsByColo]] = FieldInfo(
        alias="tracerouteStatsByColo", default=None
    )
