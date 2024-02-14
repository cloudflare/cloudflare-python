# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["DomainWorkerDomainListDomainsResponse", "DomainWorkerDomainListDomainsResponseItem"]


class DomainWorkerDomainListDomainsResponseItem(BaseModel):
    id: Optional[object] = None
    """Identifer of the Worker Domain."""

    environment: Optional[str] = None
    """Worker environment associated with the zone and hostname."""

    hostname: Optional[str] = None
    """Hostname of the Worker Domain."""

    service: Optional[str] = None
    """Worker service associated with the zone and hostname."""

    zone_id: Optional[object] = None
    """Identifier of the zone."""

    zone_name: Optional[str] = None
    """Name of the zone."""


DomainWorkerDomainListDomainsResponse = List[DomainWorkerDomainListDomainsResponseItem]
