# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = [
    "BindingGetResponse",
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


class WorkersKVNamespaceBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace_id: str
    """Namespace identifier tag."""

    type: Literal["kv_namespace"]
    """The class of resource that the binding provides."""


class WorkersServiceBinding(BaseModel):
    environment: str
    """Optional environment if the Worker utilizes one."""

    name: str
    """A JavaScript variable name for the binding."""

    service: str
    """Name of Worker to bind to"""

    type: Literal["service"]
    """The class of resource that the binding provides."""


class WorkersDoBinding(BaseModel):
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


class WorkersR2Binding(BaseModel):
    bucket_name: str
    """R2 bucket to bind to"""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["r2_bucket"]
    """The class of resource that the binding provides."""


class WorkersQueueBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    queue_name: str
    """Name of the Queue to bind to"""

    type: Literal["queue"]
    """The class of resource that the binding provides."""


class WorkersD1Binding(BaseModel):
    id: str
    """ID of the D1 database to bind to"""

    binding: str
    """A JavaScript variable name for the binding."""

    name: str
    """The name of the D1 database associated with the 'id' provided."""

    type: Literal["d1"]
    """The class of resource that the binding provides."""


class WorkersDispatchNamespaceBindingOutboundWorker(BaseModel):
    environment: Optional[str] = None
    """Environment of the outbound worker"""

    service: Optional[str] = None
    """Name of the outbound worker"""


class WorkersDispatchNamespaceBindingOutbound(BaseModel):
    params: Optional[List[str]] = None
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters
    """

    worker: Optional[WorkersDispatchNamespaceBindingOutboundWorker] = None
    """Outbound worker"""


class WorkersDispatchNamespaceBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace: str
    """Namespace to bind to"""

    type: Literal["dispatch_namespace"]
    """The class of resource that the binding provides."""

    outbound: Optional[WorkersDispatchNamespaceBindingOutbound] = None
    """Outbound worker"""


class WorkersMTLSCERTBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["mtls_certificate"]
    """The class of resource that the binding provides."""

    certificate_id: Optional[str] = None
    """ID of the certificate to bind to"""


BindingGetResponse = Union[
    WorkersKVNamespaceBinding,
    WorkersServiceBinding,
    WorkersDoBinding,
    WorkersR2Binding,
    WorkersQueueBinding,
    WorkersD1Binding,
    WorkersDispatchNamespaceBinding,
    WorkersMTLSCERTBinding,
]
