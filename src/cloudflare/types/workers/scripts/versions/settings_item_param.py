# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import TypedDict

from ....binding_item_param import BindingItemParam
from ..consumer_script_param import ConsumerScriptParam
from .compatibility_flags_item import CompatibilityFlagsItem
from ....stepped_migration_param import SteppedMigrationParam
from ....single_step_migration_param import SingleStepMigrationParam
from ....placement_configuration_param import PlacementConfigurationParam

__all__ = ["SettingsItemParam", "Migrations"]

Migrations = Union[SingleStepMigrationParam, SteppedMigrationParam]


class SettingsItemParam(TypedDict, total=False):
    bindings: Iterable[BindingItemParam]
    """List of bindings attached to this Worker"""

    compatibility_date: str
    """Opt your Worker into changes after this date"""

    compatibility_flags: List[CompatibilityFlagsItem]
    """Opt your Worker into specific changes"""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    migrations: Migrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    placement: PlacementConfigurationParam

    tags: List[str]
    """Tags to help you manage your Workers"""

    tail_consumers: Iterable[ConsumerScriptParam]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: str
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""
