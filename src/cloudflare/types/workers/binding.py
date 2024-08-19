# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .d1_binding import D1Binding
from .r2_binding import R2Binding
from .service_binding import ServiceBinding
from .mtls_cert_binding import MTLSCERTBinding
from .kv_namespace_binding import KVNamespaceBinding
from .durable_object_binding import DurableObjectBinding
from .dispatch_namespace_binding import DispatchNamespaceBinding

__all__ = ["Binding", "WorkersQueueBinding"]


class WorkersQueueBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    queue_name: str
    """Name of the Queue to bind to"""

    type: Literal["queue"]
    """The class of resource that the binding provides."""


Binding: TypeAlias = Union[
    KVNamespaceBinding,
    ServiceBinding,
    DurableObjectBinding,
    R2Binding,
    WorkersQueueBinding,
    D1Binding,
    DispatchNamespaceBinding,
    MTLSCERTBinding,
]
