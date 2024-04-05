# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal

from ...._models import BaseModel
from ...kv_namespace_binding import KVNamespaceBinding

__all__ = ["WorkersBinding", "WorkersWasmModuleBinding"]


class WorkersWasmModuleBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["wasm_module"]
    """The class of resource that the binding provides."""


WorkersBinding = Union[KVNamespaceBinding, WorkersWasmModuleBinding]
