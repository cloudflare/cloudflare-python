# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "BindingItemParam",
    "WorkersKVNamespaceBinding",
    "WorkersServiceBinding",
    "WorkersDoBinding",
    "WorkersR2Binding",
    "WorkersQueueBinding",
    "WorkersD1Binding",
    "WorkersDispatchNamespaceBinding",
    "WorkersDispatchNamespaceBindingOutbound",
    "WorkersDispatchNamespaceBindingOutboundWorker",
    "WorkersMTLSCERTBinding",
]


class WorkersKVNamespaceBinding(TypedDict, total=False):
    type: Required[Literal["kv_namespace"]]
    """The class of resource that the binding provides."""


class WorkersServiceBinding(TypedDict, total=False):
    environment: Required[str]
    """Optional environment if the Worker utilizes one."""

    service: Required[str]
    """Name of Worker to bind to"""

    type: Required[Literal["service"]]
    """The class of resource that the binding provides."""


class WorkersDoBinding(TypedDict, total=False):
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


class WorkersR2Binding(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to"""

    type: Required[Literal["r2_bucket"]]
    """The class of resource that the binding provides."""


class WorkersQueueBinding(TypedDict, total=False):
    queue_name: Required[str]
    """Name of the Queue to bind to"""

    type: Required[Literal["queue"]]
    """The class of resource that the binding provides."""


class WorkersD1Binding(TypedDict, total=False):
    id: Required[str]
    """ID of the D1 database to bind to"""

    name: Required[str]
    """The name of the D1 database associated with the 'id' provided."""

    type: Required[Literal["d1"]]
    """The class of resource that the binding provides."""


class WorkersDispatchNamespaceBindingOutboundWorker(TypedDict, total=False):
    environment: str
    """Environment of the outbound worker"""

    service: str
    """Name of the outbound worker"""


class WorkersDispatchNamespaceBindingOutbound(TypedDict, total=False):
    params: List[str]
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters
    """

    worker: WorkersDispatchNamespaceBindingOutboundWorker
    """Outbound worker"""


class WorkersDispatchNamespaceBinding(TypedDict, total=False):
    namespace: Required[str]
    """Namespace to bind to"""

    type: Required[Literal["dispatch_namespace"]]
    """The class of resource that the binding provides."""

    outbound: WorkersDispatchNamespaceBindingOutbound
    """Outbound worker"""


class WorkersMTLSCERTBinding(TypedDict, total=False):
    certificate: Required[object]

    type: Required[Literal["mtls_certificate"]]
    """The class of resource that the binding provides."""

    certificate_id: str
    """ID of the certificate to bind to"""


BindingItemParam = Union[
    WorkersKVNamespaceBinding,
    WorkersServiceBinding,
    WorkersDoBinding,
    WorkersR2Binding,
    WorkersQueueBinding,
    WorkersD1Binding,
    WorkersDispatchNamespaceBinding,
    WorkersMTLSCERTBinding,
]
