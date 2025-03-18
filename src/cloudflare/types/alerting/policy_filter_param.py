# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["PolicyFilterParam"]


class PolicyFilterParam(TypedDict, total=False):
    actions: List[str]
    """Usage depends on specific alert type"""

    affected_asns: List[str]
    """Used for configuring radar_notification"""

    affected_components: List[str]
    """Used for configuring incident_alert"""

    affected_locations: List[str]
    """Used for configuring radar_notification"""

    airport_code: List[str]
    """Used for configuring maintenance_event_notification"""

    alert_trigger_preferences: List[str]
    """Usage depends on specific alert type"""

    alert_trigger_preferences_value: List[str]
    """Usage depends on specific alert type"""

    enabled: List[str]
    """Used for configuring load_balancing_pool_enablement_alert"""

    environment: List[str]
    """Used for configuring pages_event_alert"""

    event: List[str]
    """Used for configuring pages_event_alert"""

    event_source: List[str]
    """Used for configuring load_balancing_health_alert"""

    event_type: List[str]
    """Usage depends on specific alert type"""

    group_by: List[str]
    """Usage depends on specific alert type"""

    health_check_id: List[str]
    """Used for configuring health_check_status_notification"""

    incident_impact: List[
        Literal["INCIDENT_IMPACT_NONE", "INCIDENT_IMPACT_MINOR", "INCIDENT_IMPACT_MAJOR", "INCIDENT_IMPACT_CRITICAL"]
    ]
    """Used for configuring incident_alert"""

    input_id: List[str]
    """Used for configuring stream_live_notifications"""

    insight_class: List[str]
    """Used for configuring security_insights_alert"""

    limit: List[str]
    """Used for configuring billing_usage_alert"""

    logo_tag: List[str]
    """Used for configuring logo_match_alert"""

    megabits_per_second: List[str]
    """Used for configuring advanced_ddos_attack_l4_alert"""

    new_health: List[str]
    """Used for configuring load_balancing_health_alert"""

    new_status: List[str]
    """Used for configuring tunnel_health_event"""

    packets_per_second: List[str]
    """Used for configuring advanced_ddos_attack_l4_alert"""

    pool_id: List[str]
    """Usage depends on specific alert type"""

    pop_names: List[str]
    """Usage depends on specific alert type"""

    product: List[str]
    """Used for configuring billing_usage_alert"""

    project_id: List[str]
    """Used for configuring pages_event_alert"""

    protocol: List[str]
    """Used for configuring advanced_ddos_attack_l4_alert"""

    query_tag: List[str]
    """Usage depends on specific alert type"""

    requests_per_second: List[str]
    """Used for configuring advanced_ddos_attack_l7_alert"""

    selectors: List[str]
    """Usage depends on specific alert type"""

    services: List[str]
    """Used for configuring clickhouse_alert_fw_ent_anomaly"""

    slo: List[str]
    """Usage depends on specific alert type"""

    status: List[str]
    """Used for configuring health_check_status_notification"""

    target_hostname: List[str]
    """Used for configuring advanced_ddos_attack_l7_alert"""

    target_ip: List[str]
    """Used for configuring advanced_ddos_attack_l4_alert"""

    target_zone_name: List[str]
    """Used for configuring advanced_ddos_attack_l7_alert"""

    traffic_exclusions: List[Literal["security_events"]]
    """Used for configuring traffic_anomalies_alert"""

    tunnel_id: List[str]
    """Used for configuring tunnel_health_event"""

    tunnel_name: List[str]
    """Usage depends on specific alert type"""

    where: List[str]
    """Usage depends on specific alert type"""

    zones: List[str]
    """Usage depends on specific alert type"""
