# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ZoneEditResponse", "Account", "Meta", "Owner"]


class Account(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """The name of the account"""


class Meta(BaseModel):
    cdn_only: Optional[bool] = None
    """The zone is only configured for CDN"""

    custom_certificate_quota: Optional[int] = None
    """Number of Custom Certificates the zone can have"""

    dns_only: Optional[bool] = None
    """The zone is only configured for DNS"""

    foundation_dns: Optional[bool] = None
    """The zone is setup with Foundation DNS"""

    page_rule_quota: Optional[int] = None
    """Number of Page Rules a zone can have"""

    phishing_detected: Optional[bool] = None
    """The zone has been flagged for phishing"""

    step: Optional[int] = None


class Owner(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """Name of the owner"""

    type: Optional[str] = None
    """The type of owner"""


class ZoneEditResponse(BaseModel):
    id: str
    """Identifier"""

    account: Account
    """The account the zone belongs to"""

    activated_on: Optional[datetime] = None
    """The last time proof of ownership was detected and the zone was made active"""

    created_on: datetime
    """When the zone was created"""

    development_mode: float
    """
    The interval (in seconds) from when development mode expires (positive integer)
    or last expired (negative integer) for the domain. If development mode has never
    been enabled, this value is 0.
    """

    meta: Meta
    """Metadata about the zone"""

    modified_on: datetime
    """When the zone was last modified"""

    name: str
    """The domain name"""

    original_dnshost: Optional[str] = None
    """DNS host at the time of switching to Cloudflare"""

    original_name_servers: Optional[List[str]] = None
    """
    Original name servers before moving to Cloudflare Notes: Is this only available
    for full zones?
    """

    original_registrar: Optional[str] = None
    """Registrar for the domain at the time of switching to Cloudflare"""

    owner: Owner
    """The owner of the zone"""

    vanity_name_servers: Optional[List[str]] = None
    """An array of domains used for custom name servers.

    This is only available for Business and Enterprise plans.
    """
