# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .d1_binding_param import D1BindingParam
from .r2_binding_param import R2BindingParam
from .service_binding_param import ServiceBindingParam
from .mtls_cert_binding_param import MTLSCERTBindingParam
from .kv_namespace_binding_param import KVNamespaceBindingParam
from .durable_object_binding_param import DurableObjectBindingParam
from .dispatch_namespace_binding_param import DispatchNamespaceBindingParam

__all__ = ["BindingParam", "WorkersQueueBinding"]


class WorkersQueueBinding(TypedDict, total=False):
    queue_name: Required[str]
    """Name of the Queue to bind to"""

    type: Required[Literal["queue"]]
    """The class of resource that the binding provides."""


BindingParam: TypeAlias = Union[
    KVNamespaceBindingParam,
    ServiceBindingParam,
    DurableObjectBindingParam,
    R2BindingParam,
    WorkersQueueBinding,
    D1BindingParam,
    DispatchNamespaceBindingParam,
    MTLSCERTBindingParam,
]
