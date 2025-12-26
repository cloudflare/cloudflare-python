# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "LivestreamGetOrgAnalyticsResponse",
    "Data",
    "DataRecordingStats",
    "DataRecordingStatsDayStat",
    "DataSessionStats",
    "DataSessionStatsDayStat",
]


class DataRecordingStatsDayStat(BaseModel):
    day: Optional[str] = None

    total_recording_minutes: Optional[int] = None
    """Total recording minutes for a specific day"""

    total_recordings: Optional[int] = None
    """Total number of recordings for a specific day"""


class DataRecordingStats(BaseModel):
    """Recording statistics of an App during the range specified"""

    day_stats: Optional[List[DataRecordingStatsDayStat]] = None
    """Day wise recording stats"""

    recording_count: Optional[int] = None
    """Total number of recordings during the range specified"""

    recording_minutes_consumed: Optional[float] = None
    """Total recording minutes during the range specified"""


class DataSessionStatsDayStat(BaseModel):
    day: Optional[str] = None

    total_session_minutes: Optional[float] = None
    """Total session minutes for a specific day"""

    total_sessions: Optional[int] = None
    """Total number of sessions for a specific day"""


class DataSessionStats(BaseModel):
    """Session statistics of an App during the range specified"""

    day_stats: Optional[List[DataSessionStatsDayStat]] = None
    """Day wise session stats"""

    sessions_count: Optional[int] = None
    """Total number of sessions during the range specified"""

    sessions_minutes_consumed: Optional[float] = None
    """Total session minutes during the range specified"""


class Data(BaseModel):
    recording_stats: Optional[DataRecordingStats] = None
    """Recording statistics of an App during the range specified"""

    session_stats: Optional[DataSessionStats] = None
    """Session statistics of an App during the range specified"""


class LivestreamGetOrgAnalyticsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
