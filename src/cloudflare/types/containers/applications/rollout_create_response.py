# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "RolloutCreateResponse",
    "CurrentConfiguration",
    "CurrentConfigurationAuthorizedKey",
    "CurrentConfigurationEnvironmentVariable",
    "CurrentConfigurationObservability",
    "CurrentConfigurationObservabilityLogs",
    "Health",
    "HealthError",
    "HealthErrorEvent",
    "HealthInstances",
    "TargetConfiguration",
    "TargetConfigurationAuthorizedKey",
    "TargetConfigurationEnvironmentVariable",
    "TargetConfigurationObservability",
    "TargetConfigurationObservabilityLogs",
    "Progress",
    "ProgressVersionDistribution",
    "Step",
    "StepStepSize",
    "VersionDistribution",
]


class CurrentConfigurationAuthorizedKey(BaseModel):
    """User-provided SSH public key."""

    public_key: str
    """An SSH public key."""

    name: Optional[str] = None
    """Optional human readable name for this key."""


class CurrentConfigurationEnvironmentVariable(BaseModel):
    """An environment variable with a value set."""

    name: str
    """An environment variable name."""

    value: str
    """An environment variable value."""


class CurrentConfigurationObservabilityLogs(BaseModel):
    """Observability logging settings."""

    enabled: Optional[bool] = None


class CurrentConfigurationObservability(BaseModel):
    """Settings for deployment observability such as logging."""

    logs: Optional[CurrentConfigurationObservabilityLogs] = None
    """Observability logging settings."""


class CurrentConfiguration(BaseModel):
    """User-specified container configuration changes."""

    authorized_keys: Optional[List[CurrentConfigurationAuthorizedKey]] = None

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

    environment_variables: Optional[List[CurrentConfigurationEnvironmentVariable]] = None
    """Container environment variables."""

    image: Optional[str] = None
    """Image url."""

    instance_type: Optional[Literal["lite", "basic", "standard-1", "standard-2", "standard-3", "standard-4"]] = None
    """The instance type configures vCPU, memory, and disk.

    - "lite": 1/16 vCPU, 256 MiB memory, 2 GB disk
    - "basic": 1/4 vCPU, 1 GiB memory, 4 GB disk
    - "standard-1": 1/2 vCPU, 4 GiB memory, 8 GB disk
    - "standard-2": 1 vCPU, 6 GiB memory, 12 GB disk
    - "standard-3": 2 vCPU, 8 GiB memory, 16 GB disk
    - "standard-4": 4 vCPU, 12 GiB memory, 20 GB disk
    """

    observability: Optional[CurrentConfigurationObservability] = None
    """Settings for deployment observability such as logging."""


class HealthErrorEvent(BaseModel):
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


class HealthError(BaseModel):
    event: HealthErrorEvent
    """An event within a Placement or a Job."""

    instance_id: str
    """
    An instance ID represents an identifier of an instance configuration that
    maintains an underlying placement.
    """


class HealthInstances(BaseModel):
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


class Health(BaseModel):
    errors: List[HealthError]

    instances: HealthInstances
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


class TargetConfigurationAuthorizedKey(BaseModel):
    """User-provided SSH public key."""

    public_key: str
    """An SSH public key."""

    name: Optional[str] = None
    """Optional human readable name for this key."""


class TargetConfigurationEnvironmentVariable(BaseModel):
    """An environment variable with a value set."""

    name: str
    """An environment variable name."""

    value: str
    """An environment variable value."""


class TargetConfigurationObservabilityLogs(BaseModel):
    """Observability logging settings."""

    enabled: Optional[bool] = None


class TargetConfigurationObservability(BaseModel):
    """Settings for deployment observability such as logging."""

    logs: Optional[TargetConfigurationObservabilityLogs] = None
    """Observability logging settings."""


class TargetConfiguration(BaseModel):
    """User-specified container configuration changes."""

    authorized_keys: Optional[List[TargetConfigurationAuthorizedKey]] = None

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

    environment_variables: Optional[List[TargetConfigurationEnvironmentVariable]] = None
    """Container environment variables."""

    image: Optional[str] = None
    """Image url."""

    instance_type: Optional[Literal["lite", "basic", "standard-1", "standard-2", "standard-3", "standard-4"]] = None
    """The instance type configures vCPU, memory, and disk.

    - "lite": 1/16 vCPU, 256 MiB memory, 2 GB disk
    - "basic": 1/4 vCPU, 1 GiB memory, 4 GB disk
    - "standard-1": 1/2 vCPU, 4 GiB memory, 8 GB disk
    - "standard-2": 1 vCPU, 6 GiB memory, 12 GB disk
    - "standard-3": 2 vCPU, 8 GiB memory, 16 GB disk
    - "standard-4": 4 vCPU, 12 GiB memory, 20 GB disk
    """

    observability: Optional[TargetConfigurationObservability] = None
    """Settings for deployment observability such as logging."""


