# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ServiceToken"]


class ServiceToken(BaseModel):
    id: Optional[str] = None
    """The ID of the service token."""

    client_id: Optional[str] = None
    """The Client ID for the service token.

    Access will check for this value in the `CF-Access-Client-ID` request header.
    """

    created_at: Optional[datetime] = None

    duration: Optional[str] = None
    """The duration for how long the service token will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. The default is 1 year in hours (8760h).
    """

    expires_at: Optional[datetime] = None

    last_seen_at: Optional[datetime] = None

    name: Optional[str] = None
    """The name of the service token."""

    updated_at: Optional[datetime] = None
