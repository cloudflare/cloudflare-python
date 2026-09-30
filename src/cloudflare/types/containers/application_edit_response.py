# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ApplicationEditResponse",
    "CcScheduledApplication",
    "CcScheduledApplicationConfiguration",
    "CcScheduledApplicationConfigurationAuthorizedKey",
    "CcScheduledApplicationConfigurationEnvironmentVariable",
    "CcScheduledApplicationConfigurationObservability",
    "CcScheduledApplicationConfigurationObservabilityLogs",
    "CcScheduledApplicationConstraints",
    "CcScheduledApplicationDurableObjects",
    "CcScheduledApplicationHealth",
    "CcScheduledApplicationHealthError",
    "CcScheduledApplicationHealthErrorEvent",
    "CcScheduledApplicationHealthInstances",
    "CcScheduledApplicationObservability",
    "CcScheduledApplicationObservabilityLogs",
    "CcDurableObjectApplication",
    "CcDurableObjectApplicationDurableObjects",
    "CcDurableObjectApplicationConfiguration",
    "CcDurableObjectApplicationConfigurationAuthorizedKey",
    "CcDurableObjectApplicationConfigurationWranglerSSH",
    "CcDurableObjectApplicationHealth",
    "CcDurableObjectApplicationHealthInstances",
    "CcDurableObjectApplicationObservability",
    "CcDurableObjectApplicationObservabilityLogs",
]


class CcScheduledApplicationConfigurationAuthorizedKey(BaseModel):
    """User-provided SSH public key."""

    public_key: str
    """An SSH public key."""

    name: Optional[str] = None
    """Optional human readable name for this key."""


class CcScheduledApplicationConfigurationEnvironmentVariable(BaseModel):
    """An environment variable with a value set."""

    name: str
    """An environment variable name."""

    value: str
    """An environment variable value."""


class CcScheduledApplicationConfigurationObservabilityLogs(BaseModel):
    """Observability logging settings."""

    enabled: Optional[bool] = None


class CcScheduledApplicationConfigurationObservability(BaseModel):
    """Settings for deployment observability such as logging."""

    logs: Optional[CcScheduledApplicationConfigurationObservabilityLogs] = None
    """Observability logging settings."""


class CcScheduledApplicationConfiguration(BaseModel):
    """User-specified container configuration."""

    image: str
    """Image url."""

    authorized_keys: Optional[List[CcScheduledApplicationConfigurationAuthorizedKey]] = None

    command: Optional[List[str]] = None
    """
    The command that runs when the container starts, passed to the entrypoint. You
    can override this at run-time. If you override only the command, it gets passed
    to the default entrypoint specified in the image.
    """

    entrypoint: Optional[List[str]] = None
    """
    The entry point for the container, specifying the executable to run when the
    container starts. You can override this at run-time. If you do, the default
    command from the image is ignored. Specify both entrypoint and command at
    run-time to completely replace the image defaults.
    """

    environment_variables: Optional[List[CcScheduledApplicationConfigurationEnvironmentVariable]] = None
    """Container environment variables."""

    instance_type: Optional[Literal["lite", "basic", "standard-1", "standard-2", "standard-3", "standard-4"]] = None
    """The instance type configures vCPU, memory, and disk.

    - "lite": 1/16 vCPU, 256 MiB memory, 2 GB disk
    - "basic": 1/4 vCPU, 1 GiB memory, 4 GB disk
    - "standard-1": 1/2 vCPU, 4 GiB memory, 8 GB disk
    - "standard-2": 1 vCPU, 6 GiB memory, 12 GB disk
    - "standard-3": 2 vCPU, 8 GiB memory, 16 GB disk
    - "standard-4": 4 vCPU, 12 GiB memory, 20 GB disk
    """

    observability: Optional[CcScheduledApplicationConfigurationObservability] = None
    """Settings for deployment observability such as logging."""


class CcScheduledApplicationConstraints(BaseModel):
    jurisdiction: Optional[str] = None
    """Restricts placement to datacenters in the selected jurisdiction.

    Choose "eu", "fedramp", or "us". When combined with regions, EU supports EEUR
    and WEUR while FedRAMP and US support ENAM and WNAM.
    """

    regions: Optional[List[str]] = None


class CcScheduledApplicationDurableObjects(BaseModel):
    """
    Durable object configuration stored on and returned from a Cloudchamber application.
    """

    namespace_id: str
    """The namespace ID of the durable object namespace to use for this application."""


