# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import TypedDict

from .tags import Tags
from ....binding_param import BindingParam
from .compatibility_flags import CompatibilityFlags
from ....stepped_migration_param import SteppedMigrationParam
from ..consumer_script_item_param import ConsumerScriptItemParam
from ....single_step_migration_param import SingleStepMigrationParam
from ....placement_configuration_param import PlacementConfigurationParam

__all__ = ["SettingsParam", "Migrations"]

Migrations = Union[SingleStepMigrationParam, SteppedMigrationParam]


class SettingsParam(TypedDict, total=False):
    bindings: Iterable[BindingParam]
    """List of bindings attached to this Worker"""

    compatibility_date: str
    """Opt your Worker into changes after this date"""

    compatibility_flags: List[CompatibilityFlags]
    """Opt your Worker into specific changes"""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    migrations: Migrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    placement: PlacementConfigurationParam

    tags: List[Tags]
    """Tags to help you manage your Workers"""

    tail_consumers: Iterable[ConsumerScriptItemParam]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: str
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""
