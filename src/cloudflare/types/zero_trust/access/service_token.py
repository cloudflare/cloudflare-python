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

    duration: Optional[str] = None
    """The duration for how long the service token will be valid.

    Must be in the format `300ms` or `2h45m`, or the special value `forever` for
    non-expiring tokens. Valid time units are: ns, us (or µs), ms, s, m, h. The
    default is 1 year in hours (8760h).
    """

    enabled: Optional[bool] = None
    """Whether the service token is enabled.

    A disabled service token cannot be used to authenticate; both its current and
    previous `client_secret` stop being accepted, but the token itself is preserved
    and can be re-enabled at any time. Defaults to enabled when omitted on create.
    """

    expires_at: Optional[datetime] = None

    name: Optional[str] = None
    """The name of the service token."""
