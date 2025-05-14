# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Account", "Settings"]


class Settings(BaseModel):
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

    created_on: Optional[datetime] = None
    """Timestamp for the creation of the account"""

    settings: Optional[Settings] = None
    """Account settings"""
