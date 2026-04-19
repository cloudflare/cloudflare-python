# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "SessionGetSessionParticipantDetailsResponse",
    "Data",
    "DataParticipant",
    "DataParticipantPeerStats",
    "DataParticipantPeerStatsDeviceInfo",
    "DataParticipantPeerStatsEvent",
    "DataParticipantPeerStatsIPInformation",
    "DataParticipantPeerStatsPrecallNetworkInformation",
    "DataParticipantQualityStat",
    "DataParticipantQualityStatAudioStat",
    "DataParticipantQualityStatVideoStat",
]


class DataParticipantPeerStatsDeviceInfo(BaseModel):
    browser: Optional[str] = None

    browser_version: Optional[str] = None

    cpus: Optional[float] = None

    engine: Optional[str] = None

    is_mobile: Optional[bool] = None

    memory: Optional[float] = None

    os: Optional[str] = None

    os_version: Optional[str] = None

    sdk_name: Optional[str] = None

    sdk_version: Optional[str] = None

    user_agent: Optional[str] = None

    webgl_support: Optional[str] = None


class DataParticipantPeerStatsEvent(BaseModel):
    timestamp: Optional[str] = None

    type: Optional[str] = None


class DataParticipantPeerStatsIPInformation(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    ip_location: Optional[str] = None

    ipv4: Optional[str] = None

    org: Optional[str] = None

    portal: Optional[str] = None

    region: Optional[str] = None

    timezone: Optional[str] = None


class DataParticipantPeerStatsPrecallNetworkInformation(BaseModel):
    backend_rtt: Optional[float] = None

    effective_networktype: Optional[str] = None

    fractional_loss: Optional[float] = None

    jitter: Optional[float] = None

    reflexive_connectivity: Optional[bool] = None

    relay_connectivity: Optional[bool] = None

    rtt: Optional[float] = None

    throughtput: Optional[float] = None

    turn_connectivity: Optional[bool] = None


class DataParticipantPeerStats(BaseModel):
    config: Optional[str] = None

    device_info: Optional[DataParticipantPeerStatsDeviceInfo] = None

    events: Optional[List[DataParticipantPeerStatsEvent]] = None

    ip_information: Optional[DataParticipantPeerStatsIPInformation] = None

    precall_network_information: Optional[DataParticipantPeerStatsPrecallNetworkInformation] = None

    status: Optional[str] = None


class DataParticipantQualityStatAudioStat(BaseModel):
    concealment_events: Optional[float] = None

    jitter: Optional[float] = None

    packets_lost: Optional[float] = None

    quality: Optional[float] = None

    timestamp: Optional[str] = None


class DataParticipantQualityStatVideoStat(BaseModel):
    frame_height: Optional[float] = None

    frame_width: Optional[float] = None

    frames_dropped: Optional[float] = None

    frames_per_second: Optional[float] = None

    jitter: Optional[float] = None

    packets_lost: Optional[float] = None

    quality: Optional[float] = None

    timestamp: Optional[str] = None


class DataParticipantQualityStat(BaseModel):
    audio_bandwidth: Optional[float] = None

    audio_packet_loss: Optional[float] = None

    audio_stats: Optional[List[DataParticipantQualityStatAudioStat]] = None

    average_quality: Optional[float] = None

    end: Optional[str] = None

    peer_id: Optional[str] = None

    start: Optional[str] = None

    video_bandwidth: Optional[float] = None

    video_packet_loss: Optional[float] = None

    video_stats: Optional[List[DataParticipantQualityStatVideoStat]] = None


class DataParticipant(BaseModel):
    id: Optional[str] = None
    """Participant ID. This maps to the corresponding peerId."""

    created_at: Optional[str] = None
    """timestamp when this participant was created."""

    custom_participant_id: Optional[str] = None
    """ID passed by client to create this participant."""

    display_name: Optional[str] = None
    """Display name of participant when joining the session."""

    duration: Optional[float] = None
    """number of minutes for which the participant was in the session."""

    joined_at: Optional[str] = None
    """timestamp at which participant joined the session."""

    left_at: Optional[str] = None
    """timestamp at which participant left the session."""

    peer_stats: Optional[DataParticipantPeerStats] = None

    preset_name: Optional[str] = None
    """Name of the preset associated with the participant."""

    quality_stats: Optional[List[DataParticipantQualityStat]] = None

    updated_at: Optional[str] = None
    """timestamp when this participant's data was last updated."""

    user_id: Optional[str] = None
    """User id for this participant."""


class Data(BaseModel):
    participant: Optional[DataParticipant] = None


class SessionGetSessionParticipantDetailsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
