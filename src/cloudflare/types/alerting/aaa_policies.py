# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AaaPolicies", "Filters", "Mechanisms"]


class Filters(BaseModel):
    actions: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    affected_asns: Optional[List[str]] = None
    """Used for configuring radar_notification"""

    affected_components: Optional[List[str]] = None
    """Used for configuring incident_alert.

    A list of identifiers for each component to monitor.
    """

    affected_locations: Optional[List[str]] = None
    """Used for configuring radar_notification"""

    airport_code: Optional[List[str]] = None
    """Used for configuring maintenance_event_notification"""

    alert_trigger_preferences: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    alert_trigger_preferences_value: Optional[List[Literal["99.0", "98.0", "97.0"]]] = None
    """Used for configuring magic_tunnel_health_check_event"""

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
    """Used for configuring magic_tunnel_health_check_event"""

    where: Optional[List[str]] = None
    """Usage depends on specific alert type"""

    zones: Optional[List[str]] = None
    """Usage depends on specific alert type"""


class Mechanisms(BaseModel):
    id: Union[str, str, None] = None
    """UUID"""


class AaaPolicies(BaseModel):
    id: Optional[str] = None
    """The unique identifier of a notification policy"""

    alert_type: Optional[
        Literal[
            "access_custom_certificate_expiration_type",
            "advanced_ddos_attack_l4_alert",
            "advanced_ddos_attack_l7_alert",
            "advanced_http_alert_error",
            "bgp_hijack_notification",
            "billing_usage_alert",
            "block_notification_block_removed",
            "block_notification_new_block",
            "block_notification_review_rejected",
            "brand_protection_alert",
            "brand_protection_digest",
            "clickhouse_alert_fw_anomaly",
            "clickhouse_alert_fw_ent_anomaly",
            "custom_ssl_certificate_event_type",
            "dedicated_ssl_certificate_event_type",
            "dos_attack_l4",
            "dos_attack_l7",
            "expiring_service_token_alert",
            "failing_logpush_job_disabled_alert",
            "fbm_auto_advertisement",
            "fbm_dosd_attack",
            "fbm_volumetric_attack",
            "health_check_status_notification",
            "hostname_aop_custom_certificate_expiration_type",
            "http_alert_edge_error",
            "http_alert_origin_error",
            "incident_alert",
            "load_balancing_health_alert",
            "load_balancing_pool_enablement_alert",
            "logo_match_alert",
            "magic_tunnel_health_check_event",
            "maintenance_event_notification",
            "mtls_certificate_store_certificate_expiration_type",
            "pages_event_alert",
            "radar_notification",
            "real_origin_monitoring",
            "scriptmonitor_alert_new_code_change_detections",
            "scriptmonitor_alert_new_hosts",
            "scriptmonitor_alert_new_malicious_hosts",
            "scriptmonitor_alert_new_malicious_scripts",
            "scriptmonitor_alert_new_malicious_url",
            "scriptmonitor_alert_new_max_length_resource_url",
            "scriptmonitor_alert_new_resources",
            "secondary_dns_all_primaries_failing",
            "secondary_dns_primaries_failing",
            "secondary_dns_zone_successfully_updated",
            "secondary_dns_zone_validation_warning",
            "sentinel_alert",
            "stream_live_notifications",
            "traffic_anomalies_alert",
            "tunnel_health_event",
            "tunnel_update_event",
            "universal_ssl_event_type",
            "web_analytics_metrics_update",
            "zone_aop_custom_certificate_expiration_type",
        ]
    ] = None
    """Refers to which event will trigger a Notification dispatch.

    You can use the endpoint to get available alert types which then will give you a
    list of possible values.
    """

    created: Optional[datetime] = None

    description: Optional[str] = None
    """Optional description for the Notification policy."""

    enabled: Optional[bool] = None
    """Whether or not the Notification policy is enabled."""

    filters: Optional[Filters] = None
    """
    Optional filters that allow you to be alerted only on a subset of events for
    that alert type based on some criteria. This is only available for select alert
    types. See alert type documentation for more details.
    """

    mechanisms: Optional[Dict[str, List[Mechanisms]]] = None
    """List of IDs that will be used when dispatching a notification.

    IDs for email type will be the email address.
    """

    modified: Optional[datetime] = None

    name: Optional[str] = None
    """Name of the policy."""
