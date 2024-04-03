# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "SettingEditParams",
    "Settings",
    "SettingsBinding",
    "SettingsBindingWorkersKVNamespaceBinding",
    "SettingsBindingWorkersServiceBinding",
    "SettingsBindingWorkersDoBinding",
    "SettingsBindingWorkersR2Binding",
    "SettingsBindingWorkersQueueBinding",
    "SettingsBindingWorkersD1Binding",
    "SettingsBindingWorkersDispatchNamespaceBinding",
    "SettingsBindingWorkersDispatchNamespaceBindingOutbound",
    "SettingsBindingWorkersDispatchNamespaceBindingOutboundWorker",
    "SettingsBindingWorkersMTLSCERTBinding",
    "SettingsMigrations",
    "SettingsMigrationsWorkersSingleStepMigrations",
    "SettingsMigrationsWorkersSingleStepMigrationsRenamedClass",
    "SettingsMigrationsWorkersSingleStepMigrationsTransferredClass",
    "SettingsMigrationsWorkersSteppedMigrations",
    "SettingsMigrationsWorkersSteppedMigrationsStep",
    "SettingsMigrationsWorkersSteppedMigrationsStepRenamedClass",
    "SettingsMigrationsWorkersSteppedMigrationsStepTransferredClass",
    "SettingsPlacement",
    "SettingsTailConsumer",
]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    settings: Settings


class SettingsBindingWorkersKVNamespaceBinding(TypedDict, total=False):
    type: Required[Literal["kv_namespace"]]
    """The class of resource that the binding provides."""


class SettingsBindingWorkersServiceBinding(TypedDict, total=False):
    environment: Required[str]
    """Optional environment if the Worker utilizes one."""

    service: Required[str]
    """Name of Worker to bind to"""

    type: Required[Literal["service"]]
    """The class of resource that the binding provides."""


class SettingsBindingWorkersDoBinding(TypedDict, total=False):
    class_name: Required[str]
    """The exported class name of the Durable Object"""

    type: Required[Literal["durable_object_namespace"]]
    """The class of resource that the binding provides."""

    environment: str
    """The environment of the script_name to bind to"""

    script_name: str
    """
    The script where the Durable Object is defined, if it is external to this Worker
    """


class SettingsBindingWorkersR2Binding(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to"""

    type: Required[Literal["r2_bucket"]]
    """The class of resource that the binding provides."""


class SettingsBindingWorkersQueueBinding(TypedDict, total=False):
    queue_name: Required[str]
    """Name of the Queue to bind to"""

    type: Required[Literal["queue"]]
    """The class of resource that the binding provides."""


class SettingsBindingWorkersD1Binding(TypedDict, total=False):
    id: Required[str]
    """ID of the D1 database to bind to"""

    name: Required[str]
    """The name of the D1 database associated with the 'id' provided."""

    type: Required[Literal["d1"]]
    """The class of resource that the binding provides."""


class SettingsBindingWorkersDispatchNamespaceBindingOutboundWorker(TypedDict, total=False):
    environment: str
    """Environment of the outbound worker"""

    service: str
    """Name of the outbound worker"""


class SettingsBindingWorkersDispatchNamespaceBindingOutbound(TypedDict, total=False):
    params: List[str]
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters
    """

    worker: SettingsBindingWorkersDispatchNamespaceBindingOutboundWorker
    """Outbound worker"""


class SettingsBindingWorkersDispatchNamespaceBinding(TypedDict, total=False):
    namespace: Required[str]
    """Namespace to bind to"""

    type: Required[Literal["dispatch_namespace"]]
    """The class of resource that the binding provides."""

    outbound: SettingsBindingWorkersDispatchNamespaceBindingOutbound
    """Outbound worker"""


class SettingsBindingWorkersMTLSCERTBinding(TypedDict, total=False):
    certificate: Required[object]

    type: Required[Literal["mtls_certificate"]]
    """The class of resource that the binding provides."""

    certificate_id: str
    """ID of the certificate to bind to"""


SettingsBinding = Union[
    SettingsBindingWorkersKVNamespaceBinding,
    SettingsBindingWorkersServiceBinding,
    SettingsBindingWorkersDoBinding,
    SettingsBindingWorkersR2Binding,
    SettingsBindingWorkersQueueBinding,
    SettingsBindingWorkersD1Binding,
    SettingsBindingWorkersDispatchNamespaceBinding,
    SettingsBindingWorkersMTLSCERTBinding,
]

_SettingsMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords = TypedDict(
    "_SettingsMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class SettingsMigrationsWorkersSingleStepMigrationsRenamedClass(
    _SettingsMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords, total=False
):
    to: str


_SettingsMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords = TypedDict(
    "_SettingsMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class SettingsMigrationsWorkersSingleStepMigrationsTransferredClass(
    _SettingsMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords, total=False
):
    from_script: str

    to: str


class SettingsMigrationsWorkersSingleStepMigrations(TypedDict, total=False):
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

    renamed_classes: Iterable[SettingsMigrationsWorkersSingleStepMigrationsRenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[SettingsMigrationsWorkersSingleStepMigrationsTransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


_SettingsMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords = TypedDict(
    "_SettingsMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class SettingsMigrationsWorkersSteppedMigrationsStepRenamedClass(
    _SettingsMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords, total=False
):
    to: str


_SettingsMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords = TypedDict(
    "_SettingsMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class SettingsMigrationsWorkersSteppedMigrationsStepTransferredClass(
    _SettingsMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords, total=False
):
    from_script: str

    to: str


class SettingsMigrationsWorkersSteppedMigrationsStep(TypedDict, total=False):
    deleted_classes: List[str]
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: List[str]
    """A list of classes to create Durable Object namespaces from."""

    renamed_classes: Iterable[SettingsMigrationsWorkersSteppedMigrationsStepRenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[SettingsMigrationsWorkersSteppedMigrationsStepTransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


class SettingsMigrationsWorkersSteppedMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[SettingsMigrationsWorkersSteppedMigrationsStep]
    """Migrations to apply in order."""


SettingsMigrations = Union[SettingsMigrationsWorkersSingleStepMigrations, SettingsMigrationsWorkersSteppedMigrations]


class SettingsPlacement(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    Only `"smart"` is currently supported
    """


class SettingsTailConsumer(TypedDict, total=False):
    service: Required[str]
    """Name of Worker that is to be the consumer."""

    environment: str
    """Optional environment if the Worker utilizes one."""

    namespace: str
    """Optional dispatch namespace the script belongs to."""


class Settings(TypedDict, total=False):
    bindings: Iterable[SettingsBinding]
    """List of bindings attached to this Worker"""

    compatibility_date: str
    """Opt your Worker into changes after this date"""

    compatibility_flags: List[str]
    """Opt your Worker into specific changes"""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    migrations: SettingsMigrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    placement: SettingsPlacement

    tags: List[str]
    """Tags to help you manage your Workers"""

    tail_consumers: Iterable[SettingsTailConsumer]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: str
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""
