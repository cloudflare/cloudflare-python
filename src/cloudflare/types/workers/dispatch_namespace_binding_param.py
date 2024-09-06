# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

from typing import List

__all__ = ["DispatchNamespaceBindingParam", "Outbound", "OutboundWorker"]


class OutboundWorker(TypedDict, total=False):
    environment: str
    """Environment of the outbound worker"""

    service: str
    """Name of the outbound worker"""


class Outbound(TypedDict, total=False):
    params: List[str]
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters
    """

    worker: OutboundWorker
    """Outbound worker"""


class DispatchNamespaceBindingParam(TypedDict, total=False):
    namespace: Required[str]
    """Namespace to bind to"""

    type: Required[Literal["dispatch_namespace"]]
    """The class of resource that the binding provides."""

    outbound: Outbound
    """Outbound worker"""
