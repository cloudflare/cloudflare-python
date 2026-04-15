# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ValueListParams"]


class ValueListParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    cursor: str
    """Cursor for pagination."""

    type: Literal[
        "access_application",
        "access_application_policy",
        "access_group",
        "account",
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
        "image",
        "kv_namespace",
        "managed_client_certificate",
        "queue",
        "r2_bucket",
        "resource_share",
        "stream_live_input",
        "stream_video",
        "worker",
        "worker_version",
        "zone",
    ]
    """Filter by resource type."""
