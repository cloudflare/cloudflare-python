# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ResourceTaggingListParams"]


class ResourceTaggingListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    id: SequenceNotStr[str]
    """Filter by resource ID.

    Can be repeated up to 50 times to filter by multiple IDs. Example:
    ?id=abc&id=def
    """

    case_insensitive: bool
    """Match `tag` keys and values case-insensitively.

    Stored casing is unchanged. Example:
    ?tag=environment=production&case_insensitive=true
    """

    cursor: str
    """Cursor for pagination."""

    include_navigation: bool
    """Resolve current namespace Worker navigation by immutable child tag.

    Optional read-only navigation is omitted for deleted or unresolved children.
    Lookups are limited to this page, at most five concurrently, with a shared
    two-second budget. Tag identity, ETag, filters and pagination are unchanged;
    name filtering still uses the stored resource name. Defaults to false.
    """

    name: str
    """Filter by resource name.

    Performs a case-insensitive substring match. Example: ?name=my-zone
    """

    tag: SequenceNotStr[str]
    """Filter resources by tag criteria.

    This parameter can be repeated multiple times, with AND logic between
    parameters.

    Supported syntax:

    - **Key-only**: `tag=<key>` - Resource must have the tag key (e.g.,
      `tag=production`)
    - **Key-value**: `tag=<key>=<value>` - Resource must have the tag with specific
      value (e.g., `tag=env=prod`)
    - **Multiple values (OR)**: `tag=<key>=<v1>,<v2>` - Resource must have tag with
      any of the values (e.g., `tag=env=prod,staging`)
    - **Negate key-only**: `tag=!<key>` - Resource must not have the tag key (e.g.,
      `tag=!archived`)
    - **Negate key-value**: `tag=<key>!=<value>` - Resource must not have the tag
      with specific value (e.g., `tag=region!=us-west-1`)

    Multiple tag parameters are combined with AND logic.
    """

    type: List[
        Literal[
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
    ]
    """Filter by resource type.

    Can be repeated to filter by multiple types (OR logic). Example:
    ?type=zone&type=worker
    """
