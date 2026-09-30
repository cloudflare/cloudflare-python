# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "ApplicationEditParams",
    "Configuration",
    "ConfigurationAuthorizedKey",
    "ConfigurationWranglerSSH",
    "Constraints",
    "Observability",
    "ObservabilityLogs",
]


class ApplicationEditParams(TypedDict, total=False):
    account_id: Required[str]

    configuration: Configuration
    """Application configuration fields you can change without creating a rollout."""

    constraints: Constraints

    max_instances: int
    """Maximum number of instances that an autoscaling application can run."""

    observability: Observability
    """Top-level application observability settings.

    Scheduler-backed applications hot-reload these settings across existing
    instances. An existing Durable Object-managed application accepts only
    `logs.enabled` and publishes these settings to runtime metadata without creating
    deployments or rollouts.
    """

    rollout_active_grace_period: int
    """
    Grace period for active instances to stay alive before becoming eligible for
    shutdown signal due to a rollout, in seconds. Defaults to 0.
    """


class ConfigurationAuthorizedKey(TypedDict, total=False):
    """User-provided SSH public key."""

    public_key: Required[str]
    """An SSH public key."""

    name: str
    """Optional human readable name for this key."""


class ConfigurationWranglerSSH(TypedDict, total=False):
    """Configuration properties for connecting with SSH to a container using Wrangler."""

    enabled: bool

    port: int


class Configuration(TypedDict, total=False):
    """Application configuration fields you can change without creating a rollout."""

    authorized_keys: Iterable[ConfigurationAuthorizedKey]

    wrangler_ssh: ConfigurationWranglerSSH
    """Configuration properties for connecting with SSH to a container using Wrangler."""


class Constraints(TypedDict, total=False):
    jurisdiction: str
    """Restricts placement to datacenters in the selected jurisdiction.

    Choose "eu", "fedramp", or "us". When combined with regions, EU supports EEUR
    and WEUR while FedRAMP and US support ENAM and WNAM.
    """

    regions: SequenceNotStr[str]


class ObservabilityLogs(TypedDict, total=False):
    """Observability logging settings."""

    enabled: bool


class Observability(TypedDict, total=False):
    """Top-level application observability settings.

    Scheduler-backed applications
    hot-reload these settings across existing instances. An existing Durable
    Object-managed application accepts only `logs.enabled` and publishes these settings
    to runtime metadata without creating deployments or rollouts.
    """

    logs: ObservabilityLogs
    """Observability logging settings."""
