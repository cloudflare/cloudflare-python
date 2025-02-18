# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .mechanism_param import MechanismParam
from .policy_filter_param import PolicyFilterParam

__all__ = ["PolicyCreateParams"]


class PolicyCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account id"""

    alert_type: Required[
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
            "cloudforce_one_request_notification",
            "custom_analytics",
            "custom_ssl_certificate_event_type",
            "dedicated_ssl_certificate_event_type",
            "device_connectivity_anomaly_alert",
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
            "image_notification",
            "image_resizing_notification",
            "incident_alert",
            "load_balancing_health_alert",
            "load_balancing_pool_enablement_alert",
            "logo_match_alert",
            "magic_tunnel_health_check_event",
            "magic_wan_tunnel_health",
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
            "secondary_dns_warning",
            "secondary_dns_zone_successfully_updated",
            "secondary_dns_zone_validation_warning",
            "security_insights_alert",
            "sentinel_alert",
            "stream_live_notifications",
            "synthetic_test_latency_alert",
            "synthetic_test_low_availability_alert",
            "traffic_anomalies_alert",
            "tunnel_health_event",
            "tunnel_update_event",
            "universal_ssl_event_type",
            "web_analytics_metrics_update",
            "zone_aop_custom_certificate_expiration_type",
        ]
    ]
    """Refers to which event will trigger a Notification dispatch.

    You can use the endpoint to get available alert types which then will give you a
    list of possible values.
    """

    enabled: Required[bool]
    """Whether or not the Notification policy is enabled."""

    mechanisms: Required[MechanismParam]
    """List of IDs that will be used when dispatching a notification.

    IDs for email type will be the email address.
    """

    name: Required[str]
    """Name of the policy."""

    alert_interval: str
    """
    Optional specification of how often to re-alert from the same incident, not
    support on all alert types.
    """

    description: str
    """Optional description for the Notification policy."""

    filters: PolicyFilterParam
    """
    Optional filters that allow you to be alerted only on a subset of events for
    that alert type based on some criteria. This is only available for select alert
    types. See alert type documentation for more details.
    """