class CcScheduledApplicationHealthErrorEvent(BaseModel):
    """An event within a Placement or a Job."""

    id: str

    details: Dict[str, object]

    message: str

    name: Literal[
        "SchedulerPlaced",
        "NetworkingIPAssigned",
        "VMStarted",
        "ImagePulled",
        "ImagePullError",
        "VMFailedToStart",
        "NetworkingIPAssignmentFailed",
        "VMRunning",
        "VMStopping",
        "VMStopped",
        "VMFailed",
        "RuntimeStartFailed",
        "SSHStarted",
        "ServiceHealthUpdates",
        "CheckUpdate",
        "DurableObjectConnected",
        "ContainerStarted",
    ]
    """Name of the event that describes the kind event that happened.

    - SchedulerPlaced: It's the first event that creates a container placement. It
      happens when the Containers runtime was able to retrieve deployment resources
      and start verifying everything is correct.
    - NetworkingIPAssigned: It's sent when the Containers runtime maps the IP to the
      container.
    - VMStarted: It's sent when the Containers runtime starts the VM. The container
      might remain unhealthy at this point.
    - ImagePulled: It's sent when the Containers runtime pulls the image
      successfully.
    - ImagePullError: It's sent when the Containers runtime is having issues pulling
      the image. The message and details have more information on what happened for
      debugging.
    - VMFailedToStart: It's sent when the Containers runtime was unable to boot the
      VM.
    - VMStopping: It's sent when the scheduler is stopping the VM.
    - VMStopped: It's sent when the VM finally exits.
    - VMFailed: It's sent when the scheduling of the VM failed in the current
      location.
    - RuntimeStartFailed: It's sent when the runtime hits an internal error.
    - SSHStarted: It's sent when the container gains network connectivity and opens
      the SSH port. Containers only send this event when SSH keys exist.
    - CheckUpdate: Sent when the status of a health or readiness check changes. This
      may also affect the health status of the placement.
    - DurableObjectConnected: Sent when a durable object instance connects and gains
      control of the deployment. This event is only sent for durable object
      deployments. It is sent after VMStarted.
    - ContainerStarted: It's sent when the container starts running.
    """

    status_change: Dict[str, object] = FieldInfo(alias="statusChange")

    time: str
    """UTC timestamp string in ISO 8601 format."""

    type: Literal["Info", "Error", "Warn", "UserError", "SystemError"]


class CcScheduledApplicationHealthError(BaseModel):
    event: CcScheduledApplicationHealthErrorEvent
    """An event within a Placement or a Job."""

    instance_id: str
    """
    An instance ID represents an identifier of an instance configuration that
    maintains an underlying placement.
    """


class CcScheduledApplicationHealthInstances(BaseModel):
    """Shows a count of application instance states."""

    active: int
    """
    Number of instances whose runtime reports the container as running
    (container_status = "running"). This is a subset of the placements that remain
    up: an instance that is already bound to a Durable Object and serving traffic is
    counted under "assigned" until its container_status catches up to "running", so
    container_status can briefly lag Durable Object attachment under churn. To
    estimate running, Durable-Object-bound instances, sum "active" + "assigned"
    rather than reading "active" alone.
    """

    assigned: int
    """
    Number of instances bound to a Durable Object with a running placement whose
    container_status remains behind "running". These count as live, serving
    instances; "active" + "assigned" approximates the running, Durable-Object-bound
    count.
    """


class CcScheduledApplicationHealth(BaseModel):
    errors: List[CcScheduledApplicationHealthError]

    instances: CcScheduledApplicationHealthInstances
    """Shows a count of application instance states."""

    summary: Optional[Literal["healthy", "degraded", "unhealthy", "pending"]] = None
    """High-level health assessment.

    Only populated for "new_instances" strategy. Based on a sample of target-version
    instances rather than a full count.

    - "pending": Zero target-version instances exist yet.
    - "healthy": Every sampled target-version instance reports running or active.
    - "degraded": Some sampled instances remain starting or scheduling.
    - "unhealthy": One or more sampled instances have failed.
    """


class CcScheduledApplicationObservabilityLogs(BaseModel):
    """Observability logging settings."""

    enabled: Optional[bool] = None


class CcScheduledApplicationObservability(BaseModel):
    """
    Top-level observability settings for the application.
    This field is mutually exclusive with configuration.observability.
    """

    logs: Optional[CcScheduledApplicationObservabilityLogs] = None
    """Observability logging settings."""


