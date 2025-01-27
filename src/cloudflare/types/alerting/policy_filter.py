# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PolicyFilter"]


class PolicyFilter(BaseModel):
    actions: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    affected_asns: Optional[List[str]] = None
    """Used for configuring radar_notification"""

    affected_components: Optional[List[str]] = None
    """Used for configuring incident_alert"""

    affected_locations: Optional[List[str]] = None
    """Used for configuring radar_notification"""

    airport_code: Optional[List[str]] = None
    """Used for configuring maintenance_event_notification"""

    alert_trigger_preferences: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    alert_trigger_preferences_value: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    enabled: Optional[List[str]] = None
    """Used for configuring load_balancing_pool_enablement_alert"""

    environment: Optional[List[str]] = None
    """Used for configuring pages_event_alert"""

    event: Optional[List[str]] = None
    """Used for configuring pages_event_alert"""

    event_source: Optional[List[str]] = None
    """Used for configuring load_balancing_health_alert"""

    event_type: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    group_by: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    health_check_id: Optional[List[str]] = None
    """Used for configuring health_check_status_notification"""

    incident_impact: Optional[
        List[
            Literal[
                "INCIDENT_IMPACT_NONE", "INCIDENT_IMPACT_MINOR", "INCIDENT_IMPACT_MAJOR", "INCIDENT_IMPACT_CRITICAL"
            ]
        ]
    ] = None
    """Used for configuring incident_alert"""

    input_id: Optional[List[str]] = None
    """Used for configuring stream_live_notifications"""

    insight_class: Optional[List[str]] = None
    """Used for configuring security_insights_alert"""

    limit: Optional[List[str]] = None
    """Used for configuring billing_usage_alert"""

    logo_tag: Optional[List[str]] = None
    """Used for configuring logo_match_alert"""

    megabits_per_second: Optional[List[str]] = None
    """Used for configuring advanced_ddos_attack_l4_alert"""

    new_health: Optional[List[str]] = None
    """Used for configuring load_balancing_health_alert"""

    new_status: Optional[List[str]] = None
    """Used for configuring tunnel_health_event"""

    packets_per_second: Optional[List[str]] = None
    """Used for configuring advanced_ddos_attack_l4_alert"""

    pool_id: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    pop_names: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    product: Optional[List[str]] = None
    """Used for configuring billing_usage_alert"""

    project_id: Optional[List[str]] = None
    """Used for configuring pages_event_alert"""

    protocol: Optional[List[str]] = None
    """Used for configuring advanced_ddos_attack_l4_alert"""

    query_tag: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    requests_per_second: Optional[List[str]] = None
    """Used for configuring advanced_ddos_attack_l7_alert"""

    selectors: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    services: Optional[List[str]] = None
    """Used for configuring clickhouse_alert_fw_ent_anomaly"""

    slo: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    status: Optional[List[str]] = None
    """Used for configuring health_check_status_notification"""

    target_hostname: Optional[List[str]] = None
    """Used for configuring advanced_ddos_attack_l7_alert"""

    target_ip: Optional[List[str]] = None
    """Used for configuring advanced_ddos_attack_l4_alert"""

    target_zone_name: Optional[List[str]] = None
    """Used for configuring advanced_ddos_attack_l7_alert"""

    traffic_exclusions: Optional[List[Literal["security_events"]]] = None
    """Used for configuring traffic_anomalies_alert"""

    tunnel_id: Optional[List[str]] = None
    """Used for configuring tunnel_health_event"""

    tunnel_name: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    where: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    zones: Optional[List[str]] = None
    """Usage depends on specific alert type"""
