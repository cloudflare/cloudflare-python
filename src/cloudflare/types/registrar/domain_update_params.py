# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DomainUpdateParams"]


class DomainUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    auto_renew: bool
    """
    Auto-renew controls whether subscription is automatically renewed upon domain
    expiration.
    """

    locked: bool
    """Shows whether a registrar lock is in place for a domain."""

    privacy: bool
    """Privacy option controls redacting WHOIS information."""
