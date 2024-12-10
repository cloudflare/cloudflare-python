# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["IncomingGetResponse"]


class IncomingGetResponse(BaseModel):
    id: Optional[str] = None

    auto_refresh_seconds: Optional[float] = None
    """
    How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
    applicable for primary zones.
    """

    checked_time: Optional[str] = None
    """The time for a specific event."""

    created_time: Optional[str] = None
    """The time for a specific event."""

    modified_time: Optional[str] = None
    """The time for a specific event."""

    name: Optional[str] = None
    """Zone name."""

    peers: Optional[List[str]] = None
    """A list of peer tags."""

    soa_serial: Optional[float] = None
    """The serial number of the SOA for the given zone."""
