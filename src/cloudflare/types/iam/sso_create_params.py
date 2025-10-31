# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SSOCreateParams"]


class SSOCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    email_domain: Required[str]
    """Email domain of the new SSO connector"""

    begin_verification: bool
    """Begin the verification process after creation"""
