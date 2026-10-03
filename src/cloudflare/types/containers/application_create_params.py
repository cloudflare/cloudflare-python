# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "ApplicationCreateParams",
    "CcContainersCreateScheduledApplicationRequest",
    "CcContainersCreateScheduledApplicationRequestConfiguration",
    "CcContainersCreateScheduledApplicationRequestConfigurationAuthorizedKey",
    "CcContainersCreateScheduledApplicationRequestConfigurationEnvironmentVariable",
    "CcContainersCreateScheduledApplicationRequestConfigurationObservability",
    "CcContainersCreateScheduledApplicationRequestConfigurationObservabilityLogs",
    "CcContainersCreateScheduledApplicationRequestConstraints",
    "CcContainersCreateScheduledApplicationRequestDurableObjects",
    "CcContainersCreateScheduledApplicationRequestDurableObjectsCcDurableObjectsConfigurationNamespaceID",
    "CcContainersCreateScheduledApplicationRequestDurableObjectsCcDurableObjectsConfigurationScriptAndClass",
    "CcContainersCreateScheduledApplicationRequestObservability",
    "CcContainersCreateScheduledApplicationRequestObservabilityLogs",
    "CcContainersCreateDurableObjectApplicationRequest",
    "CcContainersCreateDurableObjectApplicationRequestDurableObjects",
    "CcContainersCreateDurableObjectApplicationRequestDurableObjectsCcDurableObjectsConfigurationNamespaceID",
    "CcContainersCreateDurableObjectApplicationRequestDurableObjectsCcDurableObjectsConfigurationScriptAndClass",
    "CcContainersCreateDurableObjectApplicationRequestConfiguration",
    "CcContainersCreateDurableObjectApplicationRequestConfigurationAuthorizedKey",
    "CcContainersCreateDurableObjectApplicationRequestConfigurationWranglerSSH",
    "CcContainersCreateDurableObjectApplicationRequestObservability",
    "CcContainersCreateDurableObjectApplicationRequestObservabilityLogs",
]


class CcContainersCreateScheduledApplicationRequest(TypedDict, total=False):
    account_id: Required[str]

    configuration: Required[CcContainersCreateScheduledApplicationRequestConfiguration]
    """Defines the deployment configuration for every deployment in this application."""

    instances: Required[int]
    """The initial number of deployments to create."""

    max_instances: Required[int]
    """Sets the maximum number of instances that the application can run."""

    name: Required[str]
    """The name for this application."""

    scheduling_policy: Required[Literal["default"]]
    """Selects a scheduler-backed application.

    Use `default` when the Containers scheduler should maintain the requested number
    of instances and manage deployment configuration, placement, scaling, versions,
    and rollouts.
    """

    constraints: CcContainersCreateScheduledApplicationRequestConstraints

    durable_objects: CcContainersCreateScheduledApplicationRequestDurableObjects
    """
    Optionally associates this scheduler-backed application with a Durable Object
    namespace.
    """

    observability: CcContainersCreateScheduledApplicationRequestObservability
    """
    Top-level observability settings for the application. This field is mutually
    exclusive with configuration.observability.
    """

    rollout_active_grace_period: int
    """
    Grace period for active instances to stay alive before becoming eligible for
    shutdown signal due to a rollout, in seconds. Defaults to 0.
    """


class CcContainersCreateScheduledApplicationRequestConfigurationAuthorizedKey(TypedDict, total=False):
    """User-provided SSH public key."""

    public_key: Required[str]
    """An SSH public key."""

    name: str
    """Optional human readable name for this key."""


class CcContainersCreateScheduledApplicationRequestConfigurationEnvironmentVariable(TypedDict, total=False):
    """An environment variable with a value set."""

    name: Required[str]
    """An environment variable name."""

    value: Required[str]
    """An environment variable value."""


class CcContainersCreateScheduledApplicationRequestConfigurationObservabilityLogs(TypedDict, total=False):
    """Observability logging settings."""

    enabled: bool


class CcContainersCreateScheduledApplicationRequestConfigurationObservability(TypedDict, total=False):
    """Settings for deployment observability such as logging."""

    logs: CcContainersCreateScheduledApplicationRequestConfigurationObservabilityLogs
    """Observability logging settings."""


class CcContainersCreateScheduledApplicationRequestConfiguration(TypedDict, total=False):
    """Defines the deployment configuration for every deployment in this application."""

    image: Required[str]
    """Image url."""

    authorized_keys: Iterable[CcContainersCreateScheduledApplicationRequestConfigurationAuthorizedKey]

    command: SequenceNotStr[str]
    """
    The command that runs when the container starts, passed to the entrypoint. You
    can override this at run-time. If you override only the command, it gets passed
    to the default entrypoint specified in the image.
    """

    entrypoint: SequenceNotStr[str]
    """
    The entry point for the container, specifying the executable to run when the
    container starts. You can override this at run-time. If you do, the default
    command from the image is ignored. Specify both entrypoint and command at
    run-time to completely replace the image defaults.
    """

    environment_variables: Iterable[CcContainersCreateScheduledApplicationRequestConfigurationEnvironmentVariable]
    """Container environment variables."""

    instance_type: Literal["lite", "basic", "standard-1", "standard-2", "standard-3", "standard-4"]
    """The instance type configures vCPU, memory, and disk.

    - "lite": 1/16 vCPU, 256 MiB memory, 2 GB disk
    - "basic": 1/4 vCPU, 1 GiB memory, 4 GB disk
    - "standard-1": 1/2 vCPU, 4 GiB memory, 8 GB disk
    - "standard-2": 1 vCPU, 6 GiB memory, 12 GB disk
    - "standard-3": 2 vCPU, 8 GiB memory, 16 GB disk
    - "standard-4": 4 vCPU, 12 GiB memory, 20 GB disk
    """

    observability: CcContainersCreateScheduledApplicationRequestConfigurationObservability
    """Settings for deployment observability such as logging."""


