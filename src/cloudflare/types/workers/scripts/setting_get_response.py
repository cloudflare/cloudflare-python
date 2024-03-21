# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "SettingGetResponse",
    "Binding",
    "BindingWorkersKVNamespaceBinding",
    "BindingWorkersServiceBinding",
    "BindingWorkersDoBinding",
    "BindingWorkersR2Binding",
    "BindingWorkersQueueBinding",
    "BindingWorkersD1Binding",
    "BindingWorkersDispatchNamespaceBinding",
    "BindingWorkersDispatchNamespaceBindingOutbound",
    "BindingWorkersDispatchNamespaceBindingOutboundWorker",
    "BindingWorkersMTLSCERTBinding",
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


class BindingWorkersKVNamespaceBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace_id: str
    """Namespace identifier tag."""

    type: Literal["kv_namespace"]
    """The class of resource that the binding provides."""


class BindingWorkersServiceBinding(BaseModel):
    environment: str
    """Optional environment if the Worker utilizes one."""

    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Worker to bind to"""

    type: Literal["service"]
    """The class of resource that the binding provides."""


class BindingWorkersDoBinding(BaseModel):
    class_name: str
    """The exported class name of the Durable Object"""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["durable_object_namespace"]
    """The class of resource that the binding provides."""

    environment: Optional[str] = None
    """The environment of the script_name to bind to"""

    namespace_id: Optional[str] = None
    """Namespace identifier tag."""

    script_name: Optional[str] = None
    """
    The script where the Durable Object is defined, if it is external to this Worker
    """


class BindingWorkersR2Binding(BaseModel):
    bucket_name: str
    """R2 bucket to bind to"""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["r2_bucket"]
    """The class of resource that the binding provides."""


class BindingWorkersQueueBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    queue_name: str
    """Name of the Queue to bind to"""

    type: Literal["queue"]
    """The class of resource that the binding provides."""


class BindingWorkersD1Binding(BaseModel):
    id: str
    """ID of the D1 database to bind to"""

    binding: str
    """A JavaScript variable name for the binding."""

    name: str
    """The name of the D1 database associated with the 'id' provided."""

    type: Literal["d1"]
    """The class of resource that the binding provides."""


class BindingWorkersDispatchNamespaceBindingOutboundWorker(BaseModel):
    environment: Optional[str] = None
    """Environment of the outbound worker"""

    service: Optional[str] = None
    """Name of the outbound worker"""


class BindingWorkersDispatchNamespaceBindingOutbound(BaseModel):
    params: Optional[List[str]] = None
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters
    """

    worker: Optional[BindingWorkersDispatchNamespaceBindingOutboundWorker] = None
    """Outbound worker"""


class BindingWorkersDispatchNamespaceBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace: str
    """Namespace to bind to"""

    type: Literal["dispatch_namespace"]
    """The class of resource that the binding provides."""

    outbound: Optional[BindingWorkersDispatchNamespaceBindingOutbound] = None
    """Outbound worker"""


class BindingWorkersMTLSCERTBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["mtls_certificate"]
    """The class of resource that the binding provides."""

    certificate_id: Optional[str] = None
    """ID of the certificate to bind to"""


Binding = Union[
    BindingWorkersKVNamespaceBinding,
    BindingWorkersServiceBinding,
    BindingWorkersDoBinding,
    BindingWorkersR2Binding,
    BindingWorkersQueueBinding,
    BindingWorkersD1Binding,
    BindingWorkersDispatchNamespaceBinding,
    BindingWorkersMTLSCERTBinding,
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


class SettingGetResponse(BaseModel):
    bindings: Optional[List[Binding]] = None
    """List of bindings attached to this Worker"""

    compatibility_date: Optional[str] = None
    """Opt your Worker into changes after this date"""

    compatibility_flags: Optional[List[str]] = None
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
