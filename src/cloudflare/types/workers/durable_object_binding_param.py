# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

__all__ = ["DurableObjectBindingParam"]


class DurableObjectBindingParam(TypedDict, total=False):
    class_name: Required[str]
    """The exported class name of the Durable Object"""

    type: Required[Literal["durable_object_namespace"]]
    """The class of resource that the binding provides."""

    environment: str
    """The environment of the script_name to bind to"""

    script_name: str
    """
    The script where the Durable Object is defined, if it is external to this Worker
    """
