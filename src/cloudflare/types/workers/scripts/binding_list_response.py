# File generated from our OpenAPI spec by Stainless.

from typing import List, Union
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "BindingListResponse",
    "BindingListResponseItem",
    "BindingListResponseItemWorkersKVNamespaceBinding",
    "BindingListResponseItemWorkersWasmModuleBinding",
]


class BindingListResponseItemWorkersKVNamespaceBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace_id: str
    """Namespace identifier tag."""

    type: Literal["kv_namespace"]
    """The class of resource that the binding provides."""


class BindingListResponseItemWorkersWasmModuleBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["wasm_module"]
    """The class of resource that the binding provides."""


BindingListResponseItem = Union[
    BindingListResponseItemWorkersKVNamespaceBinding, BindingListResponseItemWorkersWasmModuleBinding
]

BindingListResponse = List[BindingListResponseItem]
