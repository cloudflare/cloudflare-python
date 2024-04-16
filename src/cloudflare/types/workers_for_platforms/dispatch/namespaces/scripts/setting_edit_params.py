# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, TypedDict

from .....workers import BindingParam, SteppedMigrationParam, SingleStepMigrationParam, PlacementConfigurationParam
from .....workers.scripts import ConsumerScriptParam

__all__ = ["SettingEditParams", "Settings", "SettingsLimits", "SettingsMigrations"]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    settings: Settings


class SettingsLimits(TypedDict, total=False):
    cpu_ms: int
    """The amount of CPU time this Worker can use in milliseconds."""


SettingsMigrations = Union[SingleStepMigrationParam, SteppedMigrationParam]


class Settings(TypedDict, total=False):
    bindings: Iterable[BindingParam]
    """List of bindings attached to this Worker"""

    compatibility_date: str
    """Opt your Worker into changes after this date"""

    compatibility_flags: List[str]
    """Opt your Worker into specific changes"""

    limits: SettingsLimits
    """Limits to apply for this Worker."""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    migrations: SettingsMigrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    placement: PlacementConfigurationParam

    tags: List[str]
    """Tags to help you manage your Workers"""

    tail_consumers: Iterable[ConsumerScriptParam]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: str
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""
