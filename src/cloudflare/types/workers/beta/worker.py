# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Worker", "Observability", "ObservabilityLogs", "Subdomain", "TailConsumer"]


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
    """Identifier."""

    created_on: datetime
    """When the Worker was created."""

    name: str
    """Name of the Worker."""

    updated_on: datetime
    """When the Worker was most recently updated."""

    logpush: Optional[bool] = None
    """Whether logpush is enabled for the Worker."""

    observability: Optional[Observability] = None
    """Observability settings for the Worker."""

    subdomain: Optional[Subdomain] = None
    """Subdomain settings for the Worker."""

    tags: Optional[List[str]] = None
    """Tags associated with the Worker."""

    tail_consumers: Optional[List[TailConsumer]] = None
    """Other Workers that should consume logs from the Worker."""
