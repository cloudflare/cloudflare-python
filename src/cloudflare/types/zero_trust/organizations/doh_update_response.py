# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["DOHUpdateResponse"]


class DOHUpdateResponse(BaseModel):
    id: Optional[str] = None
    """The ID of the service token."""

    client_id: Optional[str] = None
    """The Client ID for the service token.

    Access will check for this value in the `CF-Access-Client-ID` request header.
    """

    doh_jwt_duration: Optional[str] = None
    """The duration the DoH JWT is valid for.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note that the maximum duration for this setting is the same as the
    key rotation period on the account. Default expiration is 24h
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
    and can be re-enabled. A service token reported as leaked is disabled
    automatically and cannot be re-enabled until its secret is rotated; attempting
    to do so returns a 409. Defaults to enabled when omitted on create.
    """

    expires_at: Optional[datetime] = None

    leak_report_url: Optional[str] = None
    """Where the leaked `client_secret` was found, if provided by the reporter.

    Omitted if the token has not been reported as leaked.
    """

    leak_reported_at: Optional[datetime] = None
    """
    When a secret scanning partner reported this service token's `client_secret` as
    leaked. A leaked service token is disabled and must be rotated before it can be
    re-enabled. Cleared once the secret is rotated. Omitted if the token has not
    been reported as leaked.
    """

    leak_reporter: Optional[str] = None
    """The secret scanning partner that reported the leak.

    Omitted if the token has not been reported as leaked.
    """

    name: Optional[str] = None
    """The name of the service token."""

    tags: Optional[Dict[str, str]] = None
    """Tags associated with the service token, as key-value pairs.

    On update, replaces all existing tags.
    """
