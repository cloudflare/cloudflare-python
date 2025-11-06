# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    aud: str
    """The aud of the app."""

    domain: str
    """The domain of the app."""

    exact: bool
    """True for only exact string matches against passed name/domain query parameters."""

    name: str
    """The name of the app."""

    page: int
    """Page number of results."""

    per_page: int
    """Number of results per page."""

    search: str
    """Search for apps by other listed query parameters."""
