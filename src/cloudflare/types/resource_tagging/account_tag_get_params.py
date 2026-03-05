# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountTagGetParams"]


class AccountTagGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    resource_id: Required[str]
    """The ID of the resource to retrieve tags for."""

    resource_type: Required[
        Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
            "worker_version",
        ]
    ]
    """The type of the resource."""

    worker_id: str
    """Worker identifier. Required for worker_version resources."""
