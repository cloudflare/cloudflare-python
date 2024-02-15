# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse"]


class OutgoingSecondaryDNSPrimaryZoneCreatePrimaryZoneConfigurationResponse(BaseModel):
    id: Optional[object] = None

    checked_time: Optional[str] = None
    """The time for a specific event."""

    created_time: Optional[str] = None
    """The time for a specific event."""

    last_transferred_time: Optional[str] = None
    """The time for a specific event."""

    name: Optional[str] = None
    """Zone name."""

    peers: Optional[List[object]] = None
    """A list of peer tags."""

    soa_serial: Optional[float] = None
    """The serial number of the SOA for the given zone."""
