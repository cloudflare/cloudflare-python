# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Account", "ManagedBy", "Settings"]


class ManagedBy(BaseModel):
    """Parent container details"""

    parent_org_id: Optional[str] = None
    """ID of the parent Organization, if one exists"""

    parent_org_name: Optional[str] = None
    """Name of the parent Organization, if one exists"""


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

    managed_by: Optional[ManagedBy] = None
    """Parent container details"""

    settings: Optional[Settings] = None
    """Account settings"""
