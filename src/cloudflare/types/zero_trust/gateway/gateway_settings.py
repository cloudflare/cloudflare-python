# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["GatewaySettings"]


class GatewaySettings(BaseModel):
    created_at: Optional[datetime] = None

    public_key: Optional[str] = None
    """Provide the Base64-encoded HPKE public key that encrypts SSH session logs.

    See
    https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/use-cases/ssh/ssh-infrastructure-access/#enable-ssh-command-logging.
    """

    seed_id: Optional[str] = None
    """Identify the seed ID."""

    updated_at: Optional[datetime] = None
