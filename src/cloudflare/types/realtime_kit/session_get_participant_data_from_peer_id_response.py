# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SessionGetParticipantDataFromPeerIDResponse",
    "Data",
    "DataParticipant",
    "DataParticipantPeerEvent",
    "DataParticipantPeerReport",
    "DataParticipantPeerReportMetadata",
    "DataParticipantPeerReportMetadataAudioDevicesUpdate",
    "DataParticipantPeerReportMetadataAudioDevicesUpdateAdded",
    "DataParticipantPeerReportMetadataAudioDevicesUpdateRemoved",
    "DataParticipantPeerReportMetadataBrowserMetadata",
    "DataParticipantPeerReportMetadataCandidatePairs",
    "DataParticipantPeerReportMetadataCandidatePairsConsumingTransport",
    "DataParticipantPeerReportMetadataCandidatePairsProducingTransport",
    "DataParticipantPeerReportMetadataDeviceInfo",
    "DataParticipantPeerReportMetadataEvent",
    "DataParticipantPeerReportMetadataIPInformation",
    "DataParticipantPeerReportMetadataIPInformationASN",
    "DataParticipantPeerReportMetadataNativeMetadata",
    "DataParticipantPeerReportMetadataPcMetadata",
    "DataParticipantPeerReportMetadataSelectedDeviceUpdate",
    "DataParticipantPeerReportMetadataSelectedDeviceUpdateDevice",
    "DataParticipantPeerReportMetadataSpeakerDevicesUpdate",
    "DataParticipantPeerReportMetadataSpeakerDevicesUpdateAdded",
    "DataParticipantPeerReportMetadataSpeakerDevicesUpdateRemoved",
    "DataParticipantPeerReportMetadataVideoDevicesUpdate",
    "DataParticipantPeerReportMetadataVideoDevicesUpdateAdded",
    "DataParticipantPeerReportMetadataVideoDevicesUpdateRemoved",
    "DataParticipantPeerReportQuality",
    "DataParticipantPeerReportQualityAudioConsumer",
    "DataParticipantPeerReportQualityAudioConsumerCumulative",
    "DataParticipantPeerReportQualityAudioConsumerCumulativeJitterBufferDelay",
    "DataParticipantPeerReportQualityAudioConsumerCumulativePacketLoss",
    "DataParticipantPeerReportQualityAudioConsumerCumulativeQualityMos",
    "DataParticipantPeerReportQualityAudioProducer",
    "DataParticipantPeerReportQualityAudioProducerCumulative",
    "DataParticipantPeerReportQualityAudioProducerCumulativePacketLoss",
    "DataParticipantPeerReportQualityAudioProducerCumulativeQualityMos",
    "DataParticipantPeerReportQualityAudioProducerCumulativeRTT",
    "DataParticipantPeerReportQualityScreenshareAudioConsumer",
    "DataParticipantPeerReportQualityScreenshareAudioConsumerCumulative",
    "DataParticipantPeerReportQualityScreenshareAudioConsumerCumulativeJitterBufferDelay",
    "DataParticipantPeerReportQualityScreenshareAudioConsumerCumulativePacketLoss",
    "DataParticipantPeerReportQualityScreenshareAudioConsumerCumulativeQualityMos",
    "DataParticipantPeerReportQualityScreenshareAudioProducer",
    "DataParticipantPeerReportQualityScreenshareAudioProducerCumulative",
    "DataParticipantPeerReportQualityScreenshareAudioProducerCumulativePacketLoss",
    "DataParticipantPeerReportQualityScreenshareAudioProducerCumulativeQualityMos",
    "DataParticipantPeerReportQualityScreenshareAudioProducerCumulativeRTT",
    "DataParticipantPeerReportQualityScreenshareVideoConsumer",
    "DataParticipantPeerReportQualityScreenshareVideoConsumerCumulative",
    "DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeFramePerSecond",
    "DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeFrameWidth",
    "DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeIssues",
    "DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeJitterBufferDelay",
    "DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativePacketLoss",
    "DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeQualityMos",
    "DataParticipantPeerReportQualityScreenshareVideoProducer",
    "DataParticipantPeerReportQualityScreenshareVideoProducerQualityLimitationDurations",
    "DataParticipantPeerReportQualityScreenshareVideoProducerCumulative",
    "DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeFramePerSecond",
    "DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeFrameWidth",
    "DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeIssues",
    "DataParticipantPeerReportQualityScreenshareVideoProducerCumulativePacketLoss",
    "DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeQualityMos",
    "DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeRTT",
    "DataParticipantPeerReportQualityVideoConsumer",
    "DataParticipantPeerReportQualityVideoConsumerCumulative",
    "DataParticipantPeerReportQualityVideoConsumerCumulativeFramePerSecond",
    "DataParticipantPeerReportQualityVideoConsumerCumulativeFrameWidth",
    "DataParticipantPeerReportQualityVideoConsumerCumulativeIssues",
    "DataParticipantPeerReportQualityVideoConsumerCumulativeJitterBufferDelay",
    "DataParticipantPeerReportQualityVideoConsumerCumulativePacketLoss",
    "DataParticipantPeerReportQualityVideoConsumerCumulativeQualityMos",
    "DataParticipantPeerReportQualityVideoProducer",
    "DataParticipantPeerReportQualityVideoProducerQualityLimitationDurations",
    "DataParticipantPeerReportQualityVideoProducerCumulative",
    "DataParticipantPeerReportQualityVideoProducerCumulativeFramePerSecond",
    "DataParticipantPeerReportQualityVideoProducerCumulativeFrameWidth",
    "DataParticipantPeerReportQualityVideoProducerCumulativeIssues",
    "DataParticipantPeerReportQualityVideoProducerCumulativePacketLoss",
    "DataParticipantPeerReportQualityVideoProducerCumulativeQualityMos",
    "DataParticipantPeerReportQualityVideoProducerCumulativeRTT",
]


