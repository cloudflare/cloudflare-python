# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SessionGetParticipantDataFromPeerIDResponse",
    "Data",
    "DataParticipant",
    "DataParticipantPeerReport",
    "DataParticipantPeerReportMetadata",
    "DataParticipantPeerReportMetadataBrowserMetadata",
    "DataParticipantPeerReportMetadataCandidatePairs",
    "DataParticipantPeerReportMetadataCandidatePairsProducingTransport",
    "DataParticipantPeerReportMetadataDeviceInfo",
    "DataParticipantPeerReportMetadataEvent",
    "DataParticipantPeerReportMetadataIPInformation",
    "DataParticipantPeerReportMetadataIPInformationASN",
    "DataParticipantPeerReportMetadataPcMetadata",
    "DataParticipantPeerReportQuality",
    "DataParticipantPeerReportQualityAudioProducer",
    "DataParticipantPeerReportQualityAudioProducerCumulative",
    "DataParticipantPeerReportQualityAudioProducerCumulativePacketLoss",
    "DataParticipantPeerReportQualityAudioProducerCumulativeQualityMos",
    "DataParticipantPeerReportQualityAudioProducerCumulativeRTT",
    "DataParticipantPeerStats",
    "DataParticipantPeerStatsDeviceInfo",
    "DataParticipantPeerStatsEvent",
    "DataParticipantPeerStatsEventMetadata",
    "DataParticipantPeerStatsEventMetadataConnectionInfo",
    "DataParticipantPeerStatsEventMetadataConnectionInfoConnectivity",
    "DataParticipantPeerStatsEventMetadataConnectionInfoIPDetails",
    "DataParticipantPeerStatsEventMetadataConnectionInfoIPDetailsASN",
    "DataParticipantPeerStatsEventMetadataConnectionInfoLocation",
    "DataParticipantPeerStatsEventMetadataConnectionInfoLocationCoords",
    "DataParticipantPeerStatsIPInformation",
    "DataParticipantPeerStatsIPInformationASN",
    "DataParticipantPeerStatsPrecallNetworkInformation",
    "DataParticipantQualityStats",
]


class DataParticipantPeerReportMetadataBrowserMetadata(BaseModel):
    browser: Optional[str] = None

    browser_version: Optional[str] = None

    engine: Optional[str] = None

    user_agent: Optional[str] = None

    webgl_support: Optional[str] = None


class DataParticipantPeerReportMetadataCandidatePairsProducingTransport(BaseModel):
    available_outgoing_bitrate: Optional[int] = None

    bytes_discarded_on_send: Optional[int] = None

    bytes_received: Optional[int] = None

    bytes_sent: Optional[int] = None

    current_round_trip_time: Optional[float] = None

    last_packet_received_timestamp: Optional[int] = None

    last_packet_sent_timestamp: Optional[int] = None

    local_candidate_address: Optional[str] = None

    local_candidate_id: Optional[str] = None

    local_candidate_network_type: Optional[str] = None

    local_candidate_port: Optional[int] = None

    local_candidate_protocol: Optional[str] = None

    local_candidate_related_address: Optional[str] = None

    local_candidate_related_port: Optional[int] = None

    local_candidate_type: Optional[str] = None

    nominated: Optional[bool] = None

    packets_discarded_on_send: Optional[int] = None

    packets_received: Optional[int] = None

    packets_sent: Optional[int] = None

    remote_candidate_address: Optional[str] = None

    remote_candidate_id: Optional[str] = None

    remote_candidate_port: Optional[int] = None

    remote_candidate_protocol: Optional[str] = None

    remote_candidate_type: Optional[str] = None

    total_round_trip_time: Optional[float] = None


class DataParticipantPeerReportMetadataCandidatePairs(BaseModel):
    consuming_transport: Optional[List[object]] = None

    producing_transport: Optional[List[DataParticipantPeerReportMetadataCandidatePairsProducingTransport]] = None


class DataParticipantPeerReportMetadataDeviceInfo(BaseModel):
    cpus: Optional[int] = None

    is_mobile: Optional[bool] = None

    os: Optional[str] = None

    os_version: Optional[str] = None


class DataParticipantPeerReportMetadataEvent(BaseModel):
    name: Optional[str] = None

    timestamp: Optional[str] = None


class DataParticipantPeerReportMetadataIPInformationASN(BaseModel):
    asn: Optional[str] = None


class DataParticipantPeerReportMetadataIPInformation(BaseModel):
    asn: Optional[DataParticipantPeerReportMetadataIPInformationASN] = None

    city: Optional[str] = None

    country: Optional[str] = None

    ipv4: Optional[str] = None

    region: Optional[str] = None

    timezone: Optional[str] = None


