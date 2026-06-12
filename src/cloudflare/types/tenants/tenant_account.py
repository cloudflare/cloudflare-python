# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TenantAccount", "Settings"]


class Settings(BaseModel):
    abuse_contact_email: Optional[str] = None

    access_approval_expiry: Optional[datetime] = None

    api_access_enabled: Optional[bool] = None

    default_nameservers: Optional[str] = None
    """
    Use
    [DNS Settings](https://developers.cloudflare.com/api/operations/dns-settings-for-an-account-list-dns-settings)
    instead. Deprecated.
    """

    enforce_twofactor: Optional[bool] = None

    use_account_custom_ns_by_default: Optional[bool] = None
    """
    Use
    [DNS Settings](https://developers.cloudflare.com/api/operations/dns-settings-for-an-account-list-dns-settings)
    instead. Deprecated.
    """


class TenantAccount(BaseModel):
    id: str

    created_on: datetime

    name: Optional[str] = None

    settings: Settings

    type: Literal["standard", "enterprise"]
