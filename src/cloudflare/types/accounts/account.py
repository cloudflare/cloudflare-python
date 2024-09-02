# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Account", "Settings"]


class Settings(BaseModel):
    abuse_contact_email: Optional[str] = None
    """Sets an abuse contact email to notify for abuse reports."""

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
