# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PolicyFilterParam"]


class PolicyFilterParam(TypedDict, total=False):
    actions: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    affected_asns: SequenceNotStr[str]
    """Used for configuring radar_notification"""

    affected_components: SequenceNotStr[str]
    """Used for configuring incident_alert"""

    affected_locations: SequenceNotStr[str]
    """Used for configuring radar_notification"""

    airport_code: SequenceNotStr[str]
    """Used for configuring maintenance_event_notification"""

    alert_trigger_preferences: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    alert_trigger_preferences_value: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    enabled: SequenceNotStr[str]
    """Used for configuring load_balancing_pool_enablement_alert"""

    environment: SequenceNotStr[str]
    """Used for configuring pages_event_alert"""

    event: SequenceNotStr[str]
    """Used for configuring pages_event_alert"""

    event_source: SequenceNotStr[str]
    """Used for configuring load_balancing_health_alert"""

    event_type: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    group_by: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    health_check_id: SequenceNotStr[str]
    """Used for configuring health_check_status_notification"""

    incident_impact: List[
        Literal["INCIDENT_IMPACT_NONE", "INCIDENT_IMPACT_MINOR", "INCIDENT_IMPACT_MAJOR", "INCIDENT_IMPACT_CRITICAL"]
    ]
    """Used for configuring incident_alert"""

    input_id: SequenceNotStr[str]
    """Used for configuring stream_live_notifications"""

    insight_class: SequenceNotStr[str]
    """Used for configuring security_insights_alert"""

    limit: SequenceNotStr[str]
    """Used for configuring billing_usage_alert"""

    logo_tag: SequenceNotStr[str]
    """Used for configuring logo_match_alert"""

    megabits_per_second: SequenceNotStr[str]
    """Used for configuring advanced_ddos_attack_l4_alert"""

    new_health: SequenceNotStr[str]
    """Used for configuring load_balancing_health_alert"""

    new_status: SequenceNotStr[str]
    """Used for configuring tunnel_health_event"""

    packets_per_second: SequenceNotStr[str]
    """Used for configuring advanced_ddos_attack_l4_alert"""

    pool_id: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    pop_names: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    product: SequenceNotStr[str]
    """Used for configuring billing_usage_alert"""

    project_id: SequenceNotStr[str]
    """Used for configuring pages_event_alert"""

    protocol: SequenceNotStr[str]
    """Used for configuring advanced_ddos_attack_l4_alert"""

    query_tag: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    requests_per_second: SequenceNotStr[str]
    """Used for configuring advanced_ddos_attack_l7_alert"""

    selectors: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    services: SequenceNotStr[str]
    """Used for configuring clickhouse_alert_fw_ent_anomaly"""

    slo: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    status: SequenceNotStr[str]
    """Used for configuring health_check_status_notification"""

    target_hostname: SequenceNotStr[str]
    """Used for configuring advanced_ddos_attack_l7_alert"""

    target_ip: SequenceNotStr[str]
    """Used for configuring advanced_ddos_attack_l4_alert"""

    target_zone_name: SequenceNotStr[str]
    """Used for configuring advanced_ddos_attack_l7_alert"""

    traffic_exclusions: List[Literal["security_events"]]
    """Used for configuring traffic_anomalies_alert"""

    tunnel_id: SequenceNotStr[str]
    """Used for configuring tunnel_health_event"""

    tunnel_name: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    type: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    where: SequenceNotStr[str]
    """Usage depends on specific alert type"""

    zones: SequenceNotStr[str]
    """Usage depends on specific alert type"""