class DataParticipantPeerEvent(BaseModel):
    """A connection lifecycle event recorded for a participant's peer."""

    id: Optional[str] = None
    """ID of the peer event."""

    created_at: Optional[str] = None
    """Timestamp when this peer event was created."""

    event_name: Optional[Literal["PEER_CREATED", "PEER_JOINING", "PEER_LEAVING"]] = None
    """Name of the peer event."""

    minutes_consumed: Optional[float] = None
    """Minutes consumed attributed to this event."""

    participant_id: Optional[str] = None
    """ID of the participant this event belongs to."""

    peer_id: Optional[str] = None
    """Peer ID this event belongs to."""

    preset_view_type: Optional[Literal["GROUP_CALL", "WEBINAR", "AUDIO_ROOM", "LIVESTREAM", "CHAT"]] = None
    """View type of the preset associated with the peer."""

    session_id: Optional[str] = None
    """ID of the session this event belongs to."""

    socket_session_id: Optional[str] = None
    """ID of the socket session associated with this event."""

    updated_at: Optional[str] = None
    """Timestamp when this peer event was last updated."""


class DataParticipantPeerReportMetadataAudioDevicesUpdateAdded(BaseModel):
    """A media device (camera, microphone, or speaker)."""

    device_id: Optional[str] = None
    """ID of the device."""

    kind: Optional[str] = None
    """Kind of device, for example audioinput or videoinput."""

    label: Optional[str] = None
    """Human-readable label of the device."""


class DataParticipantPeerReportMetadataAudioDevicesUpdateRemoved(BaseModel):
    """A media device (camera, microphone, or speaker)."""

    device_id: Optional[str] = None
    """ID of the device."""

    kind: Optional[str] = None
    """Kind of device, for example audioinput or videoinput."""

    label: Optional[str] = None
    """Human-readable label of the device."""


class DataParticipantPeerReportMetadataAudioDevicesUpdate(BaseModel):
    """A change to the set of available devices at a point in time."""

    added: Optional[List[DataParticipantPeerReportMetadataAudioDevicesUpdateAdded]] = None
    """Devices that became available."""

    removed: Optional[List[DataParticipantPeerReportMetadataAudioDevicesUpdateRemoved]] = None
    """Devices that became unavailable."""

    timestamp: Optional[str] = None
    """Timestamp of the device update."""


class DataParticipantPeerReportMetadataBrowserMetadata(BaseModel):
    browser: Optional[str] = None

    browser_version: Optional[str] = None

    engine: Optional[str] = None

    user_agent: Optional[str] = None

    webgl_support: Optional[bool] = None


class DataParticipantPeerReportMetadataCandidatePairsConsumingTransport(BaseModel):
    """ICE candidate pair statistics for a transport."""

    available_incoming_bitrate: Optional[float] = None

    available_outgoing_bitrate: Optional[float] = None

    bytes_discarded_on_send: Optional[float] = None

    bytes_received: Optional[float] = None

    bytes_sent: Optional[float] = None

    current_round_trip_time: Optional[float] = None

    last_packet_received_timestamp: Optional[float] = None
    """Epoch milliseconds when the last packet was received."""

    last_packet_sent_timestamp: Optional[float] = None
    """Epoch milliseconds when the last packet was sent."""

    local_candidate_address: Optional[str] = None

    local_candidate_id: Optional[str] = None

    local_candidate_network_type: Optional[str] = None

    local_candidate_port: Optional[float] = None

    local_candidate_protocol: Optional[str] = None

    local_candidate_related_address: Optional[str] = None

    local_candidate_related_port: Optional[float] = None

    local_candidate_type: Optional[str] = None

    local_candidate_url: Optional[str] = None

    nominated: Optional[bool] = None

    packets_discarded_on_send: Optional[float] = None

    packets_received: Optional[float] = None

    packets_sent: Optional[float] = None

    remote_candidate_address: Optional[str] = None

    remote_candidate_id: Optional[str] = None

    remote_candidate_port: Optional[float] = None

    remote_candidate_protocol: Optional[str] = None

    remote_candidate_type: Optional[str] = None

    remote_candidate_url: Optional[str] = None

    total_round_trip_time: Optional[float] = None


class DataParticipantPeerReportMetadataCandidatePairsProducingTransport(BaseModel):
    """ICE candidate pair statistics for a transport."""

    available_incoming_bitrate: Optional[float] = None

    available_outgoing_bitrate: Optional[float] = None

    bytes_discarded_on_send: Optional[float] = None

    bytes_received: Optional[float] = None

    bytes_sent: Optional[float] = None

    current_round_trip_time: Optional[float] = None

    last_packet_received_timestamp: Optional[float] = None
    """Epoch milliseconds when the last packet was received."""

    last_packet_sent_timestamp: Optional[float] = None
    """Epoch milliseconds when the last packet was sent."""

    local_candidate_address: Optional[str] = None

    local_candidate_id: Optional[str] = None

    local_candidate_network_type: Optional[str] = None

    local_candidate_port: Optional[float] = None

    local_candidate_protocol: Optional[str] = None

    local_candidate_related_address: Optional[str] = None

    local_candidate_related_port: Optional[float] = None

    local_candidate_type: Optional[str] = None

    local_candidate_url: Optional[str] = None

    nominated: Optional[bool] = None

    packets_discarded_on_send: Optional[float] = None

    packets_received: Optional[float] = None

    packets_sent: Optional[float] = None

    remote_candidate_address: Optional[str] = None

    remote_candidate_id: Optional[str] = None

    remote_candidate_port: Optional[float] = None

    remote_candidate_protocol: Optional[str] = None

    remote_candidate_type: Optional[str] = None

    remote_candidate_url: Optional[str] = None

    total_round_trip_time: Optional[float] = None


