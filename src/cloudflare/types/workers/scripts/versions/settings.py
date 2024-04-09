# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from .tags import Tags
from ....binding import Binding
from ....._models import BaseModel
from .compatibility_flags import CompatibilityFlags
from ....stepped_migration import SteppedMigration
from ..consumer_script_item import ConsumerScriptItem
from ....single_step_migration import SingleStepMigration
from ....placement_configuration import PlacementConfiguration

__all__ = ["Settings", "Migrations"]

Migrations = Union[SingleStepMigration, SteppedMigration]


class Settings(BaseModel):
    bindings: Optional[List[Binding]] = None
    """List of bindings attached to this Worker"""

    compatibility_date: Optional[str] = None
    """Opt your Worker into changes after this date"""

    compatibility_flags: Optional[List[CompatibilityFlags]] = None
    """Opt your Worker into specific changes"""

    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    migrations: Optional[Migrations] = None
    """Migrations to apply for Durable Objects associated with this Worker."""

    placement: Optional[PlacementConfiguration] = None

    tags: Optional[List[Tags]] = None
    """Tags to help you manage your Workers"""

    tail_consumers: Optional[List[ConsumerScriptItem]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[str] = None
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""
