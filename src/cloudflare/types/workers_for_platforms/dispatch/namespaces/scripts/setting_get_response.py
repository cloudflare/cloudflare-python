# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ......_models import BaseModel
from .....workers.binding import Binding
from .....workers.stepped_migration import SteppedMigration
from .....workers.single_step_migration import SingleStepMigration
from .....workers.placement_configuration import PlacementConfiguration
from .....workers.scripts.consumer_script import ConsumerScript

__all__ = ["SettingGetResponse", "Limits", "Migrations", "Observability"]


class Limits(BaseModel):
    cpu_ms: Optional[int] = None
    """The amount of CPU time this Worker can use in milliseconds."""


Migrations: TypeAlias = Union[SingleStepMigration, SteppedMigration]


class Observability(BaseModel):
    enabled: bool
    """Whether observability is enabled for the Worker"""

    head_sampling_rate: Optional[float] = None
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """


class SettingGetResponse(BaseModel):
    bindings: Optional[List[Binding]] = None
    """List of bindings attached to this Worker"""

    compatibility_date: Optional[str] = None
    """Opt your Worker into changes after this date"""

    compatibility_flags: Optional[List[str]] = None
    """Opt your Worker into specific changes"""

    limits: Optional[Limits] = None
    """Limits to apply for this Worker."""

    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    migrations: Optional[Migrations] = None
    """Migrations to apply for Durable Objects associated with this Worker."""

    observability: Optional[Observability] = None
    """Observability settings for the Worker"""

    placement: Optional[PlacementConfiguration] = None

    tags: Optional[List[str]] = None
    """Tags to help you manage your Workers"""

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[str] = None
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""