class DataParticipantPeerReportMetadataCandidatePairs(BaseModel):
    consuming_transport: Optional[List[DataParticipantPeerReportMetadataCandidatePairsConsumingTransport]] = None

    producing_transport: Optional[List[DataParticipantPeerReportMetadataCandidatePairsProducingTransport]] = None


class DataParticipantPeerReportMetadataDeviceInfo(BaseModel):
    cpus: Optional[float] = None

    is_mobile: Optional[bool] = None

    os: Optional[str] = None

    os_version: Optional[str] = None


class DataParticipantPeerReportMetadataEvent(BaseModel):
    """A timestamped event recorded during the participant's connection."""

    metadata: Optional[Dict[str, Union[str, float, bool, None]]] = None
    """Event-specific metadata.

    Keys vary per event; values are primitive scalars (string, number, boolean, or
    null).
    """

    name: Optional[str] = None
    """Name of the event."""

    timestamp: Optional[str] = None
    """Timestamp when the event occurred."""


class DataParticipantPeerReportMetadataIPInformationASN(BaseModel):
    asn: Optional[str] = None

    domain: Optional[str] = None

    name: Optional[str] = None

    route: Optional[str] = None

    type: Optional[str] = None


class DataParticipantPeerReportMetadataIPInformation(BaseModel):
    asn: Optional[DataParticipantPeerReportMetadataIPInformationASN] = None

    city: Optional[str] = None

    country: Optional[str] = None

    ipv4: Optional[str] = None

    org: Optional[str] = None

    region: Optional[str] = None

    timezone: Optional[str] = None


class DataParticipantPeerReportMetadataNativeMetadata(BaseModel):
    audio_encoder: Optional[str] = None

    video_encoder: Optional[str] = None


class DataParticipantPeerReportMetadataPcMetadata(BaseModel):
    effective_network_type: Optional[str] = None

    reflexive_connectivity: Optional[bool] = None

    relay_connectivity: Optional[bool] = None

    sdp: Optional[List[str]] = None

    timestamp: Optional[str] = None

    turn_connectivity: Optional[bool] = None


class DataParticipantPeerReportMetadataSelectedDeviceUpdateDevice(BaseModel):
    """A media device (camera, microphone, or speaker)."""

    device_id: Optional[str] = None
    """ID of the device."""

    kind: Optional[str] = None
    """Kind of device, for example audioinput or videoinput."""

    label: Optional[str] = None
    """Human-readable label of the device."""


class DataParticipantPeerReportMetadataSelectedDeviceUpdate(BaseModel):
    device: Optional[DataParticipantPeerReportMetadataSelectedDeviceUpdateDevice] = None
    """A media device (camera, microphone, or speaker)."""

    timestamp: Optional[str] = None


class DataParticipantPeerReportMetadataSpeakerDevicesUpdateAdded(BaseModel):
    """A media device (camera, microphone, or speaker)."""

    device_id: Optional[str] = None
    """ID of the device."""

    kind: Optional[str] = None
    """Kind of device, for example audioinput or videoinput."""

    label: Optional[str] = None
    """Human-readable label of the device."""


class DataParticipantPeerReportMetadataSpeakerDevicesUpdateRemoved(BaseModel):
    """A media device (camera, microphone, or speaker)."""

    device_id: Optional[str] = None
    """ID of the device."""

    kind: Optional[str] = None
    """Kind of device, for example audioinput or videoinput."""

    label: Optional[str] = None
    """Human-readable label of the device."""


class DataParticipantPeerReportMetadataSpeakerDevicesUpdate(BaseModel):
    """A change to the set of available devices at a point in time."""

    added: Optional[List[DataParticipantPeerReportMetadataSpeakerDevicesUpdateAdded]] = None
    """Devices that became available."""

    removed: Optional[List[DataParticipantPeerReportMetadataSpeakerDevicesUpdateRemoved]] = None
    """Devices that became unavailable."""

    timestamp: Optional[str] = None
    """Timestamp of the device update."""


class DataParticipantPeerReportMetadataVideoDevicesUpdateAdded(BaseModel):
    """A media device (camera, microphone, or speaker)."""

    device_id: Optional[str] = None
    """ID of the device."""

    kind: Optional[str] = None
    """Kind of device, for example audioinput or videoinput."""

    label: Optional[str] = None
    """Human-readable label of the device."""


class DataParticipantPeerReportMetadataVideoDevicesUpdateRemoved(BaseModel):
    """A media device (camera, microphone, or speaker)."""

    device_id: Optional[str] = None
    """ID of the device."""

    kind: Optional[str] = None
    """Kind of device, for example audioinput or videoinput."""

    label: Optional[str] = None
    """Human-readable label of the device."""


class DataParticipantPeerReportMetadataVideoDevicesUpdate(BaseModel):
    """A change to the set of available devices at a point in time."""

    added: Optional[List[DataParticipantPeerReportMetadataVideoDevicesUpdateAdded]] = None
    """Devices that became available."""

    removed: Optional[List[DataParticipantPeerReportMetadataVideoDevicesUpdateRemoved]] = None
    """Devices that became unavailable."""

    timestamp: Optional[str] = None
    """Timestamp of the device update."""


