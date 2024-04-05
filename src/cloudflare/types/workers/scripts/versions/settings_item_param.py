# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .binding_item_param import BindingItemParam
from .compatibility_flags_item import CompatibilityFlagsItem

__all__ = [
    "SettingsItemParam",
    "Migrations",
    "MigrationsWorkersSingleStepMigrations",
    "MigrationsWorkersSingleStepMigrationsRenamedClass",
    "MigrationsWorkersSingleStepMigrationsTransferredClass",
    "MigrationsWorkersSteppedMigrations",
    "MigrationsWorkersSteppedMigrationsStep",
    "MigrationsWorkersSteppedMigrationsStepRenamedClass",
    "MigrationsWorkersSteppedMigrationsStepTransferredClass",
    "Placement",
    "TailConsumer",
]

_MigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords = TypedDict(
    "_MigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MigrationsWorkersSingleStepMigrationsRenamedClass(
    _MigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords, total=False
):
    to: str


_MigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords = TypedDict(
    "_MigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MigrationsWorkersSingleStepMigrationsTransferredClass(
    _MigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords, total=False
):
    from_script: str

    to: str


class MigrationsWorkersSingleStepMigrations(TypedDict, total=False):
    deleted_classes: List[str]
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: List[str]
    """A list of classes to create Durable Object namespaces from."""

    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    renamed_classes: Iterable[MigrationsWorkersSingleStepMigrationsRenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[MigrationsWorkersSingleStepMigrationsTransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


_MigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords = TypedDict(
    "_MigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MigrationsWorkersSteppedMigrationsStepRenamedClass(
    _MigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords, total=False
):
    to: str


_MigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords = TypedDict(
    "_MigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MigrationsWorkersSteppedMigrationsStepTransferredClass(
    _MigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords, total=False
):
    from_script: str

    to: str


class MigrationsWorkersSteppedMigrationsStep(TypedDict, total=False):
    deleted_classes: List[str]
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: List[str]
    """A list of classes to create Durable Object namespaces from."""

    renamed_classes: Iterable[MigrationsWorkersSteppedMigrationsStepRenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[MigrationsWorkersSteppedMigrationsStepTransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


class MigrationsWorkersSteppedMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[MigrationsWorkersSteppedMigrationsStep]
    """Migrations to apply in order."""


Migrations = Union[MigrationsWorkersSingleStepMigrations, MigrationsWorkersSteppedMigrations]


class Placement(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    Only `"smart"` is currently supported
    """


class TailConsumer(TypedDict, total=False):
    service: Required[str]
    """Name of Worker that is to be the consumer."""

    environment: str
    """Optional environment if the Worker utilizes one."""

    namespace: str
    """Optional dispatch namespace the script belongs to."""


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

    placement: Placement

    tags: List[str]
    """Tags to help you manage your Workers"""

    tail_consumers: Iterable[TailConsumer]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: str
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""
