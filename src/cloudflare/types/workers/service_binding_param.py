# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

__all__ = ["ServiceBindingParam"]

class ServiceBindingParam(TypedDict, total=False):
    environment: Required[str]
    """Optional environment if the Worker utilizes one."""

    service: Required[str]
    """Name of Worker to bind to"""

    type: Required[Literal["service"]]
    """The class of resource that the binding provides."""