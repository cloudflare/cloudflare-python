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
        "account",
        "account_ruleset",
        "ai_gateway",
        "alerting_policy",
        "alerting_webhook",
        "api_gateway_operation",
        "cloudflared_tunnel",
        "custom_certificate",
        "custom_hostname",
        "d1_database",
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
