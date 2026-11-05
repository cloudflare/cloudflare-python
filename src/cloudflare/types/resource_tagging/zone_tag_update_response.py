# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ZoneTagUpdateResponse",
    "ResourceTaggingTaggedResourceObjectAccessApplication",
    "ResourceTaggingTaggedResourceObjectAccessApplicationPolicy",
    "ResourceTaggingTaggedResourceObjectAccessGroup",
    "ResourceTaggingTaggedResourceObjectAccessServiceToken",
    "ResourceTaggingTaggedResourceObjectAccount",
    "ResourceTaggingTaggedResourceObjectAccountRuleset",
    "ResourceTaggingTaggedResourceObjectAIGateway",
    "ResourceTaggingTaggedResourceObjectAISearchInstance",
    "ResourceTaggingTaggedResourceObjectAISearchNamespace",
    "ResourceTaggingTaggedResourceObjectAlertingPolicy",
    "ResourceTaggingTaggedResourceObjectAlertingWebhook",
    "ResourceTaggingTaggedResourceObjectAPIGatewayOperation",
    "ResourceTaggingTaggedResourceObjectCloudflaredTunnel",
    "ResourceTaggingTaggedResourceObjectCustomCertificate",
    "ResourceTaggingTaggedResourceObjectCustomHostname",
    "ResourceTaggingTaggedResourceObjectCWSDeployment",
    "ResourceTaggingTaggedResourceObjectCWSPolicy",
    "ResourceTaggingTaggedResourceObjectCWSPolicySet",
    "ResourceTaggingTaggedResourceObjectCWSWorkload",
    "ResourceTaggingTaggedResourceObjectD1Database",
    "ResourceTaggingTaggedResourceObjectDevice",
    "ResourceTaggingTaggedResourceObjectDNSRecord",
    "ResourceTaggingTaggedResourceObjectDurableObjectNamespace",
    "ResourceTaggingTaggedResourceObjectGatewayList",
    "ResourceTaggingTaggedResourceObjectGatewayRule",
    "ResourceTaggingTaggedResourceObjectHealthcheck",
    "ResourceTaggingTaggedResourceObjectImage",
    "ResourceTaggingTaggedResourceObjectInfrastructureTarget",
    "ResourceTaggingTaggedResourceObjectKVNamespace",
    "ResourceTaggingTaggedResourceObjectLoadBalancer",
    "ResourceTaggingTaggedResourceObjectLoadBalancerMonitor",
    "ResourceTaggingTaggedResourceObjectLoadBalancerPool",
    "ResourceTaggingTaggedResourceObjectManagedClientCertificate",
    "ResourceTaggingTaggedResourceObjectNamespaceWorker",
    "ResourceTaggingTaggedResourceObjectNamespaceWorkerNavigation",
    "ResourceTaggingTaggedResourceObjectPagesProject",
    "ResourceTaggingTaggedResourceObjectQueue",
    "ResourceTaggingTaggedResourceObjectR2Bucket",
    "ResourceTaggingTaggedResourceObjectResourceShare",
    "ResourceTaggingTaggedResourceObjectStreamLiveInput",
    "ResourceTaggingTaggedResourceObjectStreamVideo",
    "ResourceTaggingTaggedResourceObjectVectorizeIndex",
    "ResourceTaggingTaggedResourceObjectWorker",
    "ResourceTaggingTaggedResourceObjectWorkerRoute",
    "ResourceTaggingTaggedResourceObjectWorkerVersion",
    "ResourceTaggingTaggedResourceObjectZone",
    "ResourceTaggingTaggedResourceObjectZoneRuleset",
]


