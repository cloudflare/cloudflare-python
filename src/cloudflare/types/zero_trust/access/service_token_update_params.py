# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ServiceTokenUpdateParams"]


class ServiceTokenUpdateParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    client_secret_version: float
    """
    A version number identifying the current `client_secret` associated with the
    service token. Incrementing it triggers a rotation; the previous secret will
    still be accepted until the time indicated by
    `previous_client_secret_expires_at`. If the service token was reported as
    leaked, `previous_client_secret_expires_at` is not required, may not be in the
    future, and the previous secret is discarded immediately.
    """

    duration: str
    """The duration for how long the service token will be valid.

    Must be in the format `300ms` or `2h45m`, or the special value `forever` for
    non-expiring tokens. Valid time units are: ns, us (or µs), ms, s, m, h. The
    default is 1 year in hours (8760h).
    """

    enabled: bool
    """Whether the service token is enabled.

    A disabled service token cannot be used to authenticate; both its current and
    previous `client_secret` stop being accepted, but the token itself is preserved
    and can be re-enabled. A service token reported as leaked is disabled
    automatically and cannot be re-enabled until its secret is rotated; attempting
    to do so returns a 409. Defaults to enabled when omitted on create.
    """

    name: str
    """The name of the service token."""

    previous_client_secret_expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The expiration of the previous `client_secret`.

    This can be modified at any point after a rotation. For example, you may extend
    it further into the future if you need more time to update services with the new
    secret; or move it into the past to immediately invalidate the previous token in
    case of compromise. Rotating a service token that was reported as leaked
    discards the previous secret entirely, so no grace period can be set.
    """

    tags: Optional[Dict[str, str]]
    """Tags associated with the service token, as key-value pairs.

    On update, replaces all existing tags.
    """
