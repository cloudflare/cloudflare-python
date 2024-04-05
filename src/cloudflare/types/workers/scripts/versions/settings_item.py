# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from .binding_item import BindingItem
from .compatibility_flags_item import CompatibilityFlagsItem

__all__ = [
    "SettingsItem",
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


class MigrationsWorkersSingleStepMigrationsRenamedClass(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class MigrationsWorkersSingleStepMigrationsTransferredClass(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    from_script: Optional[str] = None

    to: Optional[str] = None


class MigrationsWorkersSingleStepMigrations(BaseModel):
    deleted_classes: Optional[List[str]] = None
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: Optional[List[str]] = None
    """A list of classes to create Durable Object namespaces from."""

    new_tag: Optional[str] = None
    """Tag to set as the latest migration tag."""

    old_tag: Optional[str] = None
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    renamed_classes: Optional[List[MigrationsWorkersSingleStepMigrationsRenamedClass]] = None
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Optional[List[MigrationsWorkersSingleStepMigrationsTransferredClass]] = None
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


class MigrationsWorkersSteppedMigrationsStepRenamedClass(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class MigrationsWorkersSteppedMigrationsStepTransferredClass(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    from_script: Optional[str] = None

    to: Optional[str] = None


class MigrationsWorkersSteppedMigrationsStep(BaseModel):
    deleted_classes: Optional[List[str]] = None
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: Optional[List[str]] = None
    """A list of classes to create Durable Object namespaces from."""

    renamed_classes: Optional[List[MigrationsWorkersSteppedMigrationsStepRenamedClass]] = None
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Optional[List[MigrationsWorkersSteppedMigrationsStepTransferredClass]] = None
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


class MigrationsWorkersSteppedMigrations(BaseModel):
    new_tag: Optional[str] = None
    """Tag to set as the latest migration tag."""

    old_tag: Optional[str] = None
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Optional[List[MigrationsWorkersSteppedMigrationsStep]] = None
    """Migrations to apply in order."""


Migrations = Union[MigrationsWorkersSingleStepMigrations, MigrationsWorkersSteppedMigrations]


class Placement(BaseModel):
    mode: Optional[Literal["smart"]] = None
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    Only `"smart"` is currently supported
    """


class TailConsumer(BaseModel):
    service: str
    """Name of Worker that is to be the consumer."""

    environment: Optional[str] = None
    """Optional environment if the Worker utilizes one."""

    namespace: Optional[str] = None
    """Optional dispatch namespace the script belongs to."""


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

    placement: Optional[Placement] = None

    tags: Optional[List[str]] = None
    """Tags to help you manage your Workers"""

    tail_consumers: Optional[List[TailConsumer]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[str] = None
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""