class CcScheduledApplication(BaseModel):
    """
    Describes an application and the parameters that govern how it places its instances.
    """

    id: str
    """An Application ID represents an identifier of an application."""

    account_id: str
    """A unique identifier for the user's account."""

    configuration: CcScheduledApplicationConfiguration
    """User-specified container configuration."""

    created_at: str
    """UTC timestamp string in ISO 8601 format."""

    instances: int
    """Number of deployments to create."""

    name: str
    """The application name."""

    scheduling_policy: Literal["default", "durable_object"]
    """The scheduling policy to use for an application."""

    updated_at: str
    """UTC timestamp string in ISO 8601 format."""

    version: int

    active_rollout_id: Optional[str] = None
    """An identifier for a specific rollout within an application."""

    constraints: Optional[CcScheduledApplicationConstraints] = None

    durable_objects: Optional[CcScheduledApplicationDurableObjects] = None
    """
    Durable object configuration stored on and returned from a Cloudchamber
    application.
    """

    health: Optional[CcScheduledApplicationHealth] = None

    max_instances: Optional[int] = None
    """Maximum number of instances the application allows.

    This is relevant for applications that auto-scale.
    """

    observability: Optional[CcScheduledApplicationObservability] = None
    """
    Top-level observability settings for the application. This field is mutually
    exclusive with configuration.observability.
    """

    rollout_active_grace_period: Optional[int] = None
    """
    Grace period for active instances to stay alive before becoming eligible for
    shutdown signal due to a rollout, in seconds. Defaults to 0.
    """


class CcDurableObjectApplicationDurableObjects(BaseModel):
    """Durable object configuration using a namespace ID."""

    namespace_id: str
    """The namespace ID of the durable object namespace to use for this application."""


class CcDurableObjectApplicationConfigurationAuthorizedKey(BaseModel):
    """User-provided SSH public key."""

    public_key: str
    """An SSH public key."""

    name: Optional[str] = None
    """Optional human readable name for this key."""


class CcDurableObjectApplicationConfigurationWranglerSSH(BaseModel):
    """Configuration properties for connecting with SSH to a container using Wrangler."""

    enabled: Optional[bool] = None

    port: Optional[int] = None


class CcDurableObjectApplicationConfiguration(BaseModel):
    """Application-wide settings for a Durable Object-managed application."""

    authorized_keys: Optional[List[CcDurableObjectApplicationConfigurationAuthorizedKey]] = None

    wrangler_ssh: Optional[CcDurableObjectApplicationConfigurationWranglerSSH] = None
    """Configuration properties for connecting with SSH to a container using Wrangler."""


class CcDurableObjectApplicationHealthInstances(BaseModel):
    """Counts of observed non-terminal instances."""

    active: int
    """Number of instances whose runtime reports running or stopping."""

    starting: int
    """Number of instances whose runtime reports starting."""


class CcDurableObjectApplicationHealth(BaseModel):
    """
    Aggregate current activity for the latest observed placement of each instance.
    Runtime snapshots feed periodic background sweeps. Counts refresh after each
    complete sweep. Instance listings retain their separate three-month history
    for failure discovery.
    """

    instances: CcDurableObjectApplicationHealthInstances
    """Counts of observed non-terminal instances."""

    summary: Optional[Literal["pending"]] = None
    """Present as pending until the first activity sweep completes; omitted afterward."""


class CcDurableObjectApplicationObservabilityLogs(BaseModel):
    """Application-wide logging settings."""

    enabled: Optional[bool] = None


class CcDurableObjectApplicationObservability(BaseModel):
    """
    Application-wide logging settings for a Durable Object-managed application.
    The application publishes these settings to its runtime metadata. Updating
    them does not create a deployment or rollout.
    """

    logs: Optional[CcDurableObjectApplicationObservabilityLogs] = None
    """Application-wide logging settings."""


class CcDurableObjectApplication(BaseModel):
    """
    Each Durable Object creates and manages the lifecycle of its container instance.
    """

    id: str
    """An Application ID represents an identifier of an application."""

    account_id: str
    """A unique identifier for the user's account."""

    created_at: str
    """UTC timestamp string in ISO 8601 format."""

    durable_objects: CcDurableObjectApplicationDurableObjects
    """Durable object configuration using a namespace ID."""

    name: str
    """The application name."""

    scheduling_policy: Literal["durable_object"]
    """Selects a Durable Object-managed application.

    Each Durable Object creates and manages the lifecycle of its container instance.
    Configure application-wide observability settings here. Deployment
    configuration, scaling, placement constraints, versions, and rollouts do not
    apply.
    """

    updated_at: str
    """UTC timestamp string in ISO 8601 format."""

    configuration: Optional[CcDurableObjectApplicationConfiguration] = None
    """Application-wide settings for a Durable Object-managed application."""

    health: Optional[CcDurableObjectApplicationHealth] = None
    """
    Aggregate current activity for the latest observed placement of each instance.
    Runtime snapshots feed periodic background sweeps. Counts refresh after each
    complete sweep. Instance listings retain their separate three-month history for
    failure discovery.
    """

    observability: Optional[CcDurableObjectApplicationObservability] = None
    """
    Application-wide logging settings for a Durable Object-managed application. The
    application publishes these settings to its runtime metadata. Updating them does
    not create a deployment or rollout.
    """


ApplicationEditResponse: TypeAlias = Union[CcScheduledApplication, CcDurableObjectApplication]
