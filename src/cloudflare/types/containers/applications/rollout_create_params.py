# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "RolloutCreateParams",
    "TargetConfiguration",
    "TargetConfigurationAuthorizedKey",
    "TargetConfigurationEnvironmentVariable",
    "TargetConfigurationObservability",
    "TargetConfigurationObservabilityLogs",
    "Step",
    "StepStepSize",
]


class RolloutCreateParams(TypedDict, total=False):
    account_id: Required[str]

    description: Required[str]
    """Description of the rollout process."""

    strategy: Required[Literal["rolling", "new_instances"]]
    """Strategy used for the rollout.

    - "rolling": Step-based rollout with health gates. Actively replaces instances
      to reach each step's target percentage.
    - "new_instances": Percentage control over version distribution. Version sync
      actively replaces instances to match the configured percentage. The
      "full_auto" kind advances through fixed percentage targets after
      target-version health is observed.
    """

    target_configuration: Required[TargetConfiguration]
    """User-specified container configuration changes."""

    kind: Literal["full_auto", "full_manual"]
    """Kind of the rollout process. Defaults to "full_auto".

    - "full_auto": For rolling rollouts, starts progressing steps upon rollout
      creation. For new_instances rollouts, advances percentage targets
      automatically after target-version health is observed.
    - "full_manual": Requires manually progressing each step in the rollout using
      the UpdateRollout's action parameter.
    """

    percentage: int
    """Initial target version percentage (0-100).

    Version sync actively replaces instances to match. Required when strategy is
    "new_instances" and kind is "full_manual". When strategy is "new_instances" and
    kind is "full_auto", omitted percentage starts at 10% or the smallest percentage
    that targets at least one instance. Unused for "rolling".
    """

    step_percentage: Literal[5, 10, 20, 25, 50, 100]
    """Percentage of rollout to increase in each step when "steps" is absent.

    Applicable values: 5, 10, 20, 25, 50, 100. These create rollouts with 20, 10, 5,
    4, 2, 1 steps respectively. Only valid for "rolling" strategy.
    """

    steps: Iterable[Step]
    """
    Steps defining the rollout process, used when "step_percentage" is absent.
    Specify only one of "step_percentage" or "steps" when creating a rollout.
    "steps" allow granular control over each step. Only valid for "rolling"
    strategy.
    """


class TargetConfigurationAuthorizedKey(TypedDict, total=False):
    """User-provided SSH public key."""

    public_key: Required[str]
    """An SSH public key."""

    name: str
    """Optional human readable name for this key."""


class TargetConfigurationEnvironmentVariable(TypedDict, total=False):
    """An environment variable with a value set."""

    name: Required[str]
    """An environment variable name."""

    value: Required[str]
    """An environment variable value."""


class TargetConfigurationObservabilityLogs(TypedDict, total=False):
    """Observability logging settings."""

    enabled: bool


class TargetConfigurationObservability(TypedDict, total=False):
    """Settings for deployment observability such as logging."""

    logs: TargetConfigurationObservabilityLogs
    """Observability logging settings."""


class TargetConfiguration(TypedDict, total=False):
    """User-specified container configuration changes."""

    authorized_keys: Iterable[TargetConfigurationAuthorizedKey]

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

    environment_variables: Iterable[TargetConfigurationEnvironmentVariable]
    """Container environment variables."""

    image: str
    """Image url."""

    instance_type: Literal["lite", "basic", "standard-1", "standard-2", "standard-3", "standard-4"]
    """The instance type configures vCPU, memory, and disk.

    - "lite": 1/16 vCPU, 256 MiB memory, 2 GB disk
    - "basic": 1/4 vCPU, 1 GiB memory, 4 GB disk
    - "standard-1": 1/2 vCPU, 4 GiB memory, 8 GB disk
    - "standard-2": 1 vCPU, 6 GiB memory, 12 GB disk
    - "standard-3": 2 vCPU, 8 GiB memory, 16 GB disk
    - "standard-4": 4 vCPU, 12 GiB memory, 20 GB disk
    """

    observability: TargetConfigurationObservability
    """Settings for deployment observability such as logging."""


class StepStepSize(TypedDict, total=False):
    percentage: Required[int]
    """Percentage of instances affected in this step. Min 10% and Max 100%."""


class Step(TypedDict, total=False):
    """Steps defining the rollout process."""

    description: Required[str]
    """Description of the rollout step."""

    step_size: Required[StepStepSize]