class DataParticipantPeerReportMetadataPcMetadata(BaseModel):
    effective_network_type: Optional[str] = None

    reflexive_connectivity: Optional[bool] = None

    relay_connectivity: Optional[bool] = None

    timestamp: Optional[str] = None

    turn_connectivity: Optional[bool] = None


class DataParticipantPeerReportMetadata(BaseModel):
    audio_devices_updates: Optional[List[object]] = None

    browser_metadata: Optional[DataParticipantPeerReportMetadataBrowserMetadata] = None

    candidate_pairs: Optional[DataParticipantPeerReportMetadataCandidatePairs] = None

    device_info: Optional[DataParticipantPeerReportMetadataDeviceInfo] = None

    events: Optional[List[DataParticipantPeerReportMetadataEvent]] = None

    ip_information: Optional[DataParticipantPeerReportMetadataIPInformation] = None

    pc_metadata: Optional[List[DataParticipantPeerReportMetadataPcMetadata]] = None

    room_view_type: Optional[str] = None

    sdk_name: Optional[str] = None

    sdk_version: Optional[str] = None

    selected_device_updates: Optional[List[object]] = None

    speaker_devices_updates: Optional[List[object]] = None

    video_devices_updates: Optional[List[object]] = None


class DataParticipantPeerReportQualityAudioProducer(BaseModel):
    bytes_sent: Optional[int] = None

    jitter: Optional[int] = None

    mid: Optional[str] = None

    mos_quality: Optional[int] = None

    packets_lost: Optional[int] = None

    packets_sent: Optional[int] = None

    producer_id: Optional[str] = None

    rtt: Optional[float] = None

    ssrc: Optional[int] = None

    timestamp: Optional[str] = None


class DataParticipantPeerReportQualityAudioProducerCumulativePacketLoss(BaseModel):
    api_10_or_greater_event_fraction: Optional[int] = FieldInfo(alias="10_or_greater_event_fraction", default=None)

    api_25_or_greater_event_fraction: Optional[int] = FieldInfo(alias="25_or_greater_event_fraction", default=None)

    api_5_or_greater_event_fraction: Optional[int] = FieldInfo(alias="5_or_greater_event_fraction", default=None)

    api_50_or_greater_event_fraction: Optional[int] = FieldInfo(alias="50_or_greater_event_fraction", default=None)

    avg: Optional[int] = None


class DataParticipantPeerReportQualityAudioProducerCumulativeQualityMos(BaseModel):
    avg: Optional[int] = None

    p50: Optional[int] = None

    p75: Optional[int] = None

    p90: Optional[int] = None


class DataParticipantPeerReportQualityAudioProducerCumulativeRTT(BaseModel):
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
    packet_loss: Optional[DataParticipantPeerReportQualityAudioProducerCumulativePacketLoss] = None

    quality_mos: Optional[DataParticipantPeerReportQualityAudioProducerCumulativeQualityMos] = None

    rtt: Optional[DataParticipantPeerReportQualityAudioProducerCumulativeRTT] = None


class DataParticipantPeerReportQuality(BaseModel):
    audio_consumer: Optional[List[object]] = None

    audio_consumer_cumulative: Optional[object] = None

    audio_producer: Optional[List[DataParticipantPeerReportQualityAudioProducer]] = None

    audio_producer_cumulative: Optional[DataParticipantPeerReportQualityAudioProducerCumulative] = None

    screenshare_audio_consumer: Optional[List[object]] = None

    screenshare_audio_consumer_cumulative: Optional[object] = None

    screenshare_audio_producer: Optional[List[object]] = None

    screenshare_audio_producer_cumulative: Optional[object] = None

    screenshare_video_consumer: Optional[List[object]] = None

    screenshare_video_consumer_cumulative: Optional[object] = None

    screenshare_video_producer: Optional[List[object]] = None

    screenshare_video_producer_cumulative: Optional[object] = None

    video_consumer: Optional[List[object]] = None

    video_consumer_cumulative: Optional[object] = None

    video_producer: Optional[List[object]] = None

    video_producer_cumulative: Optional[object] = None


class DataParticipantPeerReport(BaseModel):
    metadata: Optional[DataParticipantPeerReportMetadata] = None

    quality: Optional[DataParticipantPeerReportQuality] = None


class DataParticipantPeerStatsDeviceInfo(BaseModel):
    browser: Optional[str] = None

    browser_version: Optional[str] = None

    cpus: Optional[int] = None

    engine: Optional[str] = None

    is_mobile: Optional[bool] = None

    os: Optional[str] = None

    os_version: Optional[str] = None

    sdk_name: Optional[str] = None

    sdk_version: Optional[str] = None

    user_agent: Optional[str] = None

    webgl_support: Optional[str] = None


class DataParticipantPeerStatsEventMetadataConnectionInfoConnectivity(BaseModel):
    host: Optional[bool] = None

    reflexive: Optional[bool] = None

    relay: Optional[bool] = None


