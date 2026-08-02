# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "AccountTagGetResponse",
    "ResourceTaggingTaggedResourceObjectAccessApplication",
    "ResourceTaggingTaggedResourceObjectAccessApplicationPolicy",
    "ResourceTaggingTaggedResourceObjectAccessGroup",
    "ResourceTaggingTaggedResourceObjectAccount",
    "ResourceTaggingTaggedResourceObjectAccountRuleset",
    "ResourceTaggingTaggedResourceObjectAIGateway",
    "ResourceTaggingTaggedResourceObjectAlertingPolicy",
    "ResourceTaggingTaggedResourceObjectAlertingWebhook",
    "ResourceTaggingTaggedResourceObjectAPIGatewayOperation",
    "ResourceTaggingTaggedResourceObjectCloudflaredTunnel",
    "ResourceTaggingTaggedResourceObjectCustomCertificate",
    "ResourceTaggingTaggedResourceObjectCustomHostname",
    "ResourceTaggingTaggedResourceObjectD1Database",
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


AccountTagGetResponse: TypeAlias = Annotated[
    Union[
        ResourceTaggingTaggedResourceObjectAccessApplication,
        ResourceTaggingTaggedResourceObjectAccessApplicationPolicy,
        ResourceTaggingTaggedResourceObjectAccessGroup,
        ResourceTaggingTaggedResourceObjectAccount,
        ResourceTaggingTaggedResourceObjectAccountRuleset,
        ResourceTaggingTaggedResourceObjectAIGateway,
        ResourceTaggingTaggedResourceObjectAlertingPolicy,
        ResourceTaggingTaggedResourceObjectAlertingWebhook,
        ResourceTaggingTaggedResourceObjectAPIGatewayOperation,
        ResourceTaggingTaggedResourceObjectCloudflaredTunnel,
        ResourceTaggingTaggedResourceObjectCustomCertificate,
        ResourceTaggingTaggedResourceObjectCustomHostname,
        ResourceTaggingTaggedResourceObjectD1Database,
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
