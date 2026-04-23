# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "AccountTagUpdateParams",
    "ResourceTaggingSetTagsRequestAccountLevelWorkerVersion",
    "ResourceTaggingSetTagsRequestAccountLevelBase",
]


class ResourceTaggingSetTagsRequestAccountLevelWorkerVersion(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    resource_id: Required[str]
    """Identifies the unique resource."""

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
    """
    Enum for base account-level resource types (those with no extra required
    fields).
    """

    worker_id: Required[str]
    """Worker ID is required only for worker_version resources"""

    tags: Dict[str, str]
    """Contains key-value pairs of tags."""

    if_match: Annotated[str, PropertyInfo(alias="If-Match")]


class ResourceTaggingSetTagsRequestAccountLevelBase(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    resource_id: Required[str]
    """Identifies the unique resource."""

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
        ]
    ]
    """
    Enum for base account-level resource types (those with no extra required
    fields).
    """

    tags: Dict[str, str]
    """Contains key-value pairs of tags."""

    if_match: Annotated[str, PropertyInfo(alias="If-Match")]


AccountTagUpdateParams: TypeAlias = Union[
    ResourceTaggingSetTagsRequestAccountLevelWorkerVersion, ResourceTaggingSetTagsRequestAccountLevelBase
]
