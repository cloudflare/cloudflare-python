# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .....workers.binding_param import BindingParam
from .....workers.migration_step_param import MigrationStepParam
from .....workers.single_step_migration_param import SingleStepMigrationParam
from .....workers.placement_configuration_param import PlacementConfigurationParam
from .....workers.scripts.consumer_script_param import ConsumerScriptParam

__all__ = [
    "SettingEditParams",
    "Settings",
    "SettingsLimits",
    "SettingsMigrations",
    "SettingsMigrationsWorkersMultipleStepMigrations",
    "SettingsObservability",
]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    settings: Settings


class SettingsLimits(TypedDict, total=False):
    cpu_ms: int
    """The amount of CPU time this Worker can use in milliseconds."""


class SettingsMigrationsWorkersMultipleStepMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[MigrationStepParam]
    """Migrations to apply in order."""


SettingsMigrations: TypeAlias = Union[SingleStepMigrationParam, SettingsMigrationsWorkersMultipleStepMigrations]


class SettingsObservability(TypedDict, total=False):
    enabled: Required[bool]
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float]
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """


class Settings(TypedDict, total=False):
    bindings: Iterable[BindingParam]
    """List of bindings attached to this Worker"""

    compatibility_date: str
    """Date indicating targeted support in the Workers runtime.

    Backwards incompatible fixes to the runtime following this date will not affect
    this Worker.
    """

    compatibility_flags: List[str]
    """Flags that enable or disable certain features in the Workers runtime.

    Used to enable upcoming features or opt in or out of specific changes not
    included in a `compatibility_date`.
    """

    limits: SettingsLimits
    """Limits to apply for this Worker."""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    migrations: SettingsMigrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    observability: SettingsObservability
    """Observability settings for the Worker."""

    placement: PlacementConfigurationParam

    tags: List[str]
    """Tags to help you manage your Workers"""

    tail_consumers: Iterable[ConsumerScriptParam]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Literal["bundled", "unbound"]
    """Usage model for the Worker invocations."""
