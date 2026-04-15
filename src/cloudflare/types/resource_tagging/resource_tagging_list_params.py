# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ResourceTaggingListParams"]


class ResourceTaggingListParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    cursor: str
    """Cursor for pagination."""

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
    ]
    """Filter by resource type.

    Can be repeated to filter by multiple types (OR logic). Example:
    ?type=zone&type=worker
    """
