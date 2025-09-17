# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["WorkerEditParams", "Observability", "ObservabilityLogs", "Subdomain", "TailConsumer"]


class WorkerEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    logpush: Required[bool]
    """Whether logpush is enabled for the Worker."""

    name: Required[str]
    """Name of the Worker."""

    observability: Required[Observability]
    """Observability settings for the Worker."""

    subdomain: Required[Subdomain]
    """Subdomain settings for the Worker."""

    tags: Required[SequenceNotStr[str]]
    """Tags associated with the Worker."""

    tail_consumers: Required[Iterable[TailConsumer]]
    """Other Workers that should consume logs from the Worker."""


class ObservabilityLogs(TypedDict, total=False):
    enabled: bool
    """Whether logs are enabled for the Worker."""

    head_sampling_rate: float
    """The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%)."""

    invocation_logs: bool
    """
    Whether
    [invocation logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs)
    are enabled for the Worker.
    """


class Observability(TypedDict, total=False):
    enabled: bool
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: float
    """The sampling rate for observability. From 0 to 1 (1 = 100%, 0.1 = 10%)."""

    logs: ObservabilityLogs
    """Log settings for the Worker."""


class Subdomain(TypedDict, total=False):
    enabled: bool
    """Whether the \\**.workers.dev subdomain is enabled for the Worker."""

    previews_enabled: bool
    """
    Whether
    [preview URLs](https://developers.cloudflare.com/workers/configuration/previews/)
    are enabled for the Worker.
    """


class TailConsumer(TypedDict, total=False):
    name: Required[str]
    """Name of the consumer Worker."""
