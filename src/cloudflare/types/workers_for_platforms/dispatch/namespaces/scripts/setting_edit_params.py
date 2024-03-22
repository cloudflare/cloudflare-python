# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "SettingEditParams",
    "Error",
    "Message",
    "Result",
    "ResultBinding",
    "ResultBindingWorkersKVNamespaceBinding",
    "ResultBindingWorkersServiceBinding",
    "ResultBindingWorkersDoBinding",
    "ResultBindingWorkersR2Binding",
    "ResultBindingWorkersQueueBinding",
    "ResultBindingWorkersD1Binding",
    "ResultBindingWorkersDispatchNamespaceBinding",
    "ResultBindingWorkersDispatchNamespaceBindingOutbound",
    "ResultBindingWorkersDispatchNamespaceBindingOutboundWorker",
    "ResultBindingWorkersMTLSCERTBinding",
    "ResultMigrations",
    "ResultMigrationsWorkersSingleStepMigrations",
    "ResultMigrationsWorkersSingleStepMigrationsRenamedClass",
    "ResultMigrationsWorkersSingleStepMigrationsTransferredClass",
    "ResultMigrationsWorkersSteppedMigrations",
    "ResultMigrationsWorkersSteppedMigrationsStep",
    "ResultMigrationsWorkersSteppedMigrationsStepRenamedClass",
    "ResultMigrationsWorkersSteppedMigrationsStepTransferredClass",
    "ResultPlacement",
    "ResultTailConsumer",
]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    errors: Required[Iterable[Error]]

    messages: Required[Iterable[Message]]

    result: Required[Result]

    success: Required[Literal[True]]
    """Whether the API call was successful"""


class Error(TypedDict, total=False):
    code: Required[int]

    message: Required[str]


class Message(TypedDict, total=False):
    code: Required[int]

    message: Required[str]


class ResultBindingWorkersKVNamespaceBinding(TypedDict, total=False):
    type: Required[Literal["kv_namespace"]]
    """The class of resource that the binding provides."""


class ResultBindingWorkersServiceBinding(TypedDict, total=False):
    environment: Required[str]
    """Optional environment if the Worker utilizes one."""

    service: Required[str]
    """Name of Worker to bind to"""

    type: Required[Literal["service"]]
    """The class of resource that the binding provides."""


class ResultBindingWorkersDoBinding(TypedDict, total=False):
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


class ResultBindingWorkersR2Binding(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to"""

    type: Required[Literal["r2_bucket"]]
    """The class of resource that the binding provides."""


class ResultBindingWorkersQueueBinding(TypedDict, total=False):
    queue_name: Required[str]
    """Name of the Queue to bind to"""

    type: Required[Literal["queue"]]
    """The class of resource that the binding provides."""


class ResultBindingWorkersD1Binding(TypedDict, total=False):
    id: Required[str]
    """ID of the D1 database to bind to"""

    name: Required[str]
    """The name of the D1 database associated with the 'id' provided."""

    type: Required[Literal["d1"]]
    """The class of resource that the binding provides."""


class ResultBindingWorkersDispatchNamespaceBindingOutboundWorker(TypedDict, total=False):
    environment: str
    """Environment of the outbound worker"""

    service: str
    """Name of the outbound worker"""


class ResultBindingWorkersDispatchNamespaceBindingOutbound(TypedDict, total=False):
    params: List[str]
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters
    """

    worker: ResultBindingWorkersDispatchNamespaceBindingOutboundWorker
    """Outbound worker"""


class ResultBindingWorkersDispatchNamespaceBinding(TypedDict, total=False):
    namespace: Required[str]
    """Namespace to bind to"""

    type: Required[Literal["dispatch_namespace"]]
    """The class of resource that the binding provides."""

    outbound: ResultBindingWorkersDispatchNamespaceBindingOutbound
    """Outbound worker"""


class ResultBindingWorkersMTLSCERTBinding(TypedDict, total=False):
    type: Required[Literal["mtls_certificate"]]
    """The class of resource that the binding provides."""

    certificate_id: str
    """ID of the certificate to bind to"""


ResultBinding = Union[
    ResultBindingWorkersKVNamespaceBinding,
    ResultBindingWorkersServiceBinding,
    ResultBindingWorkersDoBinding,
    ResultBindingWorkersR2Binding,
    ResultBindingWorkersQueueBinding,
    ResultBindingWorkersD1Binding,
    ResultBindingWorkersDispatchNamespaceBinding,
    ResultBindingWorkersMTLSCERTBinding,
]

_ResultMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords = TypedDict(
    "_ResultMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ResultMigrationsWorkersSingleStepMigrationsRenamedClass(
    _ResultMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords, total=False
):
    to: str


_ResultMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords = TypedDict(
    "_ResultMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ResultMigrationsWorkersSingleStepMigrationsTransferredClass(
    _ResultMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords, total=False
):
    from_script: str

    to: str


class ResultMigrationsWorkersSingleStepMigrations(TypedDict, total=False):
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

    renamed_classes: Iterable[ResultMigrationsWorkersSingleStepMigrationsRenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[ResultMigrationsWorkersSingleStepMigrationsTransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


_ResultMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords = TypedDict(
    "_ResultMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ResultMigrationsWorkersSteppedMigrationsStepRenamedClass(
    _ResultMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords, total=False
):
    to: str


_ResultMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords = TypedDict(
    "_ResultMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ResultMigrationsWorkersSteppedMigrationsStepTransferredClass(
    _ResultMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords, total=False
):
    from_script: str

    to: str


class ResultMigrationsWorkersSteppedMigrationsStep(TypedDict, total=False):
    deleted_classes: List[str]
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: List[str]
    """A list of classes to create Durable Object namespaces from."""

    renamed_classes: Iterable[ResultMigrationsWorkersSteppedMigrationsStepRenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[ResultMigrationsWorkersSteppedMigrationsStepTransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


class ResultMigrationsWorkersSteppedMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[ResultMigrationsWorkersSteppedMigrationsStep]
    """Migrations to apply in order."""


ResultMigrations = Union[ResultMigrationsWorkersSingleStepMigrations, ResultMigrationsWorkersSteppedMigrations]


class ResultPlacement(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    Only `"smart"` is currently supported
    """


class ResultTailConsumer(TypedDict, total=False):
    service: Required[str]
    """Name of Worker that is to be the consumer."""

    environment: str
    """Optional environment if the Worker utilizes one."""

    namespace: str
    """Optional dispatch namespace the script belongs to."""


class Result(TypedDict, total=False):
    bindings: Iterable[ResultBinding]
    """List of bindings attached to this Worker"""

    compatibility_date: str
    """Opt your Worker into changes after this date"""

    compatibility_flags: List[str]
    """Opt your Worker into specific changes"""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    migrations: ResultMigrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    placement: ResultPlacement

    tags: List[str]
    """Tags to help you manage your Workers"""

    tail_consumers: Iterable[ResultTailConsumer]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: str
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""