class DataParticipantPeerReportMetadata(BaseModel):
    """Connection and device metadata for the participant."""

    audio_devices_updates: Optional[List[DataParticipantPeerReportMetadataAudioDevicesUpdate]] = None

    browser_metadata: Optional[DataParticipantPeerReportMetadataBrowserMetadata] = None

    candidate_pairs: Optional[DataParticipantPeerReportMetadataCandidatePairs] = None

    device_info: Optional[DataParticipantPeerReportMetadataDeviceInfo] = None

    events: Optional[List[DataParticipantPeerReportMetadataEvent]] = None

    ip_information: Optional[DataParticipantPeerReportMetadataIPInformation] = None

    native_metadata: Optional[DataParticipantPeerReportMetadataNativeMetadata] = None

    pc_metadata: Optional[List[DataParticipantPeerReportMetadataPcMetadata]] = None

    room_view_type: Optional[str] = None

    sdk_name: Optional[str] = None

    sdk_type: Optional[str] = None

    sdk_version: Optional[str] = None

    selected_device_updates: Optional[List[DataParticipantPeerReportMetadataSelectedDeviceUpdate]] = None

    speaker_devices_updates: Optional[List[DataParticipantPeerReportMetadataSpeakerDevicesUpdate]] = None

    video_devices_updates: Optional[List[DataParticipantPeerReportMetadataVideoDevicesUpdate]] = None


class DataParticipantPeerReportQualityAudioConsumer(BaseModel):
    """Per-sample inbound (consumer) audio statistics."""

    bytes_received: Optional[float] = None

    concealment_events: Optional[float] = None

    consumer_id: Optional[str] = None

    jitter: Optional[float] = None

    jitter_buffer_delay: Optional[float] = None

    jitter_buffer_emitted_count: Optional[float] = None

    mid: Optional[str] = None

    mos_quality: Optional[float] = None

    packets_lost: Optional[float] = None

    packets_received: Optional[float] = None

    peer_id: Optional[str] = None

    producer_id: Optional[str] = None

    ssrc: Optional[float] = None

    timestamp: Optional[str] = None


class DataParticipantPeerReportQualityAudioConsumerCumulativeJitterBufferDelay(BaseModel):
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    api_100ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="100ms_or_greater_event_fraction", default=None
    )

    api_250ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="250ms_or_greater_event_fraction", default=None
    )

    api_500ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="500ms_or_greater_event_fraction", default=None
    )

    avg: Optional[float] = None


class DataParticipantPeerReportQualityAudioConsumerCumulativePacketLoss(BaseModel):
    """Cumulative packet loss distribution."""

    api_10_or_greater_event_fraction: Optional[float] = FieldInfo(alias="10_or_greater_event_fraction", default=None)

    api_25_or_greater_event_fraction: Optional[float] = FieldInfo(alias="25_or_greater_event_fraction", default=None)

    api_5_or_greater_event_fraction: Optional[float] = FieldInfo(alias="5_or_greater_event_fraction", default=None)

    api_50_or_greater_event_fraction: Optional[float] = FieldInfo(alias="50_or_greater_event_fraction", default=None)

    avg: Optional[float] = None


class DataParticipantPeerReportQualityAudioConsumerCumulativeQualityMos(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityAudioConsumerCumulative(BaseModel):
    """Aggregated inbound (consumer) audio statistics for the session."""

    jitter_buffer_delay: Optional[DataParticipantPeerReportQualityAudioConsumerCumulativeJitterBufferDelay] = None
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    packet_loss: Optional[DataParticipantPeerReportQualityAudioConsumerCumulativePacketLoss] = None
    """Cumulative packet loss distribution."""

    quality_mos: Optional[DataParticipantPeerReportQualityAudioConsumerCumulativeQualityMos] = None
    """Distribution summary with average and percentiles."""


class DataParticipantPeerReportQualityAudioProducer(BaseModel):
    """Per-sample outbound (producer) audio statistics."""

    bytes_sent: Optional[float] = None

    jitter: Optional[float] = None

    mid: Optional[str] = None

    mos_quality: Optional[float] = None

    packets_lost: Optional[float] = None

    packets_sent: Optional[float] = None

    producer_id: Optional[str] = None

    rtt: Optional[float] = None

    ssrc: Optional[float] = None

    timestamp: Optional[str] = None


class DataParticipantPeerReportQualityAudioProducerCumulativePacketLoss(BaseModel):
    """Cumulative packet loss distribution."""

    api_10_or_greater_event_fraction: Optional[float] = FieldInfo(alias="10_or_greater_event_fraction", default=None)

    api_25_or_greater_event_fraction: Optional[float] = FieldInfo(alias="25_or_greater_event_fraction", default=None)

    api_5_or_greater_event_fraction: Optional[float] = FieldInfo(alias="5_or_greater_event_fraction", default=None)

    api_50_or_greater_event_fraction: Optional[float] = FieldInfo(alias="50_or_greater_event_fraction", default=None)

    avg: Optional[float] = None


class DataParticipantPeerReportQualityAudioProducerCumulativeQualityMos(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityAudioProducerCumulativeRTT(BaseModel):
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    api_100ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="100ms_or_greater_event_fraction", default=None
    )

    api_250ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="250ms_or_greater_event_fraction", default=None
    )

    api_500ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="500ms_or_greater_event_fraction", default=None
    )

    avg: Optional[float] = None


class DataParticipantPeerReportQualityAudioProducerCumulative(BaseModel):
    """Aggregated outbound (producer) audio statistics for the session."""

    packet_loss: Optional[DataParticipantPeerReportQualityAudioProducerCumulativePacketLoss] = None
    """Cumulative packet loss distribution."""

    quality_mos: Optional[DataParticipantPeerReportQualityAudioProducerCumulativeQualityMos] = None
    """Distribution summary with average and percentiles."""

    rtt: Optional[DataParticipantPeerReportQualityAudioProducerCumulativeRTT] = None
    """Cumulative latency distribution (milliseconds-based thresholds)."""


