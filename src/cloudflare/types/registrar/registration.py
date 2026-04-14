# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Registration"]


class Registration(BaseModel):
    """
    A domain registration resource representing the current state of a registered domain.
    """

    auto_renew: bool
    """Whether the domain will be automatically renewed before expiration."""

    created_at: datetime
    """When the domain was registered. Present when the registration resource exists."""

    domain_name: str
    """
    Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
    `mybrand.app`). The domain name uniquely identifies a registration — the same
    domain cannot be registered twice, making it a natural idempotency key for
    registration requests.
    """

    expires_at: Optional[datetime] = None
    """When the domain registration expires.

    Present when the registration is ready; may be null only while `status` is
    `registration_pending`.
    """

    locked: bool
    """Whether the domain is locked for transfer."""

    privacy_mode: Literal["redaction"]
    """Current WHOIS privacy mode for the registration."""

    status: Literal["active", "registration_pending", "expired", "suspended", "redemption_period", "pending_delete"]
    """Current registration status.

    - `active`: Domain is registered and operational
    - `registration_pending`: Registration is in progress
    - `expired`: Domain has expired
    - `suspended`: Domain is suspended by the registry
    - `redemption_period`: Domain is in the redemption grace period
    - `pending_delete`: Domain is pending deletion by the registry
    """
