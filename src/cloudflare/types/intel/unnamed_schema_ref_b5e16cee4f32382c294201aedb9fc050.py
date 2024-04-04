# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRefB5e16cee4f32382c294201aedb9fc050"]


class UnnamedSchemaRefB5e16cee4f32382c294201aedb9fc050(BaseModel):
    first_seen: Optional[date] = None
    """First seen date of the DNS record during the time period."""

    hostname: Optional[object] = None
    """Hostname that the IP was observed resolving to."""

    last_seen: Optional[date] = None
    """Last seen date of the DNS record during the time period."""
