# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "SettingEditParams",
    "Settings",
    "SettingsError",
    "SettingsMessage",
    "SettingsResult",
    "SettingsResultBinding",
    "SettingsResultBindingWorkersKVNamespaceBinding",
    "SettingsResultBindingWorkersServiceBinding",
    "SettingsResultBindingWorkersDoBinding",
    "SettingsResultBindingWorkersR2Binding",
    "SettingsResultBindingWorkersQueueBinding",
    "SettingsResultBindingWorkersD1Binding",
    "SettingsResultBindingWorkersDispatchNamespaceBinding",
    "SettingsResultBindingWorkersDispatchNamespaceBindingOutbound",
    "SettingsResultBindingWorkersDispatchNamespaceBindingOutboundWorker",
    "SettingsResultBindingWorkersMTLSCERTBinding",
    "SettingsResultMigrations",
    "SettingsResultMigrationsWorkersSingleStepMigrations",
    "SettingsResultMigrationsWorkersSingleStepMigrationsRenamedClass",
    "SettingsResultMigrationsWorkersSingleStepMigrationsTransferredClass",
    "SettingsResultMigrationsWorkersSteppedMigrations",
    "SettingsResultMigrationsWorkersSteppedMigrationsStep",
    "SettingsResultMigrationsWorkersSteppedMigrationsStepRenamedClass",
    "SettingsResultMigrationsWorkersSteppedMigrationsStepTransferredClass",
    "SettingsResultPlacement",
    "SettingsResultTailConsumer",
]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    settings: Settings


class SettingsError(TypedDict, total=False):
    code: Required[int]

    message: Required[str]


class SettingsMessage(TypedDict, total=False):
    code: Required[int]

    message: Required[str]


class SettingsResultBindingWorkersKVNamespaceBinding(TypedDict, total=False):
    type: Required[Literal["kv_namespace"]]
    """The class of resource that the binding provides."""


class SettingsResultBindingWorkersServiceBinding(TypedDict, total=False):
    environment: Required[str]
    """Optional environment if the Worker utilizes one."""

    service: Required[str]
    """Name of Worker to bind to"""

    type: Required[Literal["service"]]
    """The class of resource that the binding provides."""


class SettingsResultBindingWorkersDoBinding(TypedDict, total=False):
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


class SettingsResultBindingWorkersR2Binding(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to"""

    type: Required[Literal["r2_bucket"]]
    """The class of resource that the binding provides."""


class SettingsResultBindingWorkersQueueBinding(TypedDict, total=False):
    queue_name: Required[str]
    """Name of the Queue to bind to"""

    type: Required[Literal["queue"]]
    """The class of resource that the binding provides."""


class SettingsResultBindingWorkersD1Binding(TypedDict, total=False):
    id: Required[str]
    """ID of the D1 database to bind to"""

    name: Required[str]
    """The name of the D1 database associated with the 'id' provided."""

    type: Required[Literal["d1"]]
    """The class of resource that the binding provides."""


class SettingsResultBindingWorkersDispatchNamespaceBindingOutboundWorker(TypedDict, total=False):
    environment: str
    """Environment of the outbound worker"""

    service: str
    """Name of the outbound worker"""


class SettingsResultBindingWorkersDispatchNamespaceBindingOutbound(TypedDict, total=False):
    params: List[str]
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters
    """

    worker: SettingsResultBindingWorkersDispatchNamespaceBindingOutboundWorker
    """Outbound worker"""


class SettingsResultBindingWorkersDispatchNamespaceBinding(TypedDict, total=False):
    namespace: Required[str]
    """Namespace to bind to"""

    type: Required[Literal["dispatch_namespace"]]
    """The class of resource that the binding provides."""

    outbound: SettingsResultBindingWorkersDispatchNamespaceBindingOutbound
    """Outbound worker"""


class SettingsResultBindingWorkersMTLSCERTBinding(TypedDict, total=False):
    type: Required[Literal["mtls_certificate"]]
    """The class of resource that the binding provides."""

    certificate_id: str
    """ID of the certificate to bind to"""


SettingsResultBinding = Union[
    SettingsResultBindingWorkersKVNamespaceBinding,
    SettingsResultBindingWorkersServiceBinding,
    SettingsResultBindingWorkersDoBinding,
    SettingsResultBindingWorkersR2Binding,
    SettingsResultBindingWorkersQueueBinding,
    SettingsResultBindingWorkersD1Binding,
    SettingsResultBindingWorkersDispatchNamespaceBinding,
    SettingsResultBindingWorkersMTLSCERTBinding,
]

_SettingsResultMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords = TypedDict(
    "_SettingsResultMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class SettingsResultMigrationsWorkersSingleStepMigrationsRenamedClass(
    _SettingsResultMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords, total=False
):
    to: str


_SettingsResultMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords = TypedDict(
    "_SettingsResultMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class SettingsResultMigrationsWorkersSingleStepMigrationsTransferredClass(
    _SettingsResultMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords, total=False
):
    from_script: str

    to: str


class SettingsResultMigrationsWorkersSingleStepMigrations(TypedDict, total=False):
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

    renamed_classes: Iterable[SettingsResultMigrationsWorkersSingleStepMigrationsRenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[SettingsResultMigrationsWorkersSingleStepMigrationsTransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


_SettingsResultMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords = TypedDict(
    "_SettingsResultMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class SettingsResultMigrationsWorkersSteppedMigrationsStepRenamedClass(
    _SettingsResultMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords, total=False
):
    to: str


_SettingsResultMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords = TypedDict(
    "_SettingsResultMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class SettingsResultMigrationsWorkersSteppedMigrationsStepTransferredClass(
    _SettingsResultMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords, total=False
):
    from_script: str

    to: str


class SettingsResultMigrationsWorkersSteppedMigrationsStep(TypedDict, total=False):
    deleted_classes: List[str]
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: List[str]
    """A list of classes to create Durable Object namespaces from."""

    renamed_classes: Iterable[SettingsResultMigrationsWorkersSteppedMigrationsStepRenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[SettingsResultMigrationsWorkersSteppedMigrationsStepTransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


class SettingsResultMigrationsWorkersSteppedMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[SettingsResultMigrationsWorkersSteppedMigrationsStep]
    """Migrations to apply in order."""


SettingsResultMigrations = Union[
    SettingsResultMigrationsWorkersSingleStepMigrations, SettingsResultMigrationsWorkersSteppedMigrations
]


class SettingsResultPlacement(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    Only `"smart"` is currently supported
    """


class SettingsResultTailConsumer(TypedDict, total=False):
    service: Required[str]
    """Name of Worker that is to be the consumer."""

    environment: str
    """Optional environment if the Worker utilizes one."""

    namespace: str
    """Optional dispatch namespace the script belongs to."""


class SettingsResult(TypedDict, total=False):
    bindings: Iterable[SettingsResultBinding]
    """List of bindings attached to this Worker"""

    compatibility_date: str
    """Opt your Worker into changes after this date"""

    compatibility_flags: List[str]
    """Opt your Worker into specific changes"""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    migrations: SettingsResultMigrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    placement: SettingsResultPlacement

    tags: List[str]
    """Tags to help you manage your Workers"""

    tail_consumers: Iterable[SettingsResultTailConsumer]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: str
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""


class Settings(TypedDict, total=False):
    errors: Required[Iterable[SettingsError]]

    messages: Required[Iterable[SettingsMessage]]

    result: Required[SettingsResult]

    success: Required[Literal[True]]
    """Whether the API call was successful"""
