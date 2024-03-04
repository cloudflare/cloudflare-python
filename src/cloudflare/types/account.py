# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Account", "Settings"]


class Settings(BaseModel):
    default_nameservers: Optional[Literal["cloudflare.standard", "custom.account", "custom.tenant"]] = None
    """
    Specifies the default nameservers to be used for new zones added to this
    account.

    - `cloudflare.standard` for Cloudflare-branded nameservers
    - `custom.account` for account custom nameservers
    - `custom.tenant` for tenant custom nameservers

    See
    [Custom Nameservers](https://developers.cloudflare.com/dns/additional-options/custom-nameservers/)
    for more information.
    """

    enforce_twofactor: Optional[bool] = None
    """
    Indicates whether membership in this account requires that Two-Factor
    Authentication is enabled
    """

    use_account_custom_ns_by_default: Optional[bool] = None
    """
    Indicates whether new zones should use the account-level custom nameservers by
    default.

    Deprecated in favor of `default_nameservers`.
    """


class Account(BaseModel):
    id: str
    """Identifier"""

    name: str
    """Account name"""

    created_on: Optional[datetime] = None
    """Timestamp for the creation of the account"""

    settings: Optional[Settings] = None
    """Account settings"""
