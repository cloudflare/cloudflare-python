# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "BindingListResponse",
    "BindingListResponseItem",
    "BindingListResponseItemWorkersKvNamespaceBinding",
    "BindingListResponseItemWorkersWasmModuleBinding",
]


class BindingListResponseItemWorkersKvNamespaceBinding(BaseModel):
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
    BindingListResponseItemWorkersKvNamespaceBinding, BindingListResponseItemWorkersWasmModuleBinding
]

BindingListResponse = List[BindingListResponseItem]