class DataParticipantPeerStatsEventMetadataConnectionInfoIPDetailsASN(BaseModel):
    asn: Optional[str] = None


class DataParticipantPeerStatsEventMetadataConnectionInfoIPDetails(BaseModel):
    asn: Optional[DataParticipantPeerStatsEventMetadataConnectionInfoIPDetailsASN] = None

    city: Optional[str] = None

    country: Optional[str] = None

    ip: Optional[str] = None

    loc: Optional[str] = None

    postal: Optional[str] = None

    region: Optional[str] = None

    timezone: Optional[str] = None


class DataParticipantPeerStatsEventMetadataConnectionInfoLocationCoords(BaseModel):
    latitude: Optional[float] = None

    longitude: Optional[float] = None


class DataParticipantPeerStatsEventMetadataConnectionInfoLocation(BaseModel):
    coords: Optional[DataParticipantPeerStatsEventMetadataConnectionInfoLocationCoords] = None


class DataParticipantPeerStatsEventMetadataConnectionInfo(BaseModel):
    backend_r_t_t: Optional[float] = None

    connectivity: Optional[DataParticipantPeerStatsEventMetadataConnectionInfoConnectivity] = None

    effective_network_type: Optional[str] = None

    fractional_loss: Optional[int] = None

    ip_details: Optional[DataParticipantPeerStatsEventMetadataConnectionInfoIPDetails] = None

    jitter: Optional[int] = None

    location: Optional[DataParticipantPeerStatsEventMetadataConnectionInfoLocation] = None

    r_t_t: Optional[float] = None

    throughput: Optional[int] = None

    turn_connectivity: Optional[bool] = None


class DataParticipantPeerStatsEventMetadata(BaseModel):
    connection_info: Optional[DataParticipantPeerStatsEventMetadataConnectionInfo] = None


class DataParticipantPeerStatsEvent(BaseModel):
    metadata: Optional[DataParticipantPeerStatsEventMetadata] = None

    timestamp: Optional[str] = None

    type: Optional[str] = None


class DataParticipantPeerStatsIPInformationASN(BaseModel):
    asn: Optional[str] = None


class DataParticipantPeerStatsIPInformation(BaseModel):
    asn: Optional[DataParticipantPeerStatsIPInformationASN] = None

    city: Optional[str] = None

    country: Optional[str] = None

    ip_location: Optional[str] = None

    ipv4: Optional[str] = None

    org: Optional[str] = None

    region: Optional[str] = None

    timezone: Optional[str] = None


class DataParticipantPeerStatsPrecallNetworkInformation(BaseModel):
    backend_rtt: Optional[float] = None

    effective_networktype: Optional[str] = None

    fractional_loss: Optional[int] = None

    jitter: Optional[int] = None

    reflexive_connectivity: Optional[bool] = None

    relay_connectivity: Optional[bool] = None

    rtt: Optional[float] = None

    throughput: Optional[int] = None

    turn_connectivity: Optional[bool] = None


class DataParticipantPeerStats(BaseModel):
    device_info: Optional[DataParticipantPeerStatsDeviceInfo] = None

    events: Optional[List[DataParticipantPeerStatsEvent]] = None

    ip_information: Optional[DataParticipantPeerStatsIPInformation] = None

    precall_network_information: Optional[DataParticipantPeerStatsPrecallNetworkInformation] = None


class DataParticipantQualityStats(BaseModel):
    audio_bandwidth: Optional[int] = None

    audio_stats: Optional[List[object]] = None

    average_quality: Optional[int] = None

    end: Optional[str] = None

    first_audio_packet_received: Optional[str] = None

    first_video_packet_received: Optional[str] = None

    last_audio_packet_received: Optional[str] = None

    last_video_packet_received: Optional[str] = None

    peer_ids: Optional[List[str]] = None

    start: Optional[str] = None

    total_audio_packets: Optional[int] = None

    total_audio_packets_lost: Optional[int] = None

    total_video_packets: Optional[int] = None

    total_video_packets_lost: Optional[int] = None

    video_bandwidth: Optional[int] = None

    video_stats: Optional[List[object]] = None


class DataParticipant(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    custom_participant_id: Optional[str] = None

    display_name: Optional[str] = None

    duration: Optional[float] = None

    joined_at: Optional[str] = None

    left_at: Optional[str] = None

    peer_report: Optional[DataParticipantPeerReport] = None

    peer_stats: Optional[DataParticipantPeerStats] = None

    quality_stats: Optional[DataParticipantQualityStats] = None

    role: Optional[str] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None


class Data(BaseModel):
    participant: Optional[DataParticipant] = None


class SessionGetParticipantDataFromPeerIDResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
