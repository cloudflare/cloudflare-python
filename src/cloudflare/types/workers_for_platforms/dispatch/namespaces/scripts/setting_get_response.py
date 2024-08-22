# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ......_models import BaseModel

from typing import Optional, List

from .....workers.single_step_migration import SingleStepMigration

from .....workers.stepped_migration import SteppedMigration

from typing_extensions import TypeAlias

from .....workers.binding import Binding

from .....workers.placement_configuration import PlacementConfiguration

from .....workers.scripts.consumer_script import ConsumerScript

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SettingGetResponse", "Limits", "Migrations"]

class Limits(BaseModel):
    cpu_ms: Optional[int] = None
    """The amount of CPU time this Worker can use in milliseconds."""

Migrations: TypeAlias = Union[SingleStepMigration, SteppedMigration]

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

    placement: Optional[PlacementConfiguration] = None

    tags: Optional[List[str]] = None
    """Tags to help you manage your Workers"""

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[str] = None
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""