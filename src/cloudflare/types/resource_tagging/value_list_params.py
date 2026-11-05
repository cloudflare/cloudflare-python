# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ValueListParams"]


class ValueListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    cursor: str
    """Cursor for pagination."""

    type: Literal[
        "access_application",
        "access_application_policy",
        "access_group",
        "access_service_token",
        "account",
        "account_ruleset",
        "ai_gateway",
        "ai_search_instance",
        "ai_search_namespace",
        "alerting_policy",
        "alerting_webhook",
        "api_gateway_operation",
        "cloudflared_tunnel",
        "custom_certificate",
        "custom_hostname",
        "cws_deployment",
        "cws_policy",
        "cws_policy_set",
        "cws_workload",
        "d1_database",
        "device",
        "dns_record",
        "durable_object_namespace",
        "gateway_list",
        "gateway_rule",
        "healthcheck",
        "image",
        "infrastructure_target",
        "kv_namespace",
        "load_balancer",
        "load_balancer_monitor",
        "load_balancer_pool",
        "managed_client_certificate",
        "namespace_worker",
        "pages_project",
        "queue",
        "r2_bucket",
        "resource_share",
        "stream_live_input",
        "stream_video",
        "vectorize_index",
        "worker",
        "worker_route",
        "worker_version",
        "zone",
        "zone_ruleset",
    ]
    """Filter by resource type."""
