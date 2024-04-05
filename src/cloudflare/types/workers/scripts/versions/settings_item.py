# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ....._models import BaseModel
from ....binding_item import BindingItem
from ..consumer_script import ConsumerScript
from ....stepped_migration import SteppedMigration
from ....single_step_migration import SingleStepMigration
from .compatibility_flags_item import CompatibilityFlagsItem
from ....placement_configuration import PlacementConfiguration

__all__ = ["SettingsItem", "Migrations"]

Migrations = Union[SingleStepMigration, SteppedMigration]


class SettingsItem(BaseModel):
    bindings: Optional[List[BindingItem]] = None
    """List of bindings attached to this Worker"""

    compatibility_date: Optional[str] = None
    """Opt your Worker into changes after this date"""

    compatibility_flags: Optional[List[CompatibilityFlagsItem]] = None
    """Opt your Worker into specific changes"""

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
