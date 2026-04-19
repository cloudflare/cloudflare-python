# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DomainGetParams"]


class DomainGetParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    domain: str

    skip_dns: bool
    """Skip DNS resolution lookups for faster response."""
