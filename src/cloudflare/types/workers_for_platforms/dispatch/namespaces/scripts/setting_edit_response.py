# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ......_models import BaseModel
from .....workers.binding import Binding
from .....workers.migration_step import MigrationStep
from .....workers.single_step_migration import SingleStepMigration
from .....workers.placement_configuration import PlacementConfiguration
from .....workers.scripts.consumer_script import ConsumerScript

__all__ = ["SettingEditResponse", "Limits", "Migrations", "MigrationsWorkersMultipleStepMigrations", "Observability"]


class Limits(BaseModel):
    cpu_ms: Optional[int] = None
    """The amount of CPU time this Worker can use in milliseconds."""


class MigrationsWorkersMultipleStepMigrations(BaseModel):
    new_tag: Optional[str] = None
    """Tag to set as the latest migration tag."""

    old_tag: Optional[str] = None
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Optional[List[MigrationStep]] = None
    """Migrations to apply in order."""


Migrations: TypeAlias = Union[SingleStepMigration, MigrationsWorkersMultipleStepMigrations]


class Observability(BaseModel):
    enabled: bool
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float] = None
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """


class SettingEditResponse(BaseModel):
    bindings: Optional[List[Binding]] = None
    """List of bindings attached to this Worker"""

    compatibility_date: Optional[str] = None
    """Date indicating targeted support in the Workers runtime.

    Backwards incompatible fixes to the runtime following this date will not affect
    this Worker.
    """

    compatibility_flags: Optional[List[str]] = None
    """Flags that enable or disable certain features in the Workers runtime.

    Used to enable upcoming features or opt in or out of specific changes not
    included in a `compatibility_date`.
    """

    limits: Optional[Limits] = None
    """Limits to apply for this Worker."""

    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    migrations: Optional[Migrations] = None
    """Migrations to apply for Durable Objects associated with this Worker."""

    observability: Optional[Observability] = None
    """Observability settings for the Worker."""

    placement: Optional[PlacementConfiguration] = None

    tags: Optional[List[str]] = None
    """Tags to help you manage your Workers"""

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[Literal["bundled", "unbound"]] = None
    """Usage model for the Worker invocations."""
