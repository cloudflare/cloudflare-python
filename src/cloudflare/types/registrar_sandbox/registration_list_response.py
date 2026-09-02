# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RegistrationListResponse"]


class RegistrationListResponse(BaseModel):
    """
    A domain registration resource representing the current state of a registered domain.
    """

    auto_renew: bool
    """Whether automatic renewal occurs before expiration."""

    created_at: datetime
    """When the domain was registered. Present when the registration resource exists."""

    domain_name: str
    """
    Provides a fully qualified domain name (FQDN), including the extension (e.g.,
    `example.com`, `mybrand.app`). The domain name uniquely identifies a
    registration. Cloudflare permits only one registration per domain, making the
    domain name a natural idempotency key for registration requests.
    """

    expires_at: Optional[datetime] = None
    """When the domain registration expires.

    Ready registrations include this value; only `registration_pending` may return
    null.
    """

    locked: bool
    """Whether the domain is locked for transfer."""

    privacy_mode: Literal["off", "redaction"]
    """Current WHOIS privacy mode for the registration."""

    status: Literal["active", "registration_pending", "expired", "suspended", "redemption_period", "pending_delete"]
    """Current registration status.

    - `active`: The domain operates with an active registration.
    - `registration_pending`: Registration remains in progress.
    - `expired`: The domain registration expired.
    - `suspended`: The registry suspended the domain.
    - `redemption_period`: The domain entered the redemption grace period.
    - `pending_delete`: The registry scheduled the domain for deletion.
    """
