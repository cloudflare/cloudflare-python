# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["KVNamespaceBindingParam"]


class KVNamespaceBindingParam(TypedDict, total=False):
    type: Required[Literal["kv_namespace"]]
    """The class of resource that the binding provides."""