class DataParticipantPeerReportQualityScreenshareAudioConsumer(BaseModel):
    """Per-sample inbound (consumer) audio statistics."""

    bytes_received: Optional[float] = None

    concealment_events: Optional[float] = None

    consumer_id: Optional[str] = None

    jitter: Optional[float] = None

    jitter_buffer_delay: Optional[float] = None

    jitter_buffer_emitted_count: Optional[float] = None

    mid: Optional[str] = None

    mos_quality: Optional[float] = None

    packets_lost: Optional[float] = None

    packets_received: Optional[float] = None

    peer_id: Optional[str] = None

    producer_id: Optional[str] = None

    ssrc: Optional[float] = None

    timestamp: Optional[str] = None


class DataParticipantPeerReportQualityScreenshareAudioConsumerCumulativeJitterBufferDelay(BaseModel):
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    api_100ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="100ms_or_greater_event_fraction", default=None
    )

    api_250ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="250ms_or_greater_event_fraction", default=None
    )

    api_500ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="500ms_or_greater_event_fraction", default=None
    )

    avg: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareAudioConsumerCumulativePacketLoss(BaseModel):
    """Cumulative packet loss distribution."""

    api_10_or_greater_event_fraction: Optional[float] = FieldInfo(alias="10_or_greater_event_fraction", default=None)

    api_25_or_greater_event_fraction: Optional[float] = FieldInfo(alias="25_or_greater_event_fraction", default=None)

    api_5_or_greater_event_fraction: Optional[float] = FieldInfo(alias="5_or_greater_event_fraction", default=None)

    api_50_or_greater_event_fraction: Optional[float] = FieldInfo(alias="50_or_greater_event_fraction", default=None)

    avg: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareAudioConsumerCumulativeQualityMos(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareAudioConsumerCumulative(BaseModel):
    """Aggregated inbound (consumer) audio statistics for the session."""

    jitter_buffer_delay: Optional[
        DataParticipantPeerReportQualityScreenshareAudioConsumerCumulativeJitterBufferDelay
    ] = None
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    packet_loss: Optional[DataParticipantPeerReportQualityScreenshareAudioConsumerCumulativePacketLoss] = None
    """Cumulative packet loss distribution."""

    quality_mos: Optional[DataParticipantPeerReportQualityScreenshareAudioConsumerCumulativeQualityMos] = None
    """Distribution summary with average and percentiles."""


class DataParticipantPeerReportQualityScreenshareAudioProducer(BaseModel):
    """Per-sample outbound (producer) audio statistics."""

    bytes_sent: Optional[float] = None

    jitter: Optional[float] = None

    mid: Optional[str] = None

    mos_quality: Optional[float] = None

    packets_lost: Optional[float] = None

    packets_sent: Optional[float] = None

    producer_id: Optional[str] = None

    rtt: Optional[float] = None

    ssrc: Optional[float] = None

    timestamp: Optional[str] = None


class DataParticipantPeerReportQualityScreenshareAudioProducerCumulativePacketLoss(BaseModel):
    """Cumulative packet loss distribution."""

    api_10_or_greater_event_fraction: Optional[float] = FieldInfo(alias="10_or_greater_event_fraction", default=None)

    api_25_or_greater_event_fraction: Optional[float] = FieldInfo(alias="25_or_greater_event_fraction", default=None)

    api_5_or_greater_event_fraction: Optional[float] = FieldInfo(alias="5_or_greater_event_fraction", default=None)

    api_50_or_greater_event_fraction: Optional[float] = FieldInfo(alias="50_or_greater_event_fraction", default=None)

    avg: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareAudioProducerCumulativeQualityMos(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareAudioProducerCumulativeRTT(BaseModel):
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    api_100ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="100ms_or_greater_event_fraction", default=None
    )

    api_250ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="250ms_or_greater_event_fraction", default=None
    )

    api_500ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="500ms_or_greater_event_fraction", default=None
    )

    avg: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareAudioProducerCumulative(BaseModel):
    """Aggregated outbound (producer) audio statistics for the session."""

    packet_loss: Optional[DataParticipantPeerReportQualityScreenshareAudioProducerCumulativePacketLoss] = None
    """Cumulative packet loss distribution."""

    quality_mos: Optional[DataParticipantPeerReportQualityScreenshareAudioProducerCumulativeQualityMos] = None
    """Distribution summary with average and percentiles."""

    rtt: Optional[DataParticipantPeerReportQualityScreenshareAudioProducerCumulativeRTT] = None
    """Cumulative latency distribution (milliseconds-based thresholds)."""


class DataParticipantPeerReportQualityScreenshareVideoConsumer(BaseModel):
    """Per-sample inbound (consumer) video statistics."""

    bytes_received: Optional[float] = None

    consumer_id: Optional[str] = None

    fir_count: Optional[float] = None

    frame_height: Optional[float] = None

    frame_width: Optional[float] = None

    frames_decoded: Optional[float] = None

    frames_dropped: Optional[float] = None

    frames_per_second: Optional[float] = None

    jitter: Optional[float] = None

    jitter_buffer_delay: Optional[float] = None

    jitter_buffer_emitted_count: Optional[float] = None

    key_frames_decoded: Optional[float] = None

    mid: Optional[str] = None

    mos_quality: Optional[float] = None

    packets_lost: Optional[float] = None

    packets_received: Optional[float] = None

    peer_id: Optional[str] = None

    producer_id: Optional[str] = None

    ssrc: Optional[float] = None

    timestamp: Optional[str] = None


class DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeFramePerSecond(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeFrameWidth(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeIssues(BaseModel):
    lag_fraction: Optional[float] = None

    no_video_fraction: Optional[float] = None

    poor_resolution_fraction: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeJitterBufferDelay(BaseModel):
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    api_100ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="100ms_or_greater_event_fraction", default=None
    )

    api_250ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="250ms_or_greater_event_fraction", default=None
    )

    api_500ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="500ms_or_greater_event_fraction", default=None
    )

    avg: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativePacketLoss(BaseModel):
    """Cumulative packet loss distribution."""

    api_10_or_greater_event_fraction: Optional[float] = FieldInfo(alias="10_or_greater_event_fraction", default=None)

    api_25_or_greater_event_fraction: Optional[float] = FieldInfo(alias="25_or_greater_event_fraction", default=None)

    api_5_or_greater_event_fraction: Optional[float] = FieldInfo(alias="5_or_greater_event_fraction", default=None)

    api_50_or_greater_event_fraction: Optional[float] = FieldInfo(alias="50_or_greater_event_fraction", default=None)

    avg: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeQualityMos(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoConsumerCumulative(BaseModel):
    """Aggregated inbound (consumer) video statistics for the session."""

    frame_per_second: Optional[DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeFramePerSecond] = None
    """Distribution summary with average and percentiles."""

    frame_width: Optional[DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeFrameWidth] = None
    """Distribution summary with average and percentiles."""

    issues: Optional[DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeIssues] = None

    jitter_buffer_delay: Optional[
        DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeJitterBufferDelay
    ] = None
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    key_frames_decoded_fraction: Optional[float] = None

    packet_loss: Optional[DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativePacketLoss] = None
    """Cumulative packet loss distribution."""

    quality_mos: Optional[DataParticipantPeerReportQualityScreenshareVideoConsumerCumulativeQualityMos] = None
    """Distribution summary with average and percentiles."""


class DataParticipantPeerReportQualityScreenshareVideoProducerQualityLimitationDurations(BaseModel):
    bandwidth: Optional[float] = None

    cpu: Optional[float] = None

    none: Optional[float] = None

    other: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoProducer(BaseModel):
    """Per-sample outbound (producer) video statistics."""

    bytes_sent: Optional[float] = None

    fir_count: Optional[float] = None

    frame_height: Optional[float] = None

    frame_width: Optional[float] = None

    frames_encoded: Optional[float] = None

    frames_per_second: Optional[float] = None

    jitter: Optional[float] = None

    key_frames_encoded: Optional[float] = None

    mid: Optional[str] = None

    mos_quality: Optional[float] = None

    packets_lost: Optional[float] = None

    packets_sent: Optional[float] = None

    pli_count: Optional[float] = None

    producer_id: Optional[str] = None

    quality_limitation_durations: Optional[
        DataParticipantPeerReportQualityScreenshareVideoProducerQualityLimitationDurations
    ] = None

    quality_limitation_reason: Optional[Literal["cpu", "bandwidth", "none", "other"]] = None

    quality_limitation_resolution_changes: Optional[float] = None

    rtt: Optional[float] = None

    ssrc: Optional[float] = None

    timestamp: Optional[str] = None


class DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeFramePerSecond(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeFrameWidth(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeIssues(BaseModel):
    bandwidth_quality_limitation_fraction: Optional[float] = None

    cpu_quality_limitation_fraction: Optional[float] = None

    no_video_fraction: Optional[float] = None

    poor_resolution_fraction: Optional[float] = None

    quality_limitation_fraction: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoProducerCumulativePacketLoss(BaseModel):
    """Cumulative packet loss distribution."""

    api_10_or_greater_event_fraction: Optional[float] = FieldInfo(alias="10_or_greater_event_fraction", default=None)

    api_25_or_greater_event_fraction: Optional[float] = FieldInfo(alias="25_or_greater_event_fraction", default=None)

    api_5_or_greater_event_fraction: Optional[float] = FieldInfo(alias="5_or_greater_event_fraction", default=None)

    api_50_or_greater_event_fraction: Optional[float] = FieldInfo(alias="50_or_greater_event_fraction", default=None)

    avg: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeQualityMos(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeRTT(BaseModel):
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    api_100ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="100ms_or_greater_event_fraction", default=None
    )

    api_250ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="250ms_or_greater_event_fraction", default=None
    )

    api_500ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="500ms_or_greater_event_fraction", default=None
    )

    avg: Optional[float] = None


class DataParticipantPeerReportQualityScreenshareVideoProducerCumulative(BaseModel):
    """Aggregated outbound (producer) video statistics for the session."""

    frame_per_second: Optional[DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeFramePerSecond] = None
    """Distribution summary with average and percentiles."""

    frame_width: Optional[DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeFrameWidth] = None
    """Distribution summary with average and percentiles."""

    high_negative_feedback_fraction: Optional[float] = None

    issues: Optional[DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeIssues] = None

    key_frames_encoded_fraction: Optional[float] = None

    packet_loss: Optional[DataParticipantPeerReportQualityScreenshareVideoProducerCumulativePacketLoss] = None
    """Cumulative packet loss distribution."""

    quality_mos: Optional[DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeQualityMos] = None
    """Distribution summary with average and percentiles."""

    rtt: Optional[DataParticipantPeerReportQualityScreenshareVideoProducerCumulativeRTT] = None
    """Cumulative latency distribution (milliseconds-based thresholds)."""


class DataParticipantPeerReportQualityVideoConsumer(BaseModel):
    """Per-sample inbound (consumer) video statistics."""

    bytes_received: Optional[float] = None

    consumer_id: Optional[str] = None

    fir_count: Optional[float] = None

    frame_height: Optional[float] = None

    frame_width: Optional[float] = None

    frames_decoded: Optional[float] = None

    frames_dropped: Optional[float] = None

    frames_per_second: Optional[float] = None

    jitter: Optional[float] = None

    jitter_buffer_delay: Optional[float] = None

    jitter_buffer_emitted_count: Optional[float] = None

    key_frames_decoded: Optional[float] = None

    mid: Optional[str] = None

    mos_quality: Optional[float] = None

    packets_lost: Optional[float] = None

    packets_received: Optional[float] = None

    peer_id: Optional[str] = None

    producer_id: Optional[str] = None

    ssrc: Optional[float] = None

    timestamp: Optional[str] = None


class DataParticipantPeerReportQualityVideoConsumerCumulativeFramePerSecond(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityVideoConsumerCumulativeFrameWidth(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityVideoConsumerCumulativeIssues(BaseModel):
    lag_fraction: Optional[float] = None

    no_video_fraction: Optional[float] = None

    poor_resolution_fraction: Optional[float] = None


class DataParticipantPeerReportQualityVideoConsumerCumulativeJitterBufferDelay(BaseModel):
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    api_100ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="100ms_or_greater_event_fraction", default=None
    )

    api_250ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="250ms_or_greater_event_fraction", default=None
    )

    api_500ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="500ms_or_greater_event_fraction", default=None
    )

    avg: Optional[float] = None


