# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["DomainWorkerDomainListDomainsParams"]


class DomainWorkerDomainListDomainsParams(TypedDict, total=False):
    environment: str
    """Worker environment associated with the zone and hostname."""

    hostname: str
    """Hostname of the Worker Domain."""

    service: str
    """Worker service associated with the zone and hostname."""

    zone_id: object
    """Identifier of the zone."""

    zone_name: str
    """Name of the zone."""