class ProgressVersionDistribution(BaseModel):
    """
    Expected distribution of instances per version, based on the current percentage split.
    Populated during active rollouts. Values derive from the version percentage weights
    rather than actual running instance counts.
    """

    current_version_instances: Optional[int] = None
    """
    Expected number of instances remaining on the current (old) version based on the
    current percentage split. Only populated for "rolling" strategy.
    """

    current_version_percentage: Optional[int] = None
    """
    The percentage of new instances being scheduled on the current version (100 -
    target_version_percentage). Only populated for "new_instances" strategy.
    """

    target_version_instances: Optional[int] = None
    """
    Expected number of instances scheduled for the target (new) version based on the
    current percentage split. Only populated for "rolling" strategy.
    """

    target_version_percentage: Optional[int] = None
    """
    The active percentage of new instances being scheduled on the target version.
    For "rolling", this reflects the step_size.percentage of the current active
    step. For "new_instances", this reflects the user-set percentage.
    """


class Progress(BaseModel):
    """Progress details of an application rollout."""

    current_step: int
    """Current step being executed in the rollout process. Initialized to 0."""

    total_instances: int
    """Total number of instances the rollout affects."""

    total_steps: int
    """Total number of steps in the rollout."""

    updated_instances: int
    """Number of instances updated in the rollout process."""

    version_distribution: Optional[ProgressVersionDistribution] = None
    """
    Expected distribution of instances per version, based on the current percentage
    split. Populated during active rollouts. Values derive from the version
    percentage weights rather than actual running instance counts.
    """


class StepStepSize(BaseModel):
    percentage: int
    """Percentage of instances affected in this step. Min 10% and Max 100%."""


class Step(BaseModel):
    """Steps within the rollout process."""

    id: int
    """
    The sequential order of the rollout step, automatically assigned starting from
    1, based on the total number of steps in the rollout process.
    """

    description: str
    """Description of the rollout step."""

    status: Literal["pending", "progressing", "reverting", "completed", "reverted"]
    """Status of the rollout step."""

    step_size: StepStepSize

    completed_at: Optional[str] = None
    """UTC timestamp string in ISO 8601 format."""

    reason: Optional[str] = None
    """Reason for the step's current status."""

    started_at: Optional[str] = None
    """UTC timestamp string in ISO 8601 format."""


class VersionDistribution(BaseModel):
    """Version percentage distribution.

    Only present for "new_instances" strategy.
    For "rolling" strategy, see progress.version_distribution instead.
    """

    current_version_percentage: int
    """Percentage of instances on the current (old) version."""

    target_version_percentage: int
    """Percentage of instances on the target (new) version."""


class RolloutCreateResponse(BaseModel):
    """
    Represents the status and metadata of a rollout process for an application.
    For "rolling" strategy: includes steps and progress with instance counts.
    For "new_instances" strategy: the response omits steps and progress. Use percentage,
    version_distribution, and health.summary for status.
    """

    id: str
    """An identifier for a specific rollout within an application."""

    created_at: str
    """UTC timestamp string in ISO 8601 format."""

    current_configuration: CurrentConfiguration
    """User-specified container configuration changes."""

    current_version: int
    """Current application version before the rollout."""

    description: str

    health: Health

    kind: Literal["full_auto", "full_manual", "durable_objects_auto"]
    """Kind of the rollout process.

    - "full_auto": For rolling rollouts, starts progressing steps upon rollout
      creation. For new_instances rollouts, advances percentage targets
      automatically after target-version health is observed.
    - "full_manual": Requires manually progressing each step in the rollout using
      the UpdateRollout's action paramater.
    - "durable_objects_auto": Default when the application is a DO application.
    """

    last_updated_at: str
    """Timestamp of the most recent update to status, health, or progress."""

    status: Literal["pending", "progressing", "completed", "reverted", "replaced"]
    """Current status of the rollout."""

    strategy: Literal["rolling", "new_instances"]
    """The rollout strategy.

    - "rolling": Step-based rollout with health gates. Actively replaces instances
      to reach each step's target percentage. Response includes steps and progress.
    - "new_instances": Percentage control over version distribution. Version sync
      actively replaces instances to match the configured percentage. "full_auto"
      ramps through fixed percentage targets after target-version health is
      observed. Response includes percentage, version_distribution, and
      health.summary.
    """

    target_configuration: TargetConfiguration
    """User-specified container configuration changes."""

    target_version: int
    """
    Target application version after the rollout is complete and applied to all
    current instances.
    """

    percentage: Optional[int] = None
    """Current target version percentage (0-100).

    Only present for "new_instances" strategy.
    """

    progress: Optional[Progress] = None
    """Progress details of an application rollout."""

    started_at: Optional[datetime] = None
    """Timestamp when the rollout started."""

    steps: Optional[List[Step]] = None

    version_distribution: Optional[VersionDistribution] = None
    """Version percentage distribution.

    Only present for "new_instances" strategy. For "rolling" strategy, see
    progress.version_distribution instead.
    """
