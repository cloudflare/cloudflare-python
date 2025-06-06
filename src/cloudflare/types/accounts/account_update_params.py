# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountUpdateParams", "Settings"]


class AccountUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    id: Required[str]
    """Identifier"""

    name: Required[str]
    """Account name"""

    settings: Settings
    """Account settings"""


class Settings(TypedDict, total=False):
    abuse_contact_email: str
    """Sets an abuse contact email to notify for abuse reports."""

    enforce_twofactor: bool
    """
    Indicates whether membership in this account requires that Two-Factor
    Authentication is enabled
    """
