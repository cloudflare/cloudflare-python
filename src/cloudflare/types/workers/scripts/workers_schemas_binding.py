# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WorkersSchemasBinding", "WorkersKVNamespaceBinding", "WorkersWasmModuleBinding"]


class WorkersKVNamespaceBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace_id: str
    """Namespace identifier tag."""

    type: Literal["kv_namespace"]
    """The class of resource that the binding provides."""


class WorkersWasmModuleBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["wasm_module"]
    """The class of resource that the binding provides."""


WorkersSchemasBinding = Union[WorkersKVNamespaceBinding, WorkersWasmModuleBinding]
