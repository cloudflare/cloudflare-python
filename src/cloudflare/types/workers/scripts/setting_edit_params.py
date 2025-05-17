# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .consumer_script_param import ConsumerScriptParam

__all__ = ["SettingEditParams", "Observability", "ObservabilityLogs"]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    observability: Optional[Observability]
    """Observability settings for the Worker."""

    tail_consumers: Optional[Iterable[ConsumerScriptParam]]
    """List of Workers that will consume logs from the attached Worker."""


class ObservabilityLogs(TypedDict, total=False):
    enabled: Required[bool]
    """Whether logs are enabled for the Worker."""

    invocation_logs: Required[bool]
    """
    Whether
    [invocation logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs)
    are enabled for the Worker.
    """

    head_sampling_rate: Optional[float]
    """The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1."""


class Observability(TypedDict, total=False):
    enabled: Required[bool]
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float]
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """

    logs: Optional[ObservabilityLogs]
    """Log settings for the Worker."""
