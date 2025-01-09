# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DelegationCreateParams"]


class DelegationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of a Cloudflare account."""

    cidr: Required[str]
    """IP Prefix in Classless Inter-Domain Routing format."""

    delegated_account_id: Required[str]
    """Account identifier for the account to which prefix is being delegated."""
