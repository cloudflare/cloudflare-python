# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DispatchNamespaceBinding", "Outbound", "OutboundWorker"]


class OutboundWorker(BaseModel):
    environment: Optional[str] = None
    """Environment of the outbound worker"""

    service: Optional[str] = None
    """Name of the outbound worker"""


class Outbound(BaseModel):
    params: Optional[List[str]] = None
    """
    Pass information from the Dispatch Worker to the Outbound Worker through the
    parameters
    """

    worker: Optional[OutboundWorker] = None
    """Outbound worker"""


class DispatchNamespaceBinding(BaseModel):
    name: str
    """A JavaScript variable name for the binding."""

    namespace: str
    """Namespace to bind to"""

    type: Literal["dispatch_namespace"]
    """The class of resource that the binding provides."""

    outbound: Optional[Outbound] = None
    """Outbound worker"""
