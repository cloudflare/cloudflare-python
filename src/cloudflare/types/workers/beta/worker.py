# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = [
    "Worker",
    "Observability",
    "ObservabilityLogs",
    "References",
    "ReferencesDispatchNamespaceOutbound",
    "ReferencesDomain",
    "ReferencesDurableObject",
    "ReferencesQueue",
    "ReferencesWorker",
    "Subdomain",
    "TailConsumer",
]


class ObservabilityLogs(BaseModel):
    enabled: Optional[bool] = None
    """Whether logs are enabled for the Worker."""

    head_sampling_rate: Optional[float] = None
    """The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%)."""

    invocation_logs: Optional[bool] = None
    """
    Whether
    [invocation logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs)
    are enabled for the Worker.
    """


class Observability(BaseModel):
    enabled: Optional[bool] = None
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float] = None
    """The sampling rate for observability. From 0 to 1 (1 = 100%, 0.1 = 10%)."""

    logs: Optional[ObservabilityLogs] = None
    """Log settings for the Worker."""


class ReferencesDispatchNamespaceOutbound(BaseModel):
    namespace_id: str
    """ID of the dispatch namespace."""

    namespace_name: str
    """Name of the dispatch namespace."""

    worker_id: str
    """ID of the Worker using the dispatch namespace."""

    worker_name: str
    """Name of the Worker using the dispatch namespace."""


class ReferencesDomain(BaseModel):
    id: str
    """ID of the custom domain."""

    certificate_id: str
    """ID of the TLS certificate issued for the custom domain."""

    hostname: str
    """Full hostname of the custom domain, including the zone name."""

    zone_id: str
    """ID of the zone."""

    zone_name: str
    """Name of the zone."""


class ReferencesDurableObject(BaseModel):
    namespace_id: str
    """ID of the Durable Object namespace being used."""

    namespace_name: str
    """Name of the Durable Object namespace being used."""

    worker_id: str
    """ID of the Worker using the Durable Object implementation."""

    worker_name: str
    """Name of the Worker using the Durable Object implementation."""


class ReferencesQueue(BaseModel):
    queue_consumer_id: str
    """ID of the queue consumer configuration."""

    queue_id: str
    """ID of the queue."""

    queue_name: str
    """Name of the queue."""


class ReferencesWorker(BaseModel):
    id: str
    """ID of the referencing Worker."""

    name: str
    """Name of the referencing Worker."""


class References(BaseModel):
    dispatch_namespace_outbounds: List[ReferencesDispatchNamespaceOutbound]
    """
    Other Workers that reference the Worker as an outbound for a dispatch namespace.
    """

    domains: List[ReferencesDomain]
    """Custom domains connected to the Worker."""

    durable_objects: List[ReferencesDurableObject]
    """Other Workers that reference Durable Object classes implemented by the Worker."""

    queues: List[ReferencesQueue]
    """Queues that send messages to the Worker."""

    workers: List[ReferencesWorker]
    """
    Other Workers that reference the Worker using
    [service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/).
    """


class Subdomain(BaseModel):
    enabled: Optional[bool] = None
    """Whether the \\**.workers.dev subdomain is enabled for the Worker."""

    previews_enabled: Optional[bool] = None
    """
    Whether
    [preview URLs](https://developers.cloudflare.com/workers/configuration/previews/)
    are enabled for the Worker.
    """


class TailConsumer(BaseModel):
    name: str
    """Name of the consumer Worker."""


class Worker(BaseModel):
    id: str
    """Immutable ID of the Worker."""

    created_on: datetime
    """When the Worker was created."""

    logpush: bool
    """Whether logpush is enabled for the Worker."""

    name: str
    """Name of the Worker."""

    observability: Observability
    """Observability settings for the Worker."""

    references: References
    """Other resources that reference the Worker and depend on it existing."""

    subdomain: Subdomain
    """Subdomain settings for the Worker."""

    tags: List[str]
    """Tags associated with the Worker."""

    tail_consumers: List[TailConsumer]
    """Other Workers that should consume logs from the Worker."""

    updated_on: datetime
    """When the Worker was most recently updated."""
