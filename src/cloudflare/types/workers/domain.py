# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Domain"]


class Domain(BaseModel):
    id: Optional[str] = None
    """Identifer of the Worker Domain."""

    environment: Optional[str] = None
    """Worker environment associated with the zone and hostname."""

    hostname: Optional[str] = None
    """Hostname of the Worker Domain."""

    service: Optional[str] = None
    """Worker service associated with the zone and hostname."""

    zone_id: Optional[str] = None
    """Identifier of the zone."""

    zone_name: Optional[str] = None
    """Name of the zone."""
