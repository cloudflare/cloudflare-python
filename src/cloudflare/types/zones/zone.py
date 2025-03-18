# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .type import Type
from ..._models import BaseModel

__all__ = ["Zone", "Account", "Meta", "Owner"]


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


class Zone(BaseModel):
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

    name_servers: List[str]
    """The name servers Cloudflare assigns to a zone"""

    original_dnshost: Optional[str] = None
    """DNS host at the time of switching to Cloudflare"""

    original_name_servers: Optional[List[str]] = None
    """Original name servers before moving to Cloudflare"""

    original_registrar: Optional[str] = None
    """Registrar for the domain at the time of switching to Cloudflare"""

    owner: Owner
    """The owner of the zone"""

    paused: Optional[bool] = None
    """Indicates whether the zone is only using Cloudflare DNS services.

    A true value means the zone will not receive security or performance benefits.
    """

    status: Optional[Literal["initializing", "pending", "active", "moved"]] = None
    """The zone status on Cloudflare."""

    type: Optional[Type] = None
    """A full zone implies that DNS is hosted with Cloudflare.

    A partial zone is typically a partner-hosted zone or a CNAME setup.
    """

    vanity_name_servers: Optional[List[str]] = None
    """An array of domains used for custom name servers.

    This is only available for Business and Enterprise plans.
    """

    verification_key: Optional[str] = None
    """Verification key for partial zone setup."""