class CcContainersCreateScheduledApplicationRequestConstraints(TypedDict, total=False):
    jurisdiction: str
    """Restricts placement to datacenters in the selected jurisdiction.

    Choose "eu", "fedramp", or "us". When combined with regions, EU supports EEUR
    and WEUR while FedRAMP and US support ENAM and WNAM.
    """

    regions: SequenceNotStr[str]


class CcContainersCreateScheduledApplicationRequestDurableObjectsCcDurableObjectsConfigurationNamespaceID(
    TypedDict, total=False
):
    """Durable object configuration using a namespace ID."""

    namespace_id: Required[str]
    """The namespace ID of the durable object namespace to use for this application."""


class CcContainersCreateScheduledApplicationRequestDurableObjectsCcDurableObjectsConfigurationScriptAndClass(
    TypedDict, total=False
):
    """Durable object configuration using script and class names."""

    class_name: Required[str]
    """The class name of the durable object."""

    script_name: Required[str]
    """The script name where the durable object class is defined."""


CcContainersCreateScheduledApplicationRequestDurableObjects: TypeAlias = Union[
    CcContainersCreateScheduledApplicationRequestDurableObjectsCcDurableObjectsConfigurationNamespaceID,
    CcContainersCreateScheduledApplicationRequestDurableObjectsCcDurableObjectsConfigurationScriptAndClass,
]


class CcContainersCreateScheduledApplicationRequestObservabilityLogs(TypedDict, total=False):
    """Observability logging settings."""

    enabled: bool


class CcContainersCreateScheduledApplicationRequestObservability(TypedDict, total=False):
    """
    Top-level observability settings for the application.
    This field is mutually exclusive with configuration.observability.
    """

    logs: CcContainersCreateScheduledApplicationRequestObservabilityLogs
    """Observability logging settings."""


class CcContainersCreateDurableObjectApplicationRequest(TypedDict, total=False):
    account_id: Required[str]

    durable_objects: Required[CcContainersCreateDurableObjectApplicationRequestDurableObjects]
    """
    The customer-owned Durable Object namespace that owns this application and its
    instances.
    """

    name: Required[str]
    """The name for this application."""

    scheduling_policy: Required[Literal["durable_object"]]
    """Selects a Durable Object-managed application.

    Each Durable Object creates and manages the lifecycle of its container instance.
    Configure application-wide observability settings here. Deployment
    configuration, scaling, placement constraints, versions, and rollouts do not
    apply.
    """

    configuration: CcContainersCreateDurableObjectApplicationRequestConfiguration
    """Configuration for a Durable Object-managed application."""

    observability: CcContainersCreateDurableObjectApplicationRequestObservability
    """
    Application-wide logging settings for a Durable Object-managed application. The
    application publishes these settings to its runtime metadata. Updating them does
    not create a deployment or rollout.
    """


class CcContainersCreateDurableObjectApplicationRequestDurableObjectsCcDurableObjectsConfigurationNamespaceID(
    TypedDict, total=False
):
    """Durable object configuration using a namespace ID."""

    namespace_id: Required[str]
    """The namespace ID of the durable object namespace to use for this application."""


class CcContainersCreateDurableObjectApplicationRequestDurableObjectsCcDurableObjectsConfigurationScriptAndClass(
    TypedDict, total=False
):
    """Durable object configuration using script and class names."""

    class_name: Required[str]
    """The class name of the durable object."""

    script_name: Required[str]
    """The script name where the durable object class is defined."""


CcContainersCreateDurableObjectApplicationRequestDurableObjects: TypeAlias = Union[
    CcContainersCreateDurableObjectApplicationRequestDurableObjectsCcDurableObjectsConfigurationNamespaceID,
    CcContainersCreateDurableObjectApplicationRequestDurableObjectsCcDurableObjectsConfigurationScriptAndClass,
]


class CcContainersCreateDurableObjectApplicationRequestConfigurationAuthorizedKey(TypedDict, total=False):
    """User-provided SSH public key."""

    public_key: Required[str]
    """An SSH public key."""

    name: str
    """Optional human readable name for this key."""


class CcContainersCreateDurableObjectApplicationRequestConfigurationWranglerSSH(TypedDict, total=False):
    """Configuration properties for connecting with SSH to a container using Wrangler."""

    enabled: bool

    port: int


class CcContainersCreateDurableObjectApplicationRequestConfiguration(TypedDict, total=False):
    """Configuration for a Durable Object-managed application."""

    authorized_keys: Iterable[CcContainersCreateDurableObjectApplicationRequestConfigurationAuthorizedKey]

    wrangler_ssh: CcContainersCreateDurableObjectApplicationRequestConfigurationWranglerSSH
    """Configuration properties for connecting with SSH to a container using Wrangler."""


class CcContainersCreateDurableObjectApplicationRequestObservabilityLogs(TypedDict, total=False):
    """Application-wide logging settings."""

    enabled: bool


class CcContainersCreateDurableObjectApplicationRequestObservability(TypedDict, total=False):
    """
    Application-wide logging settings for a Durable Object-managed application.
    The application publishes these settings to its runtime metadata. Updating
    them does not create a deployment or rollout.
    """

    logs: CcContainersCreateDurableObjectApplicationRequestObservabilityLogs
    """Application-wide logging settings."""


ApplicationCreateParams: TypeAlias = Union[
    CcContainersCreateScheduledApplicationRequest, CcContainersCreateDurableObjectApplicationRequest
]
