# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .kv_namespace_binding import KVNamespaceBinding

from .service_binding import ServiceBinding

from .durable_object_binding import DurableObjectBinding

from .r2_binding import R2Binding

from .d1_binding import D1Binding

from .dispatch_namespace_binding import DispatchNamespaceBinding

from .mtls_cert_binding import MTLSCERTBinding

from ..._models import BaseModel

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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
