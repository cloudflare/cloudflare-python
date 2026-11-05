# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Account", "LegacyFlags", "LegacyFlagsEnterpriseZoneQuota", "ManagedBy", "Settings"]


class LegacyFlagsEnterpriseZoneQuota(BaseModel):
    """Enterprise zone quota for standard and enterprise accounts.

    Accounts without a quota have a maximum of 0.
    """

    available: Optional[int] = None
    """Number of additional Enterprise zones available.

    Returns 0 if the quota is not allocated or is exhausted.
    """

    current: Optional[int] = None
    """Current number of Enterprise zones."""

    maximum: Optional[int] = None
    """Maximum number of Enterprise zones allowed."""


class LegacyFlags(BaseModel):
    """Legacy account flags."""

    enterprise_zone_quota: Optional[LegacyFlagsEnterpriseZoneQuota] = None
    """Enterprise zone quota for standard and enterprise accounts.

    Accounts without a quota have a maximum of 0.
    """


class ManagedBy(BaseModel):
    """Parent container details"""

    parent_org_id: Optional[str] = None
    """ID of the parent Organization, if one exists"""

    parent_org_name: Optional[str] = None
    """Name of the parent Organization, if one exists"""

    root_org_id: Optional[str] = None
    """ID of the root Organization, if one exists"""

    should_display_parent_orgs: Optional[bool] = None
    """Indicates whether the parent Organization hierarchy should be displayed"""


class Settings(BaseModel):
    """Account settings"""

    abuse_contact_email: Optional[str] = None
    """Sets an abuse contact email to notify for abuse reports."""

    enforce_twofactor: Optional[bool] = None
    """
    Indicates whether membership in this account requires that Two-Factor
    Authentication is enabled
    """


class Account(BaseModel):
    id: str
    """Identifier"""

    name: str
    """Account name"""

    type: Literal["standard", "enterprise"]

    created_on: Optional[datetime] = None
    """Timestamp for the creation of the account"""

    legacy_flags: Optional[LegacyFlags] = None
    """Legacy account flags."""

    managed_by: Optional[ManagedBy] = None
    """Parent container details"""

    settings: Optional[Settings] = None
    """Account settings"""
