# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from ...._models import BaseModel
from ...kv_namespace_binding import KVNamespaceBinding

__all__ = ["BindingGetResponse", "BindingGetResponseItem", "BindingGetResponseItemWorkersWasmModuleBinding"]


class BindingGetResponseItemWorkersWasmModuleBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["wasm_module"]
    """The class of resource that the binding provides."""


BindingGetResponseItem = Union[KVNamespaceBinding, BindingGetResponseItemWorkersWasmModuleBinding]

BindingGetResponse = List[BindingGetResponseItem]