class ResourceTaggingTaggedResourceObjectAccessApplication(BaseModel):
    """Response for access_application resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["access_application"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAccessApplicationPolicy(BaseModel):
    """Response for access_application_policy resources"""

    id: str
    """Identifies the unique resource."""

    access_application_id: str
    """Access application ID is required only for access_application_policy resources"""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["access_application_policy"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAccessGroup(BaseModel):
    """Response for access_group resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["access_group"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAccessServiceToken(BaseModel):
    """Response for access_service_token resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["access_service_token"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAccount(BaseModel):
    """Response for account resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["account"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAccountRuleset(BaseModel):
    """Response for account_ruleset resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["account_ruleset"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAIGateway(BaseModel):
    """Response for ai_gateway resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["ai_gateway"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAISearchInstance(BaseModel):
    """Response for ai_search_instance resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["ai_search_instance"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAISearchNamespace(BaseModel):
    """Response for ai_search_namespace resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["ai_search_namespace"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAlertingPolicy(BaseModel):
    """Response for alerting_policy resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["alerting_policy"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAlertingWebhook(BaseModel):
    """Response for alerting_webhook resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["alerting_webhook"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectAPIGatewayOperation(BaseModel):
    """Response for api_gateway_operation resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["api_gateway_operation"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectCloudflaredTunnel(BaseModel):
    """Response for cloudflared_tunnel resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["cloudflared_tunnel"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectCustomCertificate(BaseModel):
    """Response for custom_certificate resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["custom_certificate"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectCustomHostname(BaseModel):
    """Response for custom_hostname resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["custom_hostname"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectCWSDeployment(BaseModel):
    """Response for cws_deployment resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["cws_deployment"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectCWSPolicy(BaseModel):
    """Response for cws_policy resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["cws_policy"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectCWSPolicySet(BaseModel):
    """Response for cws_policy_set resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["cws_policy_set"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectCWSWorkload(BaseModel):
    """Response for cws_workload resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["cws_workload"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectD1Database(BaseModel):
    """Response for d1_database resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["d1_database"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectDevice(BaseModel):
    """Response for device resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["device"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectDNSRecord(BaseModel):
    """Response for dns_record resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["dns_record"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectDurableObjectNamespace(BaseModel):
    """Response for durable_object_namespace resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["durable_object_namespace"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectGatewayList(BaseModel):
    """Response for gateway_list resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["gateway_list"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectGatewayRule(BaseModel):
    """Response for gateway_rule resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["gateway_rule"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectHealthcheck(BaseModel):
    """Response for healthcheck resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["healthcheck"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectImage(BaseModel):
    """Response for image resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["image"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectInfrastructureTarget(BaseModel):
    """Response for infrastructure_target resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["infrastructure_target"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectKVNamespace(BaseModel):
    """Response for kv_namespace resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["kv_namespace"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectLoadBalancer(BaseModel):
    """Response for load_balancer resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["load_balancer"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectLoadBalancerMonitor(BaseModel):
    """Response for load_balancer_monitor resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["load_balancer_monitor"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectLoadBalancerPool(BaseModel):
    """Response for load_balancer_pool resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["load_balancer_pool"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectManagedClientCertificate(BaseModel):
    """Response for managed_client_certificate resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["managed_client_certificate"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectNamespaceWorkerNavigation(BaseModel):
    """
    Read-only routing metadata resolved from EWC using the account and immutable
    namespace Worker ID. Returned only by tagged-resource lists requested with
    include_navigation=true. Omitted when lookup is unavailable or the child
    has been deleted. Never supplied on tag writes or stored as extra_data.
    """

    namespace_id: str

    namespace_name: str

    script_name: str


class ResourceTaggingTaggedResourceObjectNamespaceWorker(BaseModel):
    """Response for namespace_worker resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["namespace_worker"]

    navigation: Optional[ResourceTaggingTaggedResourceObjectNamespaceWorkerNavigation] = None
    """
    Read-only routing metadata resolved from EWC using the account and immutable
    namespace Worker ID. Returned only by tagged-resource lists requested with
    include_navigation=true. Omitted when lookup is unavailable or the child has
    been deleted. Never supplied on tag writes or stored as extra_data.
    """

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectPagesProject(BaseModel):
    """Response for pages_project resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["pages_project"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectQueue(BaseModel):
    """Response for queue resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["queue"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectR2Bucket(BaseModel):
    """Response for r2_bucket resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["r2_bucket"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectResourceShare(BaseModel):
    """Response for resource_share resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["resource_share"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectStreamLiveInput(BaseModel):
    """Response for stream_live_input resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["stream_live_input"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectStreamVideo(BaseModel):
    """Response for stream_video resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["stream_video"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectVectorizeIndex(BaseModel):
    """Response for vectorize_index resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["vectorize_index"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectWorker(BaseModel):
    """Response for worker resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["worker"]

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectWorkerRoute(BaseModel):
    """Response for worker_route resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["worker_route"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectWorkerVersion(BaseModel):
    """Response for worker_version resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["worker_version"]

    worker_id: str
    """Worker ID is required only for worker_version resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectZone(BaseModel):
    """Response for zone resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["zone"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


class ResourceTaggingTaggedResourceObjectZoneRuleset(BaseModel):
    """Response for zone_ruleset resources"""

    id: str
    """Identifies the unique resource."""

    etag: str
    """ETag identifier for optimistic concurrency control.

    Formatted as "v1:<hash>" where the hash is the base64url-encoded SHA-256
    (truncated to 128 bits) of the tags map canonicalized using RFC 8785 (JSON
    Canonicalization Scheme). Clients should treat ETags as opaque strings and pass
    them back via the If-Match header on write operations.
    """

    name: str
    """Human-readable name of the resource."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags.

    Keys may contain at most 256 characters. Values may contain at most 1024
    characters and may be empty for key-only tags.
    """

    type: Literal["zone_ruleset"]

    zone_id: str
    """Zone ID is required only for zone-level resources"""

    tags_updated_at: Optional[datetime] = None
    """
    Monotonic version of the resource's tags: the timestamp assigned when the tags
    were last written. Returned by read endpoints, by 2PC prepare (the version that
    will be assigned on commit, unless a concurrent write lands first, in which case
    a newer version is assigned), and by 2PC commit (the authoritative committed
    version). Omitted for untagged resources and delete commits: a deleted resource
    has no current version, and deletions are ordered by event order rather than by
    version.
    """


ZoneTagUpdateResponse: TypeAlias = Annotated[
    Union[
        ResourceTaggingTaggedResourceObjectAccessApplication,
        ResourceTaggingTaggedResourceObjectAccessApplicationPolicy,
        ResourceTaggingTaggedResourceObjectAccessGroup,
        ResourceTaggingTaggedResourceObjectAccessServiceToken,
        ResourceTaggingTaggedResourceObjectAccount,
        ResourceTaggingTaggedResourceObjectAccountRuleset,
        ResourceTaggingTaggedResourceObjectAIGateway,
        ResourceTaggingTaggedResourceObjectAISearchInstance,
        ResourceTaggingTaggedResourceObjectAISearchNamespace,
        ResourceTaggingTaggedResourceObjectAlertingPolicy,
        ResourceTaggingTaggedResourceObjectAlertingWebhook,
        ResourceTaggingTaggedResourceObjectAPIGatewayOperation,
        ResourceTaggingTaggedResourceObjectCloudflaredTunnel,
        ResourceTaggingTaggedResourceObjectCustomCertificate,
        ResourceTaggingTaggedResourceObjectCustomHostname,
        ResourceTaggingTaggedResourceObjectCWSDeployment,
        ResourceTaggingTaggedResourceObjectCWSPolicy,
        ResourceTaggingTaggedResourceObjectCWSPolicySet,
        ResourceTaggingTaggedResourceObjectCWSWorkload,
        ResourceTaggingTaggedResourceObjectD1Database,
        ResourceTaggingTaggedResourceObjectDevice,
        ResourceTaggingTaggedResourceObjectDNSRecord,
        ResourceTaggingTaggedResourceObjectDurableObjectNamespace,
        ResourceTaggingTaggedResourceObjectGatewayList,
        ResourceTaggingTaggedResourceObjectGatewayRule,
        ResourceTaggingTaggedResourceObjectHealthcheck,
        ResourceTaggingTaggedResourceObjectImage,
        ResourceTaggingTaggedResourceObjectInfrastructureTarget,
        ResourceTaggingTaggedResourceObjectKVNamespace,
        ResourceTaggingTaggedResourceObjectLoadBalancer,
        ResourceTaggingTaggedResourceObjectLoadBalancerMonitor,
        ResourceTaggingTaggedResourceObjectLoadBalancerPool,
        ResourceTaggingTaggedResourceObjectManagedClientCertificate,
        ResourceTaggingTaggedResourceObjectNamespaceWorker,
        ResourceTaggingTaggedResourceObjectPagesProject,
        ResourceTaggingTaggedResourceObjectQueue,
        ResourceTaggingTaggedResourceObjectR2Bucket,
        ResourceTaggingTaggedResourceObjectResourceShare,
        ResourceTaggingTaggedResourceObjectStreamLiveInput,
        ResourceTaggingTaggedResourceObjectStreamVideo,
        ResourceTaggingTaggedResourceObjectVectorizeIndex,
        ResourceTaggingTaggedResourceObjectWorker,
        ResourceTaggingTaggedResourceObjectWorkerRoute,
        ResourceTaggingTaggedResourceObjectWorkerVersion,
        ResourceTaggingTaggedResourceObjectZone,
        ResourceTaggingTaggedResourceObjectZoneRuleset,
    ],
    PropertyInfo(discriminator="type"),
]