class DataParticipantPeerReportQualityVideoConsumerCumulativePacketLoss(BaseModel):
    """Cumulative packet loss distribution."""

    api_10_or_greater_event_fraction: Optional[float] = FieldInfo(alias="10_or_greater_event_fraction", default=None)

    api_25_or_greater_event_fraction: Optional[float] = FieldInfo(alias="25_or_greater_event_fraction", default=None)

    api_5_or_greater_event_fraction: Optional[float] = FieldInfo(alias="5_or_greater_event_fraction", default=None)

    api_50_or_greater_event_fraction: Optional[float] = FieldInfo(alias="50_or_greater_event_fraction", default=None)

    avg: Optional[float] = None


class DataParticipantPeerReportQualityVideoConsumerCumulativeQualityMos(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityVideoConsumerCumulative(BaseModel):
    """Aggregated inbound (consumer) video statistics for the session."""

    frame_per_second: Optional[DataParticipantPeerReportQualityVideoConsumerCumulativeFramePerSecond] = None
    """Distribution summary with average and percentiles."""

    frame_width: Optional[DataParticipantPeerReportQualityVideoConsumerCumulativeFrameWidth] = None
    """Distribution summary with average and percentiles."""

    issues: Optional[DataParticipantPeerReportQualityVideoConsumerCumulativeIssues] = None

    jitter_buffer_delay: Optional[DataParticipantPeerReportQualityVideoConsumerCumulativeJitterBufferDelay] = None
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    key_frames_decoded_fraction: Optional[float] = None

    packet_loss: Optional[DataParticipantPeerReportQualityVideoConsumerCumulativePacketLoss] = None
    """Cumulative packet loss distribution."""

    quality_mos: Optional[DataParticipantPeerReportQualityVideoConsumerCumulativeQualityMos] = None
    """Distribution summary with average and percentiles."""


class DataParticipantPeerReportQualityVideoProducerQualityLimitationDurations(BaseModel):
    bandwidth: Optional[float] = None

    cpu: Optional[float] = None

    none: Optional[float] = None

    other: Optional[float] = None


class DataParticipantPeerReportQualityVideoProducer(BaseModel):
    """Per-sample outbound (producer) video statistics."""

    bytes_sent: Optional[float] = None

    fir_count: Optional[float] = None

    frame_height: Optional[float] = None

    frame_width: Optional[float] = None

    frames_encoded: Optional[float] = None

    frames_per_second: Optional[float] = None

    jitter: Optional[float] = None

    key_frames_encoded: Optional[float] = None

    mid: Optional[str] = None

    mos_quality: Optional[float] = None

    packets_lost: Optional[float] = None

    packets_sent: Optional[float] = None

    pli_count: Optional[float] = None

    producer_id: Optional[str] = None

    quality_limitation_durations: Optional[DataParticipantPeerReportQualityVideoProducerQualityLimitationDurations] = (
        None
    )

    quality_limitation_reason: Optional[Literal["cpu", "bandwidth", "none", "other"]] = None

    quality_limitation_resolution_changes: Optional[float] = None

    rtt: Optional[float] = None

    ssrc: Optional[float] = None

    timestamp: Optional[str] = None


class DataParticipantPeerReportQualityVideoProducerCumulativeFramePerSecond(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityVideoProducerCumulativeFrameWidth(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityVideoProducerCumulativeIssues(BaseModel):
    bandwidth_quality_limitation_fraction: Optional[float] = None

    cpu_quality_limitation_fraction: Optional[float] = None

    no_video_fraction: Optional[float] = None

    poor_resolution_fraction: Optional[float] = None

    quality_limitation_fraction: Optional[float] = None


class DataParticipantPeerReportQualityVideoProducerCumulativePacketLoss(BaseModel):
    """Cumulative packet loss distribution."""

    api_10_or_greater_event_fraction: Optional[float] = FieldInfo(alias="10_or_greater_event_fraction", default=None)

    api_25_or_greater_event_fraction: Optional[float] = FieldInfo(alias="25_or_greater_event_fraction", default=None)

    api_5_or_greater_event_fraction: Optional[float] = FieldInfo(alias="5_or_greater_event_fraction", default=None)

    api_50_or_greater_event_fraction: Optional[float] = FieldInfo(alias="50_or_greater_event_fraction", default=None)

    avg: Optional[float] = None


class DataParticipantPeerReportQualityVideoProducerCumulativeQualityMos(BaseModel):
    """Distribution summary with average and percentiles."""

    avg: Optional[float] = None

    p50: Optional[float] = None

    p75: Optional[float] = None

    p90: Optional[float] = None


class DataParticipantPeerReportQualityVideoProducerCumulativeRTT(BaseModel):
    """Cumulative latency distribution (milliseconds-based thresholds)."""

    api_100ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="100ms_or_greater_event_fraction", default=None
    )

    api_250ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="250ms_or_greater_event_fraction", default=None
    )

    api_500ms_or_greater_event_fraction: Optional[float] = FieldInfo(
        alias="500ms_or_greater_event_fraction", default=None
    )

    avg: Optional[float] = None


class DataParticipantPeerReportQualityVideoProducerCumulative(BaseModel):
    """Aggregated outbound (producer) video statistics for the session."""

    frame_per_second: Optional[DataParticipantPeerReportQualityVideoProducerCumulativeFramePerSecond] = None
    """Distribution summary with average and percentiles."""

    frame_width: Optional[DataParticipantPeerReportQualityVideoProducerCumulativeFrameWidth] = None
    """Distribution summary with average and percentiles."""

    high_negative_feedback_fraction: Optional[float] = None

    issues: Optional[DataParticipantPeerReportQualityVideoProducerCumulativeIssues] = None

    key_frames_encoded_fraction: Optional[float] = None

    packet_loss: Optional[DataParticipantPeerReportQualityVideoProducerCumulativePacketLoss] = None
    """Cumulative packet loss distribution."""

    quality_mos: Optional[DataParticipantPeerReportQualityVideoProducerCumulativeQualityMos] = None
    """Distribution summary with average and percentiles."""

    rtt: Optional[DataParticipantPeerReportQualityVideoProducerCumulativeRTT] = None
    """Cumulative latency distribution (milliseconds-based thresholds)."""


class DataParticipantPeerReportQuality(BaseModel):
    """Media quality statistics for the participant."""

    audio_consumer: Optional[List[DataParticipantPeerReportQualityAudioConsumer]] = None

    audio_consumer_cumulative: Optional[DataParticipantPeerReportQualityAudioConsumerCumulative] = None
    """Aggregated inbound (consumer) audio statistics for the session."""

    audio_producer: Optional[List[DataParticipantPeerReportQualityAudioProducer]] = None

    audio_producer_cumulative: Optional[DataParticipantPeerReportQualityAudioProducerCumulative] = None
    """Aggregated outbound (producer) audio statistics for the session."""

    screenshare_audio_consumer: Optional[List[DataParticipantPeerReportQualityScreenshareAudioConsumer]] = None

    screenshare_audio_consumer_cumulative: Optional[
        DataParticipantPeerReportQualityScreenshareAudioConsumerCumulative
    ] = None
    """Aggregated inbound (consumer) audio statistics for the session."""

    screenshare_audio_producer: Optional[List[DataParticipantPeerReportQualityScreenshareAudioProducer]] = None

    screenshare_audio_producer_cumulative: Optional[
        DataParticipantPeerReportQualityScreenshareAudioProducerCumulative
    ] = None
    """Aggregated outbound (producer) audio statistics for the session."""

    screenshare_video_consumer: Optional[List[DataParticipantPeerReportQualityScreenshareVideoConsumer]] = None

    screenshare_video_consumer_cumulative: Optional[
        DataParticipantPeerReportQualityScreenshareVideoConsumerCumulative
    ] = None
    """Aggregated inbound (consumer) video statistics for the session."""

    screenshare_video_producer: Optional[List[DataParticipantPeerReportQualityScreenshareVideoProducer]] = None

    screenshare_video_producer_cumulative: Optional[
        DataParticipantPeerReportQualityScreenshareVideoProducerCumulative
    ] = None
    """Aggregated outbound (producer) video statistics for the session."""

    video_consumer: Optional[List[DataParticipantPeerReportQualityVideoConsumer]] = None

    video_consumer_cumulative: Optional[DataParticipantPeerReportQualityVideoConsumerCumulative] = None
    """Aggregated inbound (consumer) video statistics for the session."""

    video_producer: Optional[List[DataParticipantPeerReportQualityVideoProducer]] = None

    video_producer_cumulative: Optional[DataParticipantPeerReportQualityVideoProducerCumulative] = None
    """Aggregated outbound (producer) video statistics for the session."""


class DataParticipantPeerReport(BaseModel):
    """Peer call statistics report."""

    metadata: Optional[DataParticipantPeerReportMetadata] = None
    """Connection and device metadata for the participant."""

    quality: Optional[DataParticipantPeerReportQuality] = None
    """Media quality statistics for the participant."""


class DataParticipant(BaseModel):
    id: Optional[str] = None
    """ID of the participant."""

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

    peer_events: Optional[List[DataParticipantPeerEvent]] = None
    """Connection lifecycle events for the participant's peer."""

    peer_report: Optional[DataParticipantPeerReport] = None
    """Peer call statistics report."""

    role: Optional[str] = None
    """Name of the preset associated with the participant."""

    session_id: Optional[str] = None

    updated_at: Optional[str] = None
    """timestamp when this participant's data was last updated."""

    user_id: Optional[str] = None
    """User id for this participant."""


class Data(BaseModel):
    participant: Optional[DataParticipant] = None


class SessionGetParticipantDataFromPeerIDResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
